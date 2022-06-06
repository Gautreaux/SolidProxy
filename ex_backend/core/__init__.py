import sys
import os


_path_comps = os.path.normpath(os.path.dirname(__file__)).split(os.path.sep)

while _path_comps:
    if _path_comps[-1] == 'SolidProxy':
        break
    else:
        _path_comps.pop()

if not _path_comps:
    raise ImportError("Could not locate the solid proxy module")

_d = os.path.sep.join(_path_comps)

if "SolidProxy" in os.listdir(_d):
    sys.path.append(_d)
else:
    raise ImportError(f"Located SolidProxy at `{_d}` but did not find submodule")
