"""
Docstring for genotype submodule
"""
from __future__ import annotations
import typing
__all__ = ['CPPNData', 'Innovations']
class CPPNData:
    """
    C++ supporting type for genomic data
    """
    class Link:
        """
        From-to relationship between two computational node
        """
        def __init__(self, arg0: int, arg1: int, arg2: int, arg3: float) -> None:
            ...
        def __repr__(self) -> str:
            ...
        @property
        def dst(self) -> int:
            """
            ID of the destination node
            """
        @dst.setter
        def dst(self, arg0: int) -> None:
            ...
        @property
        def id(self) -> int:
            """
            Historical marking
            """
        @id.setter
        def id(self, arg0: int) -> None:
            ...
        @property
        def src(self) -> int:
            """
            ID of the source node
            """
        @src.setter
        def src(self, arg0: int) -> None:
            ...
        @property
        def weight(self) -> float:
            """
            Connection weight
            """
        @weight.setter
        def weight(self, arg0: float) -> None:
            ...
    class Links:
        """
        Collection of Links
        """
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None:
            """
            Delete list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> CPPNData.Links:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, arg0: int) -> CPPNData.Link:
            ...
        @typing.overload
        def __init__(self) -> None:
            ...
        @typing.overload
        def __init__(self, arg0: CPPNData.Links) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None:
            ...
        def __iter__(self) -> typing.Iterator[CPPNData.Link]:
            ...
        def __len__(self) -> int:
            ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: CPPNData.Link) -> None:
            ...
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: CPPNData.Links) -> None:
            """
            Assign list elements using a slice object
            """
        def append(self, x: CPPNData.Link) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        @typing.overload
        def extend(self, L: CPPNData.Links) -> None:
            """
            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None:
            """
            Extend the list by appending all the items in the given list
            """
        def insert(self, i: int, x: CPPNData.Link) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> CPPNData.Link:
            """
            Remove and return the last item
            """
        @typing.overload
        def pop(self, i: int) -> CPPNData.Link:
            """
            Remove and return the item at index ``i``
            """
    class Node:
        """
        Computational node of a CPPN
        """
        def __init__(self, arg0: int, arg1: str) -> None:
            ...
        def __repr__(self) -> str:
            ...
        @property
        def func(self) -> str:
            """
            Function used to compute
            """
        @func.setter
        def func(self, arg0: str) -> None:
            ...
        @property
        def id(self) -> int:
            """
            Historical marking
            """
        @id.setter
        def id(self, arg0: int) -> None:
            ...
    class Nodes:
        """
        Collection of Nodes
        """
        def __bool__(self) -> bool:
            """
            Check whether the list is nonempty
            """
        @typing.overload
        def __delitem__(self, arg0: int) -> None:
            """
            Delete the list elements at index ``i``
            """
        @typing.overload
        def __delitem__(self, arg0: slice) -> None:
            """
            Delete list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, s: slice) -> CPPNData.Nodes:
            """
            Retrieve list elements using a slice object
            """
        @typing.overload
        def __getitem__(self, arg0: int) -> CPPNData.Node:
            ...
        @typing.overload
        def __init__(self) -> None:
            ...
        @typing.overload
        def __init__(self, arg0: CPPNData.Nodes) -> None:
            """
            Copy constructor
            """
        @typing.overload
        def __init__(self, arg0: typing.Iterable) -> None:
            ...
        def __iter__(self) -> typing.Iterator[CPPNData.Node]:
            ...
        def __len__(self) -> int:
            ...
        @typing.overload
        def __setitem__(self, arg0: int, arg1: CPPNData.Node) -> None:
            ...
        @typing.overload
        def __setitem__(self, arg0: slice, arg1: CPPNData.Nodes) -> None:
            """
            Assign list elements using a slice object
            """
        def append(self, x: CPPNData.Node) -> None:
            """
            Add an item to the end of the list
            """
        def clear(self) -> None:
            """
            Clear the contents
            """
        @typing.overload
        def extend(self, L: CPPNData.Nodes) -> None:
            """
            Extend the list by appending all the items in the given list
            """
        @typing.overload
        def extend(self, L: typing.Iterable) -> None:
            """
            Extend the list by appending all the items in the given list
            """
        def insert(self, i: int, x: CPPNData.Node) -> None:
            """
            Insert an item at a given position.
            """
        @typing.overload
        def pop(self) -> CPPNData.Node:
            """
            Remove and return the last item
            """
        @typing.overload
        def pop(self, i: int) -> CPPNData.Node:
            """
            Remove and return the item at index ``i``
            """
    @staticmethod
    def from_json(j: dict) -> CPPNData:
        """
        Convert from the json-compliant Python dictionary `j`
        """
    def __getstate__(self) -> dict:
        ...
    def __init__(self) -> None:
        ...
    def __setstate__(self, arg0: dict) -> None:
        ...
    def _sort_by_id(self) -> None:
        """
        Ensures both nodes and links are id-sorted
        """
    def to_json(self) -> dict:
        """
        Convert to a json-compliant Python dictionary
        """
    @property
    def bias(self) -> bool:
        """
        Whether to use an input bias
        """
    @bias.setter
    def bias(self, arg0: bool) -> None:
        ...
    @property
    def inputs(self) -> int:
        """
        Number of inputs
        """
    @inputs.setter
    def inputs(self, arg0: int) -> None:
        ...
    @property
    def labels(self) -> str:
        """
        (optional) label for the inputs/outputs
        """
    @labels.setter
    def labels(self, arg0: str) -> None:
        ...
    @property
    def links(self) -> CPPNData.Links:
        """
        The collection of inter-node relationships
        """
    @links.setter
    def links(self, arg0: CPPNData.Links) -> None:
        ...
    @property
    def nodes(self) -> CPPNData.Nodes:
        """
        The collection of computing nodes
        """
    @nodes.setter
    def nodes(self, arg0: CPPNData.Nodes) -> None:
        ...
    @property
    def outputs(self) -> int:
        """
        Number of outputs
        """
    @outputs.setter
    def outputs(self, arg0: int) -> None:
        ...
class Innovations:
    """
    C++ database for innovation markings
    """
    NOT_FOUND: typing.ClassVar[int] = -1
    @staticmethod
    def from_json(j: dict) -> Innovations:
        """
        Convert from the json-compliant Python dictionary `j`
        """
    def __getstate__(self) -> dict:
        ...
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: dict) -> None:
        ...
    def copy(self) -> Innovations:
        """
        Return a perfect (deep)copy of this innovations database
        """
    def empty(self) -> bool:
        """
        Whether any historical markings have been generated yet
        """
    def get_link_id(self, src: int, dst: int) -> int:
        """
                    Attempt to generate a new link innovation marking for provided key
        
                    :param src: ID of the link's source
                    :param dst: ID of the link's destination
                    :return: The newly created, or existing corresponding *link*
                      innovation marking
        """
    def get_node_id(self, src: int, dst: int) -> int:
        """
                    Attempt to generate a new node innovation marking for provided key
        
                    :param src: ID of the link's source
                    :param dst: ID of the link's destination
                    :return: The newly created, or existing corresponding *node*
                      innovation marking
        """
    def initialize(self, nextNodeID: int) -> None:
        """
                    Reset the database.
        
                    Next node id is set to the provided value and the next link
                    id is set to 0. All known nodes and links mappings are cleared.
        
                    :param nextNodeID: The next node id to give
        """
    def link_id(self, src: int, dst: int) -> int:
        """
                    Retrieve link innovation marking for provided key
        
                    :param src: ID of the link's source
                    :param dst: ID of the link's destination
                    :return: The corresponding *link* innovation marking or
                      :attr:`Innovations.NOT_FOUND` if not found
        """
    def new_link_id(self, src: int, dst: int) -> int:
        """
                    Force generation of a new link innovation marking for provided key
        
                    :param src: ID of the link's source
                    :param dst: ID of the link's destination
                    :return: The newly created *link* innovation marking
        """
    def new_node_id(self, src: int, dst: int) -> int:
        """
                    Force generation of a new node innovation marking for provided key
        
                    :param src: ID of the link's source
                    :param dst: ID of the link's destination
                    :return: The newly created *node* innovation marking
        """
    def next_link_id(self) -> int:
        """
        Historical marking of the next new link
        """
    def next_node_id(self) -> int:
        """
        Historical marking of the next new node
        """
    def node_id(self, src: int, dst: int) -> int:
        """
                    Retrieve node innovation marking for provided key
        
                    The link refers to the link that was broken up to create this new
                     node
        
                    :param src: ID of the link's source
                    :param dst: ID of the link's destination
                    :return: The corresponding *node* innovation marking or
                      :attr:`Innovations.NOT_FOUND` if not found
        """
    def size(self) -> tuple:
        """
        The number of node and link historical markings currently registered
        """
    def to_json(self) -> dict:
        """
        Convert to a json-compliant Python dictionary
        """
