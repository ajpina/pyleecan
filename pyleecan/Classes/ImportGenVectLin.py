# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Import/ImportGenVectLin.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .ImportMatrix import ImportMatrix

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Import.ImportGenVectLin.check import check
except ImportError as error:
    check = error

try:
    from ..Methods.Import.ImportGenVectLin.comp_step import comp_step
except ImportError as error:
    comp_step = error

try:
    from ..Methods.Import.ImportGenVectLin.get_data import get_data
except ImportError as error:
    get_data = error


from ._check import InitUnKnowClassError


class ImportGenVectLin(ImportMatrix):
    """To generate a Linspace vector"""

    VERSION = 1

    # Check ImportError to remove unnecessary dependencies in unused method
    # cf Methods.Import.ImportGenVectLin.check
    if isinstance(check, ImportError):
        check = property(
            fget=lambda x: raise_(
                ImportError("Can't use ImportGenVectLin method check: " + str(check))
            )
        )
    else:
        check = check
    # cf Methods.Import.ImportGenVectLin.comp_step
    if isinstance(comp_step, ImportError):
        comp_step = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ImportGenVectLin method comp_step: " + str(comp_step)
                )
            )
        )
    else:
        comp_step = comp_step
    # cf Methods.Import.ImportGenVectLin.get_data
    if isinstance(get_data, ImportError):
        get_data = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use ImportGenVectLin method get_data: " + str(get_data)
                )
            )
        )
    else:
        get_data = get_data
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
        start=0,
        stop=1,
        num=100,
        endpoint=True,
        is_transpose=False,
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
            start = obj.start
            stop = obj.stop
            num = obj.num
            endpoint = obj.endpoint
            is_transpose = obj.is_transpose
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "start" in list(init_dict.keys()):
                start = init_dict["start"]
            if "stop" in list(init_dict.keys()):
                stop = init_dict["stop"]
            if "num" in list(init_dict.keys()):
                num = init_dict["num"]
            if "endpoint" in list(init_dict.keys()):
                endpoint = init_dict["endpoint"]
            if "is_transpose" in list(init_dict.keys()):
                is_transpose = init_dict["is_transpose"]
        # Initialisation by argument
        self.start = start
        self.stop = stop
        self.num = num
        self.endpoint = endpoint
        # Call ImportMatrix init
        super(ImportGenVectLin, self).__init__(is_transpose=is_transpose)
        # The class is frozen (in ImportMatrix init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        ImportGenVectLin_str = ""
        # Get the properties inherited from ImportMatrix
        ImportGenVectLin_str += super(ImportGenVectLin, self).__str__()
        ImportGenVectLin_str += "start = " + str(self.start) + linesep
        ImportGenVectLin_str += "stop = " + str(self.stop) + linesep
        ImportGenVectLin_str += "num = " + str(self.num) + linesep
        ImportGenVectLin_str += "endpoint = " + str(self.endpoint) + linesep
        return ImportGenVectLin_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from ImportMatrix
        if not super(ImportGenVectLin, self).__eq__(other):
            return False
        if other.start != self.start:
            return False
        if other.stop != self.stop:
            return False
        if other.num != self.num:
            return False
        if other.endpoint != self.endpoint:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from ImportMatrix
        ImportGenVectLin_dict = super(ImportGenVectLin, self).as_dict()
        ImportGenVectLin_dict["start"] = self.start
        ImportGenVectLin_dict["stop"] = self.stop
        ImportGenVectLin_dict["num"] = self.num
        ImportGenVectLin_dict["endpoint"] = self.endpoint
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        ImportGenVectLin_dict["__class__"] = "ImportGenVectLin"
        return ImportGenVectLin_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        self.start = None
        self.stop = None
        self.num = None
        self.endpoint = None
        # Set to None the properties inherited from ImportMatrix
        super(ImportGenVectLin, self)._set_None()

    def _get_start(self):
        """getter of start"""
        return self._start

    def _set_start(self, value):
        """setter of start"""
        check_var("start", value, "float")
        self._start = value

    # Begin point of the linspace
    # Type : float
    start = property(
        fget=_get_start, fset=_set_start, doc=u"""Begin point of the linspace"""
    )

    def _get_stop(self):
        """getter of stop"""
        return self._stop

    def _set_stop(self, value):
        """setter of stop"""
        check_var("stop", value, "float")
        self._stop = value

    # End point of the linspace
    # Type : float
    stop = property(
        fget=_get_stop, fset=_set_stop, doc=u"""End point of the linspace"""
    )

    def _get_num(self):
        """getter of num"""
        return self._num

    def _set_num(self, value):
        """setter of num"""
        check_var("num", value, "float")
        self._num = value

    # Number of value in the linspace
    # Type : float
    num = property(
        fget=_get_num, fset=_set_num, doc=u"""Number of value in the linspace"""
    )

    def _get_endpoint(self):
        """getter of endpoint"""
        return self._endpoint

    def _set_endpoint(self, value):
        """setter of endpoint"""
        check_var("endpoint", value, "bool")
        self._endpoint = value

    # If True, stop is the last sample. Otherwise, it is not included
    # Type : bool
    endpoint = property(
        fget=_get_endpoint,
        fset=_set_endpoint,
        doc=u"""If True, stop is the last sample. Otherwise, it is not included""",
    )
