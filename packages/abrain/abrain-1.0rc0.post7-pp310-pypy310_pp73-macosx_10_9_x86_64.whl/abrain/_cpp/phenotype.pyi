"""
Docstring for phenotype submodule
"""
from __future__ import annotations
import _cpp.config
import _cpp.genotype
import typing
__all__ = ['ANN2D', 'ANN3D', 'CPPN', 'CPPN2D', 'CPPN3D', 'Point2D', 'Point3D']
class ANN2D:
    """
    2D Artificial Neural Network produced through Evolvable Substrate Hyper-NEAT
    """
    class IBuffer:
        """
        Input data buffer for an ANN
        """
        @staticmethod
        def __getitem__(*args, **kwargs):
            """
            Access an element
            """
        @staticmethod
        def __init__(*args, **kwargs):
            """
            --
            
            Initialize self. See help(type(self)) for accurate signature.
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __len__(*args, **kwargs):
            ...
        @staticmethod
        def __repr__(*args, **kwargs):
            ...
        @staticmethod
        def __setitem__(*args, **kwargs):
            """
            Assign an element
            """
    class Neuron:
        """
        Atomic computational unit of an ANN
        """
        class Link:
            """
            An incoming neural connection
            """
            @staticmethod
            def __init__(*args, **kwargs):
                """
                --
                
                Initialize self. See help(type(self)) for accurate signature.
                """
            def src(self) -> ANN2D.Neuron:
                """
                Return a reference to the source neuron
                """
            @property
            def weight(self) -> float:
                """
                Connection weight (see :attr:`abrain.Config.annWeightsRange`)
                """
        class Type:
            """
            Members:
            
              I : Input (receiving data)
            
              H : Hidden (processing data)
            
              O : Output (producing data)
            """
            H: typing.ClassVar[ANN2D.Neuron.Type]  # value = <Type.H: 2>
            I: typing.ClassVar[ANN2D.Neuron.Type]  # value = <Type.I: 0>
            O: typing.ClassVar[ANN2D.Neuron.Type]  # value = <Type.O: 1>
            __members__: typing.ClassVar[dict[str, ANN2D.Neuron.Type]]  # value = {'I': <Type.I: 0>, 'H': <Type.H: 2>, 'O': <Type.O: 1>}
            def __eq__(self, other: typing.Any) -> bool:
                ...
            def __getstate__(self) -> int:
                ...
            def __hash__(self) -> int:
                ...
            def __index__(self) -> int:
                ...
            def __int__(self) -> int:
                ...
            def __ne__(self, other: typing.Any) -> bool:
                ...
            def __repr__(self) -> str:
                ...
            def __setstate__(self, state: int) -> None:
                ...
            def __str__(self) -> str:
                ...
            @property
            def name(self) -> str:
                ...
            @property
            def value(self) -> int:
                ...
        @staticmethod
        def __init__(*args, **kwargs):
            """
            --
            
            Initialize self. See help(type(self)) for accurate signature.
            """
        def is_hidden(self) -> bool:
            """
            Whether this neuron is used for internal computations
            """
        def is_input(self) -> bool:
            """
            Whether this neuron is used a an input
            """
        def is_output(self) -> bool:
            """
            Whether this neuron is used a an output
            """
        def links(self) -> list[ANN2D.Neuron.Link]:
            """
            Return the list of inputs connections
            """
        @property
        def bias(self) -> float:
            """
            Neural bias
            """
        @property
        def depth(self) -> int:
            """
            Depth in the neural network
            """
        @property
        def flags(self) -> int:
            """
            Stimuli-dependent flags (for modularization)
            """
        @property
        def pos(self) -> Point2D:
            """
            Position in the 2D substrate
            """
        @property
        def type(self) -> ANN2D.Neuron.Type:
            """
            Neuron role (see :class:`Type`)
            """
        @property
        def value(self) -> float:
            """
            Current activation value
            """
    class Neurons:
        """
        Wrapper for the C++ neurons container
        """
        @staticmethod
        def __init__(*args, **kwargs):
            """
            --
            
            Initialize self. See help(type(self)) for accurate signature.
            """
        def __iter__(self) -> typing.Iterator[ANN2D.Neuron]:
            ...
        def __len__(self) -> int:
            ...
    class OBuffer:
        """
        Output data buffer for an ANN
        """
        @staticmethod
        def __getitem__(*args, **kwargs):
            """
            Access an element
            """
        @staticmethod
        def __init__(*args, **kwargs):
            """
            --
            
            Initialize self. See help(type(self)) for accurate signature.
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __len__(*args, **kwargs):
            ...
        @staticmethod
        def __repr__(*args, **kwargs):
            ...
        @staticmethod
        def __setitem__(*args, **kwargs):
            """
            Assign an element
            """
    class Stats:
        """
        Contains various statistics about an ANN
        """
        @staticmethod
        def __init__(*args, **kwargs):
            """
            --
            
            Initialize self. See help(type(self)) for accurate signature.
            """
        def dict(self) -> dict:
            """
            Return the stats as Python dictionary
            """
        @property
        def axons(self) -> float:
            """
            Total length of the connections
            """
        @property
        def density(self) -> float:
            """
            Ratio of expressed connections
            """
        @property
        def depth(self) -> int:
            """
            Maximal depth of the neural network
            """
        @property
        def edges(self) -> int:
            """
            Number of connections
            """
        @property
        def hidden(self) -> int:
            """
            Number of hidden neurons
            """
        @property
        def iterations(self) -> int:
            """
            H -> H iterations before convergence
            """
        @property
        def utility(self) -> float:
            """
            Ratio of used input/output neurons
            """
    DIMENSIONS: typing.ClassVar[int] = 2
    @staticmethod
    def __init__(*args, **kwargs):
        """
        --
        
        Initialize self. See help(type(self)) for accurate signature.
        """
    @staticmethod
    def build(inputs: list[Point2D], outputs: list[Point2D], genome: _cpp.genotype.CPPNData) -> ANN2D:
        """
        Create an ANN via ES-HyperNEAT
        
        The ANN has inputs/outputs at specified coordinates.
        A CPPN is instantiated from the provided genome and used
        to query connections weight, existence and to discover
        hidden neurons locations
        
        :param inputs: coordinates of the input neurons on the substrate
        :param outputs: coordinates of the output neurons on the substrate
        :param genome: genome describing a cppn (see :class:`abrain.Genome`,
                                                :class:`CPPN`)
        
        .. seealso:: :ref:`usage-basics-ann`
        """
    @staticmethod
    def max_hidden_neurons() -> int:
        """
        How many hidden neurons an ANN could have based on the value of :attr:`~abrain.Config.maxDepth`
        """
    def __call__(self, inputs: ANN2D.IBuffer, outputs: ANN2D.OBuffer, substeps: int = 1) -> None:
        """
        Execute a computational step
        
        Assigns provided input values to corresponding input neurons in the same order
        as when created (see build). Returns output values as computed.
        If not otherwise specified, a single computational substep is executed. If need
        be (e.g. large network, fast response required) you can requested for multiple
        sequential execution in one call
        
        :param inputs: provided analog values for the input neurons
        :param outputs: computed analog values for the output neurons
        :param substeps: number of sequential executions
        
        .. seealso:: :ref:`usage-basics-ann`
        """
    def buffers(self) -> tuple[ANN2D.IBuffer, ANN2D.OBuffer]:
        """
        Return the ann's I/O buffers as a tuple
        """
    def empty(self, strict: bool = False) -> bool:
        """
        Whether the ANN contains neurons/connections
        
        :param strict: whether perceptrons count as empty (true) or not (false)
        
        .. seealso:: `Config::allowPerceptrons`
        """
    def ibuffer(self) -> ANN2D.IBuffer:
        """
        Return a reference to the neural inputs buffer
        """
    def max_edges(self) -> int:
        """
        How many connections this ANN could have based on  the number of inputs/outputs and hidden nodes (if any)
        """
    def neuronAt(self, pos: Point2D) -> ANN2D.Neuron:
        """
        Query an individual neuron
        """
    def neurons(self) -> ANN2D.Neurons:
        """
        Provide read-only access to the underlying neurons
        """
    def obuffer(self) -> ANN2D.OBuffer:
        """
        Return a reference to the neural outputs buffer
        """
    def perceptron(self) -> bool:
        """
        Whether this ANN is a perceptron
        """
    def reset(self) -> None:
        """
        Resets internal state to null (0)
        """
    def stats(self) -> ANN2D.Stats:
        """
        Return associated stats (connections, depth...)
        """
