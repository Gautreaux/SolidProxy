from enum import IntEnum, unique

@unique
class swSurfaceTypes_e(IntEnum):
    """Surface types."""

    BLEND_TYPE = 4007
    BSURF_TYPE = 4006
    CONE_TYPE = 4003
    CYLINDER_TYPE = 4002
    EXTRU_TYPE = 4009
    OFFSET_TYPE = 4008
    PLANE_TYPE = 4001
    SPHERE_TYPE = 4004
    SREV_TYPE = 4010
    TORUS_TYPE = 4005

    def what(self) -> str:
        return {
            4007 : "BLEND_TYPE",
            4006 : "BSURF_TYPE",
            4003 : "CONE_TYPE",
            4002 : "CYLINDER_TYPE",
            4009 : "EXTRU_TYPE",
            4008 : "OFFSET_TYPE",
            4001 : "PLANE_TYPE",
            4004 : "SPHERE_TYPE",
            4010 : "SREV_TYPE",
            4005 : "TORUS_TYPE"
        }[self.value]
