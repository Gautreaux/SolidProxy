
from .IFace2 import IFace2
from ..swconst.swBodyType_e import swBodyType_e

class IBody2:
    """Allows access to the faces on a body and the ability to create surfaces for sewing into a body object."""

    def __init__(self, com_inst):
        self.com_inst = com_inst

    def GetFaceCount(self) -> int:
        """Gets the number of faces in this body."""
        return self.com_inst.GetFaceCount()

    def GetFaces(self) -> tuple[IFace2]:
        """Gets all of the faces on the body."""
        return tuple(map(lambda x: IFace2(x), self.com_inst.GetFaces()))
    
    def GetType(self) -> swBodyType_e:
        """Gets the type of the body."""
        return swBodyType_e(self.com_inst.GetType())
