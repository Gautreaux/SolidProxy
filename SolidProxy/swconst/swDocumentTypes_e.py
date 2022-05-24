from enum import IntEnum, unique

@unique
class swDocumentTypes_e(IntEnum):
    """Document types."""

    swDocASSEMBLY = 2
    swDocDRAWING = 3
    swDocIMPORTED_ASSEMBLY = 7
    swDocIMPORTED_PART = 6
    swDocLAYOUT = 5
    swDocNONE = 0
    swDocPART = 1
    swDocSDM = 4

    def what(self) -> str:
        return {
            2 : "swDocASSEMBLY",
            3 : "swDocDRAWING",
            7 : "Multi-CAD",
            6 : "Multi-CAD",
            5 : "swDocLAYOUT",
            0 : "swDocNONE",
            1 : "swDocPART",
            4 : "swDocSDM"
        }[self.value]

