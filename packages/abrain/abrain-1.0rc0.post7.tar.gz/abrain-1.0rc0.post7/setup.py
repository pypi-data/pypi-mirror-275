import itertools
import os
import re
import subprocess
import sys
from distutils.command.build import build
from pathlib import Path

from setuptools import Extension, setup, Command
from setuptools.command.build_ext import build_ext

# Convert distutils Windows platform specifiers to CMake -A arguments
PLAT_TO_CMAKE = {
    "win32": "Win32",
    "win-amd64": "x64",
    "win-arm32": "ARM",
    "win-arm64": "ARM64",
}


# A CMakeExtension needs a sourcedir instead of a file list.
# The name must be the _single_ output extension from the CMake build.
# If you need multiple extensions, see scikit-build.
class CMakeExtension(Extension):
    def __init__(self, name: str, sourcedir: str = "") -> None:
        super().__init__(name, sources=[])
        self.sourcedir = os.fspath(Path(sourcedir).resolve())


class CMakeBuild(build_ext):
    def build_extension(self, ext: CMakeExtension) -> None:
        # Must be in this form due to bug in .resolve() only fixed in
        #  Python 3.10+
        ext_fullpath = Path.cwd() / self.get_ext_fullpath(ext.name) \
            # type: ignore[no-untyped-call]
        extdir = ext_fullpath.parent.resolve()

        # Using this requires trailing slash for auto-detection & inclusion of
        # auxiliary "native" libs

        # == kgd - Additions == #
        with_tests = bool(os.environ.get("TEST", 0))
        if with_tests:
            debug = True
        else:
            debug = int(os.environ.get("DEBUG", 0)) \
                if self.debug is None else self.debug
        cfg = "Debug" if debug else "Release"

        dev_build = bool(os.environ.get("DEV", 0))

        # ===================== #

        # CMake lets you override the generator - we need to check this.
        # Can be set with Conda-Build, for example.
        cmake_generator = os.environ.get("CMAKE_GENERATOR", "")

        # Set Python_EXECUTABLE instead if you use PYBIND11_FINDPYTHON
        # EXAMPLE_VERSION_INFO shows you how to pass a value into the C++ code
        # from Python.
        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}{os.sep}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-DCMAKE_BUILD_TYPE={cfg}",  # not used on MSVC, but no harm
        ]
        build_args = []
        # Adding CMake arguments set as environment variable
        # (needed e.g. to build for ARM OSx on conda-forge)

        if "CMAKE_ARGS" in os.environ:
            cmake_args += [item for item in os.environ["CMAKE_ARGS"].split(" ")
                           if item]

        # Pass the version to C++ (why not?)
        if version := self.distribution.get_version():
            # type: ignore[attr-defined]
            cmake_args += [f"-DVERSION_INFO={version}"]
        else:
            print("No version")

        if self.compiler.compiler_type != "msvc":
            # Using Ninja-build since it a) is available as a wheel and b)
            # multithreads automatically. MSVC would require all variables be
            # exported for Ninja to pick it up, which is a little tricky to do.
            # Users can override the generator with CMAKE_GENERATOR in CMake
            # 3.15+.
            if not cmake_generator or cmake_generator == "Ninja":
                try:
                    import ninja  # noqa

                    ninja_executable_path = Path(ninja.BIN_DIR) / "ninja"
                    cmake_args += [
                        "-GNinja",
                        f"-DCMAKE_MAKE_PROGRAM:FILEPATH="
                        f"{ninja_executable_path}"
                    ]
                except ImportError:
                    pass

        else:

            # Single config generators are handled "normally"
            single_config = any(x in cmake_generator for x in
                                {"NMake", "Ninja"})

            # CMake allows an arch-in-generator style for backward
            # compatibility
            contains_arch = any(x in cmake_generator for x in
                                {"ARM", "Win64"})

            # Specify the arch if using MSVC generator, but only if it doesn't
            # contain a backward-compatibility arch spec already in the
            # generator name.
            if not single_config and not contains_arch:
                cmake_args += ["-A", PLAT_TO_CMAKE[self.plat_name]]

            # Multi-config generators have a different way to specify configs
            if not single_config:
                cmake_args += [
                    f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{cfg.upper()}={extdir}"
                ]
                build_args += ["--config", cfg]

        if sys.platform.startswith("darwin"):
            # Cross-compile support for macOS - respect ARCHFLAGS if set
            archs = re.findall(r"-arch (\S+)", os.environ.get("ARCHFLAGS", ""))
            if archs:
                cmake_args += \
                    ["-DCMAKE_OSX_ARCHITECTURES={}".format(";".join(archs))]

        # Set CMAKE_BUILD_PARALLEL_LEVEL to control the parallel build level
        # across all generators.
        if "CMAKE_BUILD_PARALLEL_LEVEL" not in os.environ:
            # self.parallel is a Python 3 only way to set parallel jobs by hand
            # using -j in the build_ext call, not supported by pip or
            # PyPA-build
            if hasattr(self, "parallel") and self.parallel:
                # CMake 3.12+ only.
                build_args += [f"-j{self.parallel}"]

        build_temp = Path(self.build_temp) / ext.name
        if not build_temp.exists():
            build_temp.mkdir(parents=True)

        # == kgd - Additions == #
        if with_tests:
            cmake_args += ["-DWITH_COVERAGE=ON"]
        # Forward if we need develop-level info (notably the stubs)
        if dev_build:
            cmake_args += ["-DDEV_BUILD=ON"]

        # ===================== #
        # Write clion configuration (if requested)
        if (path := os.environ.get("CLION_CONFIG")) is not None:
            with open(path, "w") as cc:
                cc.write("Replace the ninja builder with default (Makefile)\n")
                cc.write("Replace the default build folder with:\n")
                cc.write(f"\t{build_temp}\n")
                cc.write("Give the following arguments for cmake:\n")
                config_str = ' '.join(['-DAUTO_INSTALL=ON'] + cmake_args)
                cc.write(f"\t{config_str}\n")
                cc.write("Ensure the build command looks like:\n")
                build_str = ' '.join(['cmake', '--build', '.'] + build_args)
                cc.write(f"       build: {build_str}\n")
        # ===================== #

        # Allow discovering packages in build site-packages (overlay?)
        cmake_args += [f"-DCMAKE_PREFIX_PATH={';'.join(sys.path)}"]
        # Ensure discovery of executables (pybind11-stubgen for instance)
        cmake_args += [f"-DBUILD_TIME_PATH={os.environ.get('PATH')}"]

        subprocess.run(
            ["cmake", ext.sourcedir] + cmake_args, cwd=build_temp, check=True
        )
        subprocess.run(
            ["cmake", "--build", "."] + build_args, cwd=build_temp, check=True
        )


class BuildData(Command):
    description = "Build data"
    user_options = []
    def initialize_options(self): pass
    def finalize_options(self): pass

    def run(self):
        if not os.path.exists("src/abrain/core/functions/id.png"):
            subprocess.check_call("src/abrain/core/functions/plotter.sh")


def is_build_ext(item): return item[0] == 'build_ext'


class CustomBuildOrder(build):
    def finalize_options(self) -> None:
        super().finalize_options()
        t1, t2 = itertools.tee(self.sub_commands)
        build_ext = filter(is_build_ext, t1)
        tail = itertools.filterfalse(is_build_ext, t2)
        self.sub_commands[:] = list(build_ext) + list(tail)


# Most metadata is in pyproject.toml
setup(
    package_data={'': ['*.eps', '*.png', '*.svg', '*.pyi']},
    include_package_data=True,

    ext_modules=[CMakeExtension("abrain._cpp")],
    cmdclass={
        'build_ext': CMakeBuild,
        'build_data': BuildData,
        'build': CustomBuildOrder
    },
)
