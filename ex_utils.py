
import os

from SolidProxy.bootstrap import GetOrStartSWInst
from SolidProxy.sldworks.IPartDoc import IPartDoc
from SolidProxy.swconst.swDocumentTypes_e import swDocumentTypes_e
from SolidProxy.swconst.swFileLoadWarning_e import swFileLoadWarning_e
from SolidProxy.swconst.swOpenDocOptions_e import swOpenDocOptions_e

def loadTestFile(
    filepath: str,
    read_only:bool=True,
    configuration:str="",
) -> IPartDoc:

    filepath = os.path.abspath(filepath)
    print("Full Filepath:", filepath)

    if filepath.lower().endswith(".sldprt"):
        part_type = swDocumentTypes_e.swDocPART
    else:
        raise RuntimeError("Only part files are currently supported")

    sw_inst = GetOrStartSWInst()
    assert(sw_inst is not None)
    
    (doc_pointer, (errors, warnings)) = sw_inst.OpenDoc6(
        filepath,
        part_type,
        swOpenDocOptions_e.swOpenDocOptions_ReadOnly if read_only else swOpenDocOptions_e.swOpenDocOptions_NotSet,
        configuration,
    )

    if read_only:
        # need to negate the read only bit:
        warnings &= ~(swFileLoadWarning_e.swFileLoadWarning_ReadOnly.value)
    
    if warnings:
        print(f"[WARNING] `{warnings}` while opening `{filepath}`")
    
    if errors:
        msg = f"Error `{errors}` while opening `{filepath}`"
        raise RuntimeError(msg)

    if doc_pointer is None:
        # this is unreachable i think; any such condition would be caught in errors?
        raise RuntimeError("Opening file did not return a pointer to the object")

    return IPartDoc(doc_pointer.com_inst)
