from typing import Optional
import win32com.client as ComClient

from .sldworks.ISldWorks import ISldWorks

SW_INST_TARGET_NAME = "SldWorks.Application"

def GetOrStartSWInst() -> Optional[ISldWorks]:
    """Get the running SolidWorks instance, if one is running
        otherwise create a new headless instance of SolidWorks
    """
    sw_inst = ComClient.Dispatch(SW_INST_TARGET_NAME)

    if sw_inst:
        return ISldWorks(sw_inst)
    else:
        return None
