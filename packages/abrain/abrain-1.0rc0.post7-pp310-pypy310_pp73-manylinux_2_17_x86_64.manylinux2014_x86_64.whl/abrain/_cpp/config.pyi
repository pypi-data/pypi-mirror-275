"""
Docstring for config submodule
"""
from __future__ import annotations
import typing
__all__ = ['Config', 'MutationRates', 'OutputFunctions']
class Config:
    """
    C++/Python configuration values for the ABrain library
    """
    class ESHNOutputs:
        """
        Members:
        
          Weight
        
          LEO
        
          Bias
        """
        Bias: typing.ClassVar[Config.ESHNOutputs]  # value = <ESHNOutputs.Bias: 2>
        LEO: typing.ClassVar[Config.ESHNOutputs]  # value = <ESHNOutputs.LEO: 1>
        Weight: typing.ClassVar[Config.ESHNOutputs]  # value = <ESHNOutputs.Weight: 0>
        __members__: typing.ClassVar[dict[str, Config.ESHNOutputs]]  # value = {'Weight': <ESHNOutputs.Weight: 0>, 'LEO': <ESHNOutputs.LEO: 1>, 'Bias': <ESHNOutputs.Bias: 2>}
        @staticmethod
        def __eq__(*args, **kwargs):
            ...
        @staticmethod
        def __getstate__(*args, **kwargs):
            ...
        @staticmethod
        def __hash__(*args, **kwargs):
            ...
        @staticmethod
        def __index__(*args, **kwargs):
            ...
        @staticmethod
        def __int__(*args, **kwargs):
            ...
        @staticmethod
        def __iter__() -> dict:
            ...
        @staticmethod
        def __ne__(*args, **kwargs):
            ...
        @staticmethod
        def __repr__(*args, **kwargs):
            ...
        @staticmethod
        def __setstate__(*args, **kwargs):
            ...
        @staticmethod
        def __str__(*args, **kwargs):
            ...
        @property
        def name(*args, **kwargs):
            """
            Name of the output
            """
        @property
        def value(*args, **kwargs):
            """
            Corresponding value of the output
            """
    class FBounds:
        """
        C++ encapsulation for mutation bounds
        """
        __hash__: typing.ClassVar[None] = None
        max: float
        min: float
        rndMax: float
        rndMin: float
        stddev: float
        @staticmethod
        def fromJson(arg0: list[float]) -> Config.FBounds:
            """
            Convert from a python list of floats
            """
        def __eq__(self, arg0: Config.FBounds) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def isValid(self) -> bool:
            """
            Whether this is a valid mutation bounds object
            """
        def toJson(self) -> list:
            """
            Convert to a python list of floats
            """
    class Strings:
        """
        C++ list of strings
        """
        __hash__: typing.ClassVar[None] = None
        @staticmethod
        def __bool__(*args, **kwargs):
            """
            Check whether the list is nonempty
            """
        @staticmethod
        def __contains__(*args, **kwargs):
            """
            Return true the container contains ``x``
            """
        @staticmethod
        def __delitem__(*args, **kwargs):
            """
            Delete the list elements at index ``i``
            Delete list elements using a slice object
            """
        @staticmethod
        def __eq__(*args, **kwargs):
            ...
        @staticmethod
        def __getitem__(*args, **kwargs):
            """
            Retrieve list elements using a slice object
            """
        @staticmethod
        def __init__(*args, **kwargs):
            """
            Copy constructor
            """
        @staticmethod
        def __iter__(*args, **kwargs):
            ...
        @staticmethod
        def __len__(*args, **kwargs):
            ...
        @staticmethod
        def __ne__(*args, **kwargs):
            ...
        @staticmethod
        def __repr__(*args, **kwargs):
            """
            Return the canonical string representation of this list.
            """
        @staticmethod
        def __setitem__(*args, **kwargs):
            """
            Assign list elements using a slice object
            """
        @staticmethod
        def append(*args, **kwargs):
            """
            Add an item to the end of the list
            """
        @staticmethod
        def clear(*args, **kwargs):
            """
            Clear the contents
            """
        @staticmethod
        def count(*args, **kwargs):
            """
            Return the number of times ``x`` appears in the list
            """
        @staticmethod
        def extend(*args, **kwargs):
            """
            Extend the list by appending all the items in the given list
            Extend the list by appending all the items in the given list
            """
        @staticmethod
        def fromJson(arg0: list) -> Config.Strings:
            """
            Convert from a python list of strings
            """
        @staticmethod
        def insert(*args, **kwargs):
            """
            Insert an item at a given position.
            """
        @staticmethod
        def pop(*args, **kwargs):
            """
            Remove and return the last item
            Remove and return the item at index ``i``
            """
        @staticmethod
        def remove(*args, **kwargs):
            """
            Remove the first item from the list whose value is x. It is an error if there is no such item.
            """
        def isValid(self) -> bool:
            """
            Whether this is a valid strings collection (not empty)
            """
        def toJson(self) -> list:
            """
            Convert to a python list of strings
            """
    Bias: typing.ClassVar[Config.ESHNOutputs]  # value = <ESHNOutputs.Bias: 2>
    LEO: typing.ClassVar[Config.ESHNOutputs]  # value = <ESHNOutputs.LEO: 1>
    Weight: typing.ClassVar[Config.ESHNOutputs]  # value = <ESHNOutputs.Weight: 0>
    _docstrings: typing.ClassVar[dict] = {'activationFunc': 'The activation function used by all hidden/output neurons (inputs are passthrough)', 'allowPerceptrons': 'Attempt to generate a perceptron if no hidden neurons were discovered', 'annWeightsRange': 'Scaling factor `s` for the CPPN `w` output mapping :math:`[-1,1] to [-s,s]`', 'bndThr': 'Minimal divergence threshold for discovering neurons', 'cppnWeightBounds': "Initial and maximal bounds for each of the CPPN's weights", 'defaultOutputFunction': 'Output function for random generic CPPNs', 'divThr': 'Division threshold for a quad-/octtree cell/cube', 'eshnOutputFunctions': 'Functions used for :class:`CPPN2D` and :class:`CPPN3D` outputs', 'functionSet': 'List of functions accessible to nodes via creation/mutation', 'initialDepth': 'Initial division depth for the underlying quad-/octtree', 'iterations': 'Maximal number of discovery steps for Hidden/Hidden connections. Can stop early in case of convergence (no new neurons discovered)', 'maxDepth': 'Maximal division depth for the underlying quad-/octtree', 'mutationRates': 'Probabilities for each point mutation (addition/deletion/alteration)\n\nGlossary:\n  - add_l: add a random link between two nodes (feedforward only)\n  - add_n: replace a link by creating a node\n  - del_l: delete a random link (never leaves unconnected nodes)\n  - del_n: replace a simple node by a direct link\n  - mut_f: change the function of a node\n  - mut_w: change the connection weight of a link\n\n', 'varThr': 'Variance threshold for exploring a quad-/octtree cell/cube'}
    _sections: typing.ClassVar[dict]  # value = {'ANN': Strings[annWeightsRange, activationFunc], 'CPPN': Strings[functionSet, defaultOutputFunction, eshnOutputFunctions, mutationRates, cppnWeightBounds], 'ESHN': Strings[initialDepth, maxDepth, iterations, divThr, varThr, bndThr, allowPerceptrons]}
    activationFunc: typing.ClassVar[str] = 'ssgn'
    allowPerceptrons: typing.ClassVar[bool] = True
    annWeightsRange: typing.ClassVar[float] = 3.0
    bndThr: typing.ClassVar[float] = 0.15000000596046448
    cppnWeightBounds: typing.ClassVar[Config.FBounds]  # value = Bounds(-3, -1, 1, 3, 0.01)
    defaultOutputFunction: typing.ClassVar[str] = 'id'
    divThr: typing.ClassVar[float] = 0.30000001192092896
    eshnOutputFunctions: typing.ClassVar[OutputFunctions]  # value = OutputFunctions{0: bsgm, 1: step, 2: id}
    functionSet: typing.ClassVar[Config.Strings]  # value = Strings[abs, gaus, id, bsgm, sin, step]
    initialDepth: typing.ClassVar[int] = 2
    iterations: typing.ClassVar[int] = 10
    maxDepth: typing.ClassVar[int] = 3
    mutationRates: typing.ClassVar[MutationRates]  # value = MutationRates{add_l: 0.0681818, add_n: 0.0454545, del_l: 0.0909091, del_n: 0.0681818, mut_f: 0.227273, mut_w: 0.5}
    varThr: typing.ClassVar[float] = 0.30000001192092896
    @staticmethod
    def __init__(*args, **kwargs):
        """
        --
        
        Initialize self. See help(type(self)) for accurate signature.
        """
    @staticmethod
    def known_function(name: str) -> bool:
        """
        Whether the requested function name is a built-in
        """
    @staticmethod
    def test_valid() -> bool:
        """
        Function used after reading a configuration file to ensure validity
        """
