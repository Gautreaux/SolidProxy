
from ..swconst.swSurfaceTypes_e import swSurfaceTypes_e

class ISurface:
    """Used as the underlying definition of a face."""
    
    def __init__(self, com_inst):
        self.com_inst = com_inst
    
    def Identity(self) -> swSurfaceTypes_e:
        """Gets the type of surface."""
        return swSurfaceTypes_e(self.com_inst.Identity)
