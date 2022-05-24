
from .IBody2 import IBody2
from .IModelDoc2 import IModelDoc2
from ..swconst.swBodyType_e import swBodyType_e

class IPartDoc(IModelDoc2):
    """Provides access to functions that perform operations on parts in part documents."""

    def __init__(self, com_inst) -> None:
        super().__init__(com_inst)

    def GetBodies2(self, BodyType: swBodyType_e, BVisibleOnly: bool) -> tuple[IBody2]:
        """Gets the bodies in this part.
        
        BodyType
        Type of body as defined in swBodyType_e

        BVisibleOnly
        True gets only the visible bodies, false gets all of the bodies in the part
         """
        a = self.com_inst.GetBodies2(BodyType.value, BVisibleOnly)
        if a is None:
            return tuple()
        return tuple(map(lambda x: IBody2(x), a))
