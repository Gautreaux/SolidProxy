
import pythoncom
import win32com.client

class IFeature:
    """Allows access to the feature type, name, parameter data, and the next feature in the FeatureManager design tree."""

    def __init__(self, com_inst):
        self.com_inst = com_inst

    def GetErrorCode2(self) -> tuple[int, bool]:
        """Gets the error code for this feature.
        
        NOTE: this call does not match the SW API reference

        returns tuple:
            int - the error code as specified in swFeatureError_e
            bool - true iff the error code indicates a warning
                undefined when the error code is 0 (no error)
        """    
        # TODO - integrate swFeatureError_e
        b = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_BOOL, False)

        i = self.com_inst.GetErrorCode2(b)

        return (i, b.value)