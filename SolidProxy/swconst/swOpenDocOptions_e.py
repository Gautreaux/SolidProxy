from enum import IntEnum, unique

@unique
class swOpenDocOptions_e(IntEnum):
    """How to open documents using ISldWorks::OpenDoc6. Bitmask."""

    swOpenDocOptions_AdvancedConfig = 8192
    swOpenDocOptions_AutoMissingConfig = 32
    swOpenDocOptions_DontLoadHiddenComponents = 256
    swOpenDocOptions_LDR_EditAssembly = 2048
    swOpenDocOptions_LoadExternalReferencesInMemory = 512
    swOpenDocOptions_LoadLightweight = 128
    swOpenDocOptions_LoadModel = 16
    swOpenDocOptions_OpenDetailingMode = 1024
    swOpenDocOptions_OverrideDefaultLoadLightweight = 64
    swOpenDocOptions_RapidDraft = 8
    swOpenDocOptions_ReadOnly = 2
    swOpenDocOptions_Silent = 1
    swOpenDocOptions_SpeedPak = 4096
    swOpenDocOptions_ViewOnly = 4

    swOpenDocOptions_NotSet = 0

    def what(self) -> str:
        return {
            8192 : "Open assemblyusing anadvanced configuration",
            32 : "Obsolete; do not use</p>",
            256 : "By default, hidden components are loaded when you open an assembly document. Set swOpenDocOptions_DontLoadHiddenComponents to not load hidden components when opening an assembly document",
            2048 : "Open in Large Design Review mode with edit assembly enabled",
            512 : "Open external references in memory only; this setting is valid only if swUserPreferenceIntegerValue_e.swLoadExternalReferences is not set to swLoadExternalReferences_e.swLoadExternalReferences_None",
            128 : "Open assembly document as lightweight",
            16 : "Load Detached model upon opening document (drawings only)",
            1024 : "Open document in detailing mode",
            64 : "Override default setting whether to open an assembly document as lightweight",
            8 : "Convert document to Detached format (drawings only)",
            2 : "Open document read only",
            1 : "Open document silently",
            4096 : "Open document using the SpeedPak option",
            4 : "Open document in Large Design Review mode only (assemblies only)",
            0 : "No bit flag was set"
        }[self.value]
