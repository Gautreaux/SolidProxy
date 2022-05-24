
from .ISurface import ISurface

class IFace2:
    """Allows access to the underlying edge, loop, and surface to the owning body or feature, and to face tessellation, trim data."""

    def __init__(self, com_inst):
        self.com_inst = com_inst

    def GetArea(self) -> float:
        """Gets the area of this face.
        
        Face area in square meters
        """
        return self.com_inst.GetArea

    def GetSurface(self) -> ISurface:
        """Gets the surface referenced by this face."""
        return ISurface(self.com_inst.GetSurface)
