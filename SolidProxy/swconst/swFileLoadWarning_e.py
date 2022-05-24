from enum import IntEnum, unique

@unique
class swFileLoadWarning_e(IntEnum):
    """File load warnings for"""

    swFileLoadWarning_AlreadyOpen = 128
    swFileLoadWarning_AutomaticRepair = 262144
    swFileLoadWarning_BasePartNotLoaded = 64
    swFileLoadWarning_ComponentMissingReferencedConfig = 32768
    swFileLoadWarning_CriticalDataRepair = 524288
    swFileLoadWarning_DimensionsReferencedIncorrectlyToModels = 16384
    swFileLoadWarning_DrawingANSIUpdate = 8
    swFileLoadWarning_DrawingSFSymbolConvert = 2048
    swFileLoadWarning_DrawingsOnlyRapidDraft = 256
    swFileLoadWarning_IdMismatch = 1
    swFileLoadWarning_InvisibleDoc_LinkedDesignTableUpdateFail = 65536
    swFileLoadWarning_MissingDesignTable = 131072
    swFileLoadWarning_MissingExternalReferences = 1048576
    swFileLoadWarning_ModelOutOfDate = 8192
    swFileLoadWarning_NeedsRegen = 32
    swFileLoadWarning_ReadOnly = 2
    swFileLoadWarning_RevolveDimTolerance = 4096
    swFileLoadWarning_SharingViolation = 4
    swFileLoadWarning_SheetScaleUpdate = 16
    swFileLoadWarning_ViewMissingReferencedConfig = 1024
    swFileLoadWarning_ViewOnlyRestrictions = 512

    def what(self) -> str:
        return {
            128 : "Warning appears because the document is already open.",
            262144 : "Warning appears that non-critical data in the document was automatically repaired.",
            64 : "Warning appears because the document was defined in the context of another existing document that is not loaded.",
            32768 : "Warning appears if document is opened silently and swOpenDocOptions_AutoMissingConfig is specified.",
            524288 : "Warning appears that critical data in the document was automatically repaired.",
            16384 : "Warning appears because some dimensions are referenced to the models incorrectly; these dimensions are highlighted in red in the drawing.",
            8 : "Warning appears because radial dimension arrows now displayed outside when the dimension text is outside of the arc or circle.",
            2048 : "Warning appears asking the user if he or she wants to convert this drawing's surface finish symbols to the sizes specified in ANSI Y14.36M-1996 and ISO 1302-1978.",
            256 : "Warning appears because the only RapidDraft format conversion that can take place is a drawing document that is not Detached.",
            1 : "Warning appears if the internal ID of the document does not match the internal ID saved with the referencing document.",
            65536 : "Warning issued because an attempt has been made to open an invisible document with a linked design table that was modified externally, and the design table cannot be updated because the document cannot be displayed;you must make the document visible to open it and update the design table.",
            131072 : "Warning appears because the design table is missing.",
            1048576 : "Warning appears if one or more references are missing when loading a file.",
            8192 : "Warning appears because some sheets contain drawing views that are out of date with their external models.",
            32 : "Warning appears because the document needs to be rebuilt.",
            2 : "Warning appears because the document is read only.",
            4096 : "Warning appears because some of the tolerances of the revolved feature dimensions were created in SOLIDWORKS 99 or earlier and are not synchronized with their corresponding dimensions in the sketch.",
            4 : "Warning appears if the document is being used by another user.",
            16 : "Warning appears because SOLIDWORKS now applies the scale of the sheet to the sketch entities on the sheet; which means that the sheet looks the same but dimension values arescaled.",
            1024 : "Warning appears because a configuration that a drawing view is referencing no longer exists in the model (part or assembly); the active configuration is used.",
            512 : "Warning appears because the document is view only and a configuration other than the default configuration is set."
        }[self.value]