class ANN3D:
    """
    3D Artificial Neural Network produced through Evolvable Substrate Hyper-NEAT
    """
    class IBuffer:
        """
        Input data buffer for an ANN
        """
        @staticmethod
        def __getitem__(*args, **kwargs):
            """
            Access an element
            """
        @staticmethod
        def __init__(*args, **kwargs):
            """
            --
            
            Initialize self. See help(type(self)) for accurate signature.
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __len__(*args, **kwargs):
            ...
        @staticmethod
        def __repr__(*args, **kwargs):
            ...
        @staticmethod
        def __setitem__(*args, **kwargs):
            """
            Assign an element
            """
    class Neuron:
        """
        Atomic computational unit of an ANN
        """
        class Link:
            """
            An incoming neural connection
            """
            @staticmethod
            def __init__(*args, **kwargs):
                """
                --
                
                Initialize self. See help(type(self)) for accurate signature.
                """
            def src(self) -> ANN3D.Neuron:
                """
                Return a reference to the source neuron
                """
            @property
            def weight(self) -> float:
                """
                Connection weight (see :attr:`abrain.Config.annWeightsRange`)
                """
        class Type:
            """
            Members:
            
              I : Input (receiving data)
            
              H : Hidden (processing data)
            
              O : Output (producing data)
            """
            H: typing.ClassVar[ANN3D.Neuron.Type]  # value = <Type.H: 2>
            I: typing.ClassVar[ANN3D.Neuron.Type]  # value = <Type.I: 0>
            O: typing.ClassVar[ANN3D.Neuron.Type]  # value = <Type.O: 1>
            __members__: typing.ClassVar[dict[str, ANN3D.Neuron.Type]]  # value = {'I': <Type.I: 0>, 'H': <Type.H: 2>, 'O': <Type.O: 1>}
            def __eq__(self, other: typing.Any) -> bool:
                ...
            def __getstate__(self) -> int:
                ...
            def __hash__(self) -> int:
                ...
            def __index__(self) -> int:
                ...
            def __int__(self) -> int:
                ...
            def __ne__(self, other: typing.Any) -> bool:
                ...
            def __repr__(self) -> str:
                ...
            def __setstate__(self, state: int) -> None:
                ...
            def __str__(self) -> str:
                ...
            @property
            def name(self) -> str:
                ...
            @property
            def value(self) -> int:
                ...
        @staticmethod
        def __init__(*args, **kwargs):
            """
            --
            
            Initialize self. See help(type(self)) for accurate signature.
            """
        def is_hidden(self) -> bool:
            """
            Whether this neuron is used for internal computations
            """
        def is_input(self) -> bool:
            """
            Whether this neuron is used a an input
            """
        def is_output(self) -> bool:
            """
            Whether this neuron is used a an output
            """
        def links(self) -> list[ANN3D.Neuron.Link]:
            """
            Return the list of inputs connections
            """
        @property
        def bias(self) -> float:
            """
            Neural bias
            """
        @property
        def depth(self) -> int:
            """
            Depth in the neural network
            """
        @property
        def flags(self) -> int:
            """
            Stimuli-dependent flags (for modularization)
            """
        @property
        def pos(self) -> Point3D:
            """
            Position in the 3D substrate
            """
        @property
        def type(self) -> ANN3D.Neuron.Type:
            """
            Neuron role (see :class:`Type`)
            """
        @property
        def value(self) -> float:
            """
            Current activation value
            """
    class Neurons:
        """
        Wrapper for the C++ neurons container
        """
        @staticmethod
        def __init__(*args, **kwargs):
            """
            --
            
            Initialize self. See help(type(self)) for accurate signature.
            """
        def __iter__(self) -> typing.Iterator[ANN3D.Neuron]:
            ...
        def __len__(self) -> int:
            ...
    class OBuffer:
        """
        Output data buffer for an ANN
        """
        @staticmethod
        def __getitem__(*args, **kwargs):
            """
            Access an element
            """
        @staticmethod
        def __init__(*args, **kwargs):
            """
            --
            
            Initialize self. See help(type(self)) for accurate signature.
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __len__(*args, **kwargs):
            ...
        @staticmethod
        def __repr__(*args, **kwargs):
            ...
        @staticmethod
        def __setitem__(*args, **kwargs):
            """
            Assign an element
            """
    class Stats:
        """
        Contains various statistics about an ANN
        """
        @staticmethod
        def __init__(*args, **kwargs):
            """
            --
            
            Initialize self. See help(type(self)) for accurate signature.
            """
        def dict(self) -> dict:
            """
            Return the stats as Python dictionary
            """
        @property
        def axons(self) -> float:
            """
            Total length of the connections
            """
        @property
        def density(self) -> float:
            """
            Ratio of expressed connections
            """
        @property
        def depth(self) -> int:
            """
            Maximal depth of the neural network
            """
        @property
        def edges(self) -> int:
            """
            Number of connections
            """
        @property
        def hidden(self) -> int:
            """
            Number of hidden neurons
            """
        @property
        def iterations(self) -> int:
            """
            H -> H iterations before convergence
            """
        @property
        def utility(self) -> float:
            """
            Ratio of used input/output neurons
            """
    DIMENSIONS: typing.ClassVar[int] = 3
    @staticmethod
    def __init__(*args, **kwargs):
        """
        --
        
        Initialize self. See help(type(self)) for accurate signature.
        """
    @staticmethod
    def build(inputs: list[Point3D], outputs: list[Point3D], genome: _cpp.genotype.CPPNData) -> ANN3D:
        """
        Create an ANN via ES-HyperNEAT
        
        The ANN has inputs/outputs at specified coordinates.
        A CPPN is instantiated from the provided genome and used
        to query connections weight, existence and to discover
        hidden neurons locations
        
        :param inputs: coordinates of the input neurons on the substrate
        :param outputs: coordinates of the output neurons on the substrate
        :param genome: genome describing a cppn (see :class:`abrain.Genome`,
                                                :class:`CPPN`)
        
        .. seealso:: :ref:`usage-basics-ann`
        """
    @staticmethod
    def max_hidden_neurons() -> int:
        """
        How many hidden neurons an ANN could have based on the value of :attr:`~abrain.Config.maxDepth`
        """
    def __call__(self, inputs: ANN3D.IBuffer, outputs: ANN3D.OBuffer, substeps: int = 1) -> None:
        """
        Execute a computational step
        
        Assigns provided input values to corresponding input neurons in the same order
        as when created (see build). Returns output values as computed.
        If not otherwise specified, a single computational substep is executed. If need
        be (e.g. large network, fast response required) you can requested for multiple
        sequential execution in one call
        
        :param inputs: provided analog values for the input neurons
        :param outputs: computed analog values for the output neurons
        :param substeps: number of sequential executions
        
        .. seealso:: :ref:`usage-basics-ann`
        """
    def buffers(self) -> tuple[ANN3D.IBuffer, ANN3D.OBuffer]:
        """
        Return the ann's I/O buffers as a tuple
        """
    def empty(self, strict: bool = False) -> bool:
        """
        Whether the ANN contains neurons/connections
        
        :param strict: whether perceptrons count as empty (true) or not (false)
        
        .. seealso:: `Config::allowPerceptrons`
        """
    def ibuffer(self) -> ANN3D.IBuffer:
        """
        Return a reference to the neural inputs buffer
        """
    def max_edges(self) -> int:
        """
        How many connections this ANN could have based on  the number of inputs/outputs and hidden nodes (if any)
        """
    def neuronAt(self, pos: Point3D) -> ANN3D.Neuron:
        """
        Query an individual neuron
        """
    def neurons(self) -> ANN3D.Neurons:
        """
        Provide read-only access to the underlying neurons
        """
    def obuffer(self) -> ANN3D.OBuffer:
        """
        Return a reference to the neural outputs buffer
        """
    def perceptron(self) -> bool:
        """
        Whether this ANN is a perceptron
        """
    def reset(self) -> None:
        """
        Resets internal state to null (0)
        """
    def stats(self) -> ANN3D.Stats:
        """
        Return associated stats (connections, depth...)
        """
