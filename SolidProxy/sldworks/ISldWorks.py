
import pythoncom
from typing import Optional
import win32com.client

from .IModelDoc2 import IModelDoc2
from ..swconst.swDocumentTypes_e import swDocumentTypes_e
from ..swconst.swOpenDocOptions_e import swOpenDocOptions_e

class ISldWorks:
    """Provides direct and indirect access to all other interfaces exposed in the SOLIDWORKS API."""

    def __init__(self, com_inst):
        self.com_inst = com_inst

    def CloseAllDocuments(self, IncludeUnsaved: bool) -> bool:
        """Closes all open documents in the SOLIDWORKS session.

        IncludeUnsaved
            True = Close all documents, including dirty documents
            False = Close all documents, excluding dirty documents
        
        Returns: True if method executes successfully, false if not
        """
        return self.com_inst.CloseAllDocuments(IncludeUnsaved)
    
    def GetDocuments(self) -> tuple[IModelDoc2]:
        "Gets the open documents in this SOLIDWORKS session."
        d = self.com_inst.GetDocuments
        if d is None:
            return tuple()
        else:
            return tuple(map(lambda x: IModelDoc2(x), d))

    def OpenDoc6(self, 
        FileName: str, 
        Type: swDocumentTypes_e, 
        Options: swOpenDocOptions_e, 
        Configuration: str
    ) -> tuple[Optional[IModelDoc2], tuple[int, int]]:
        """Opens an existing document and returns a pointer to the document object.
        
        NOTE: this call does not match the SW API reference

        returns tuple:
            Optional[ModelDoc2] - pointer to the file, if opened successfully
            tuple (Errors, Warnings)
        """
        e = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
        w = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)

        p = self.com_inst.OpenDoc6(FileName, Type.value, Options.value, Configuration, e, w)

        if p is None:
            return (None, (e.value, w.value))
        else:
            return (IModelDoc2(p), (e.value, w.value))
