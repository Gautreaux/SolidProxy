

from collections import Counter
from SolidProxy.bootstrap import GetOrStartSWInst
from SolidProxy.sldworks.IPartDoc import IPartDoc
from SolidProxy.swconst.swBodyType_e import swBodyType_e
from SolidProxy.swconst.swSurfaceTypes_e import swSurfaceTypes_e
from ex_utils import loadTestFile

def CountFaces(part: IPartDoc) -> Counter:
    """Count the number and types of faces in the part"""

    c = Counter()

    print(type(part))

    for body in part.GetBodies2(swBodyType_e.swAllBodies, True):
        for face in body.GetFaces():
            surface = face.GetSurface()
            surface_type = surface.Identity()

            c.update([surface_type, ])

    return c


if __name__ == "__main__":
    sw_inst = GetOrStartSWInst()
    assert(sw_inst is not None)
    sw_inst.CloseAllDocuments(True)

    f = loadTestFile("TestFiles/cube.sldprt")
    c = CountFaces(f)

    assert(c == Counter([swSurfaceTypes_e.PLANE_TYPE]*6))
    
    f = loadTestFile("TestFiles/cylinder.sldprt")
    c = CountFaces(f)

    assert(c == Counter([
        swSurfaceTypes_e.PLANE_TYPE,
        swSurfaceTypes_e.PLANE_TYPE,
        swSurfaceTypes_e.CYLINDER_TYPE,
    ]))

    f = loadTestFile("TestFiles/sphere.sldprt")
    c = CountFaces(f)

    assert(c == Counter([swSurfaceTypes_e.SPHERE_TYPE]))

    f = loadTestFile("TestFiles/ellipsoid.sldprt")
    c = CountFaces(f)

    # not sure what an SREV is exactly, but apparently this is one
    assert(c == Counter([swSurfaceTypes_e.SREV_TYPE]))

    print(f"All face counts matched expected")

