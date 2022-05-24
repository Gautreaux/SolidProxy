
from .IModelDocExtension import IModelDocExtension
from ..swconst.swDocumentTypes_e import swDocumentTypes_e

class IModelDoc2:
    """Allows access to SOLIDWORKS documents: parts, assemblies, and drawings."""

    def __init__(self, com_inst):
        self.com_inst = com_inst

    def Extension(self) -> IModelDocExtension:
        """Gets the IModelDocExtension object, which also allows access to the model document."""
        return IModelDocExtension(self.com_inst.Extension)

    def GetType(self) -> swDocumentTypes_e:
        "Gets the type of the document"
        return swDocumentTypes_e(self.com_inst.GetType)

    def GetTitle(self) -> str:
        "Gets the title of the document that appears in the active window's title bar."
        return self.com_inst.GetTitle

    def GetPathName(self) -> str:
        "Gets the full path name for this document, including the file name."
        return self.com_inst.GetPathName

    def SetReadOnlyState(self, b: bool) -> bool:
        """Sets whether this document is read-only or read-write.
        
        Returns True if method executes successfully, false if not
        """
        return self.com_inst.SetReadOnlyState(b)

    def IsOpenedReadOnly(self) -> bool:
        """Gets whether a SOLIDWORKS document is open in read-only mode.
        
        True if this document is read-only, false if not
        """

        return self.com_inst.IsOpenedReadOnly