class MutationRates:
    """
    C++ mapping between mutation types and rates
    """
    @staticmethod
    def __bool__(*args, **kwargs):
        """
        Check whether the map is nonempty
        """
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        """
        Return the canonical string representation of this map.
        """
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def fromJson(arg0: dict) -> MutationRates:
        """
        Convert from a python map of strings/floats
        """
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def keys(*args, **kwargs):
        ...
    @staticmethod
    def values(*args, **kwargs):
        ...
    def isValid(self) -> bool:
        """
        Whether this is a valid dictionary of mutation rates
        """
    def toJson(self) -> dict:
        """
        Convert to a python map of strings/float
        """
class OutputFunctions:
    """
    C++ mapping between CPPN's outputs, when used with ES-HyperNEAT, and functions
    """
    @staticmethod
    def __bool__(*args, **kwargs):
        """
        Check whether the map is nonempty
        """
    @staticmethod
    def __contains__(*args, **kwargs):
        ...
    @staticmethod
    def __delitem__(*args, **kwargs):
        ...
    @staticmethod
    def __getitem__(*args, **kwargs):
        ...
    @staticmethod
    def __iter__(*args, **kwargs):
        ...
    @staticmethod
    def __len__(*args, **kwargs):
        ...
    @staticmethod
    def __repr__(*args, **kwargs):
        """
        Return the canonical string representation of this map.
        """
    @staticmethod
    def __setitem__(*args, **kwargs):
        ...
    @staticmethod
    def fromJson(arg0: dict) -> OutputFunctions:
        """
        Convert from a python dict
        """
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def keys(*args, **kwargs):
        ...
    @staticmethod
    def values(*args, **kwargs):
        ...
    def isValid(self) -> bool:
        """
        Whether this is a collection of output functions
        """
    def toJson(self) -> dict:
        """
        Convert to a python dict
        """