class CPPN:
    """
    Generic CPPN for regular use (images, morphologies, etc.)
    """
    class IBuffer:
        """
        Input data buffer for a CPPN
        """
        @staticmethod
        def __getitem__(*args, **kwargs):
            """
            Access an element
            """
        @staticmethod
        def __init__(*args, **kwargs):
            """
            --
            
            Initialize self. See help(type(self)) for accurate signature.
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __len__(*args, **kwargs):
            ...
        @staticmethod
        def __repr__(*args, **kwargs):
            ...
        @staticmethod
        def __setitem__(*args, **kwargs):
            """
            Assign an element
            """
    class OBuffer:
        """
        Output data buffer for a CPPN
        """
        @staticmethod
        def __getitem__(*args, **kwargs):
            """
            Access an element
            """
        @staticmethod
        def __init__(*args, **kwargs):
            """
            --
            
            Initialize self. See help(type(self)) for accurate signature.
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __len__(*args, **kwargs):
            ...
        @staticmethod
        def __repr__(*args, **kwargs):
            ...
        @staticmethod
        def __setitem__(*args, **kwargs):
            """
            Assign an element
            """
    _docstrings: typing.ClassVar[dict] = {'DIMENSIONS': 'for the I/O coordinates', 'INPUTS': 'Number of inputs', 'OUTPUTS': 'Number of outputs', 'OUTPUTS_LIST': 'The list of output types the CPPN can produce'}
    @staticmethod
    def functions() -> dict[str, typing.Callable[[float], float]]:
        """
        Return a copy of the C++ built-in function set
        """
    @typing.overload
    def __call__(self, outputs: CPPN.OBuffer, inputs: CPPN.IBuffer) -> None:
        """
        Evaluates on provided inputs and retrieve all outputs
        """
    @typing.overload
    def __call__(self, output: int, inputs: CPPN.IBuffer) -> float:
        """
        Evaluates on provided inputs and retrieve requested output
        """
    @typing.overload
    def __call__(self, outputs: CPPN.OBuffer, inputs: list) -> None:
        """
        Evaluates on provided inputs and retrieve all outputs
        """
    @typing.overload
    def __call__(self, output: int, inputs: list) -> float:
        """
        Evaluates on provided inputs and retrieve requested output
        """
    @typing.overload
    def __call__(self, outputs: CPPN.OBuffer, *args) -> None:
        """
        Evaluates on provided inputs and retrieve all outputs
        """
    @typing.overload
    def __call__(self, output: int, *args) -> float:
        """
        Evaluates on provided inputs and retrieve requested output
        """
    def ibuffer(self) -> CPPN.IBuffer:
        """
        Buffer for input data
        """
    def n_hidden(self) -> int:
        """
        Return the number of internal nodes
        """
    def n_inputs(self, with_bias: bool = False) -> int:
        """
        Return the number of inputs
        """
    def n_outputs(self) -> int:
        """
        Return the number of outputs
        """
    def obuffer(self) -> CPPN.OBuffer:
        """
        Buffer for output data
        """
    def outputs(self) -> CPPN.OBuffer:
        """
        Return a buffer in which the CPPN can store output data
        """
