# -*- coding: utf-8 -*-
# File generated according to Generator/ClassesRef/Output/OutMagElmer.csv
# WARNING! All changes made in this file will be lost!
"""Method code available at https://github.com/Eomys/pyleecan/tree/master/pyleecan/Methods/Output/OutMagElmer
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from ..Functions.copy import copy
from ..Functions.load import load_init_dict
from ..Functions.Load.import_class import import_class
from .OutInternal import OutInternal

from ._check import InitUnKnowClassError


class OutMagElmer(OutInternal):
    """Class to store outputs related to MagElmer magnetic model"""

    VERSION = 1

    # save and copy methods are available in all object
    save = save
    copy = copy
    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(self, FEA_dict=None, init_dict = None, init_str = None):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for pyleecan type, -1 will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with property names as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if init_str is not None:  # Load from a file
            init_dict = load_init_dict(init_str)[1]
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "FEA_dict" in list(init_dict.keys()):
                FEA_dict = init_dict["FEA_dict"]
        # Set the properties (value check and convertion are done in setter)
        self.FEA_dict = FEA_dict
        # Call OutInternal init
        super(OutMagElmer, self).__init__()
        # The class is frozen (in OutInternal init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this object in a readeable string (for print)"""

        OutMagElmer_str = ""
        # Get the properties inherited from OutInternal
        OutMagElmer_str += super(OutMagElmer, self).__str__()
        OutMagElmer_str += "FEA_dict = " + str(self.FEA_dict) + linesep
        return OutMagElmer_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from OutInternal
        if not super(OutMagElmer, self).__eq__(other):
            return False
        if other.FEA_dict != self.FEA_dict:
            return False
        return True

    def as_dict(self):
        """Convert this object in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from OutInternal
        OutMagElmer_dict = super(OutMagElmer, self).as_dict()
        OutMagElmer_dict["FEA_dict"] = self.FEA_dict.copy() if self.FEA_dict is not None else None
        # The class name is added to the dict for deserialisation purpose
        # Overwrite the mother class name
        OutMagElmer_dict["__class__"] = "OutMagElmer"
        return OutMagElmer_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.FEA_dict = None
        # Set to None the properties inherited from OutInternal
        super(OutMagElmer, self)._set_None()

    def _get_FEA_dict(self):
        """getter of FEA_dict"""
        return self._FEA_dict

    def _set_FEA_dict(self, value):
        """setter of FEA_dict"""
        if type(value) is int and value == -1:
            value = dict()
        check_var("FEA_dict", value, "dict")
        self._FEA_dict = value

    FEA_dict = property(
        fget=_get_FEA_dict,
        fset=_set_FEA_dict,
        doc=u"""Dictionnary containing the main FEA parameters

        :Type: dict
        """,
    )
