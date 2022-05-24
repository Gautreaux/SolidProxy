from enum import IntEnum, unique

@unique
class swBodyType_e(IntEnum):
    """Valid body types."""

    swAllBodies = -1
    swEmptyBody = 5
    swGeneralBody = 4
    swMinimumBody = 3
    swSheetBody = 1
    swSolidBody = 0
    swWireBody = 2

    def what(self) -> str:
        return {
            -1 : "All solid and sheet bodies",
            5 : "NULL body",
            4 : "General, nonmanifold body",
            3 : "Point body",
            1 : "Sheet body",
            0 : "Solid body",
            2 : "Wire body"
        }[self.value]
