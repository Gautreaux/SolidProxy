from enum import IntEnum, unique

@unique
class swFileLoadError_e(IntEnum):
    """File load errors. Bitmask."""

    swAddinInteruptError = 1048576
    swApplicationBusy = 8388608
    swFileCriticalDataRepairError = 4194304
    swFileNotFoundError = 2
    swFileRequiresRepairError = 2097152
    swFileWithSameTitleAlreadyOpen = 65536
    swFutureVersion = 8192
    swGenericError = 1
    swInvalidFileTypeError = 1024
    swLiquidMachineDoc = 131072
    swLowResourcesError = 262144
    swNoDisplayData = 524288

    def what(self) -> str:
        return {
            1048576 : "The user attempted to open a file, and then interrupted the open-file routine toopen a different file",
            8388608 : "swApplicationBusy",
            4194304 : "A document has critical data corruption",
            2 : "Unable to locate the file; the file is not loaded or the referenced file (that is, component) is suppressed",
            2097152 : "A document has non-critical custom property data corruption",
            65536 : "A document with the same name is already open",
            8192 : "The document was saved in a future version of SOLIDWORKS",
            1 : "Another error was encountered",
            1024 : "File type argument is not valid",
            131072 : "File encrypted by Liquid Machines",
            262144 : "File is open and blocked because the system memory is low, or the number of GDI handles has exceeded the allowed maximum",
            524288 : "File contains no display data"
        }[self.value]
