# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Mesh/Solution.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Mesh/Solution
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ._frozen import FrozenClass

from ._check import InitUnKnowClassError


class Solution(FrozenClass):
    """Abstract class for solution related classes."""

    VERSION = 1

    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        type_cell="triangle",
        label=None,
        dimension=2,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            type_cell = obj.type_cell
            label = obj.label
            dimension = obj.dimension
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "type_cell" in list(init_dict.keys()):
                type_cell = init_dict["type_cell"]
            if "label" in list(init_dict.keys()):
                label = init_dict["label"]
            if "dimension" in list(init_dict.keys()):
                dimension = init_dict["dimension"]
        # Initialisation by argument
        self.parent = None
        self.type_cell = type_cell
        self.label = label
        self.dimension = dimension

        # The class is frozen, for now it's impossible to add new properties
        self._freeze()

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        Solution_str = ""
        if self.parent is None:
            Solution_str += "parent = None " + linesep
        else:
            Solution_str += "parent = " + str(type(self.parent)) + " object" + linesep
        Solution_str += 'type_cell = "' + str(self.type_cell) + '"' + linesep
        Solution_str += 'label = "' + str(self.label) + '"' + linesep
        Solution_str += "dimension = " + str(self.dimension) + linesep
        return Solution_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False
        if other.type_cell != self.type_cell:
            return False
        if other.label != self.label:
            return False
        if other.dimension != self.dimension:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        Solution_dict = dict()
        Solution_dict["type_cell"] = self.type_cell
        Solution_dict["label"] = self.label
        Solution_dict["dimension"] = self.dimension
        # The class name is added to the dict fordeserialisation purpose
        Solution_dict["__class__"] = "Solution"
        return Solution_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.type_cell = None
        self.label = None
        self.dimension = None

    def _get_type_cell(self):
        """getter of type_cell"""
        return self._type_cell

    def _set_type_cell(self, value):
        """setter of type_cell"""
        check_var("type_cell", value, "str")
        self._type_cell = value

    type_cell = property(
        fget=_get_type_cell,
        fset=_set_type_cell,
        doc=u"""Type of cell (Point, Segment2, Triangle3, etc.)

        :Type: str
        """,
    )

    def _get_label(self):
        """getter of label"""
        return self._label

    def _set_label(self, value):
        """setter of label"""
        check_var("label", value, "str")
        self._label = value

    label = property(
        fget=_get_label,
        fset=_set_label,
        doc=u"""Label to identify the solution

        :Type: str
        """,
    )

    def _get_dimension(self):
        """getter of dimension"""
        return self._dimension

    def _set_dimension(self, value):
        """setter of dimension"""
        check_var("dimension", value, "int", Vmin=1, Vmax=3)
        self._dimension = value

    dimension = property(
        fget=_get_dimension,
        fset=_set_dimension,
        doc=u"""Dimension of the physical problem

        :Type: int
        :min: 1
        :max: 3
        """,
    )
