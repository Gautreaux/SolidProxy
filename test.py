

from SolidProxy.bootstrap import GetOrStartSWInst


sw_inst = GetOrStartSWInst()

if not sw_inst:
    print(f"No SolidWorks instance was found (and failed to start one)")
else:
    print(f"SolidWorks connected")
    print(f"Total open documents: {len(sw_inst.GetDocuments())}")