class CPPN2D(CPPN):
    """
    Created from a :class:`~abrain.Genome` and used to generate, via ES-HyperNEAT, an :class:`~abrain.ANN2D`
    """
    DIMENSIONS: typing.ClassVar[int] = 2
    Point = Point2D
    @typing.overload
    def __call__(self, src: Point2D, dst: Point2D, buffer: CPPN.OBuffer) -> None:
        """
        Evaluates on provided coordinates and retrieve all outputs
        """
    @typing.overload
    def __call__(self, src: Point2D, dst: Point2D, type: _cpp.config.Config.ESHNOutputs) -> float:
        """
        Evaluates on provided coordinates for the requested output
        
        .. note: due to an i686 bug this function is unoptimized on said platforms
        """
    @typing.overload
    def __call__(self, src: Point2D, dst: Point2D, buffer: CPPN.OBuffer, subset: set[_cpp.config.Config.ESHNOutputs]) -> None:
        """
        Evaluates on provided coordinates for the requested outputs
        """
    def __init__(self, arg0: _cpp.genotype.CPPNData) -> None:
        """
        Create from a :class:`abrain.Genome`
        """
class CPPN3D(CPPN):
    """
    Created from a :class:`~abrain.Genome` and used to generate, via ES-HyperNEAT, an :class:`~abrain.ANN3D`
    """
    DIMENSIONS: typing.ClassVar[int] = 3
    Point = Point3D
    @typing.overload
    def __call__(self, src: Point3D, dst: Point3D, buffer: CPPN.OBuffer) -> None:
        """
        Evaluates on provided coordinates and retrieve all outputs
        """
    @typing.overload
    def __call__(self, src: Point3D, dst: Point3D, type: _cpp.config.Config.ESHNOutputs) -> float:
        """
        Evaluates on provided coordinates for the requested output
        
        .. note: due to an i686 bug this function is unoptimized on said platforms
        """
    @typing.overload
    def __call__(self, src: Point3D, dst: Point3D, buffer: CPPN.OBuffer, subset: set[_cpp.config.Config.ESHNOutputs]) -> None:
        """
        Evaluates on provided coordinates for the requested outputs
        """
    def __init__(self, arg0: _cpp.genotype.CPPNData) -> None:
        """
        Create from a :class:`abrain.Genome`
        """
class Point2D:
    """
    2D coordinate using fixed point notation with 3 decimals
    """
    DIMENSIONS: typing.ClassVar[int] = 2
    @staticmethod
    def null() -> Point2D:
        """
        Return the null vector
        """
    def __eq__(self, arg0: Point2D) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __init__(self, x: float, y: float) -> None:
        """
        Create a point with the specified coordinates
        
        Args:
          x, y (float): x, y coordinate
        """
    def __ne__(self, arg0: Point2D) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def tuple(self) -> tuple[float, float]:
        """
        Return a tuple for easy unpacking in python
        """
class Point3D:
    """
    3D coordinate using fixed point notation with 3 decimals
    """
    DIMENSIONS: typing.ClassVar[int] = 3
    @staticmethod
    def null() -> Point3D:
        """
        Return the null vector
        """
    def __eq__(self, arg0: Point3D) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __init__(self, x: float, y: float, z: float) -> None:
        """
        Create a point with the specified coordinates
        
        Args:
          x, y, z (float): x, y, z coordinate
        """
    def __ne__(self, arg0: Point3D) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def tuple(self) -> tuple[float, float, float]:
        """
        Return a tuple for easy unpacking in python
        """
