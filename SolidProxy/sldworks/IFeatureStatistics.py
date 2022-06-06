
from .IFeature import IFeature

class IFeatureStatistics:
    """Allows access to the feature statistics in a part document."""

    def __init__(self, com_inst):
        self.com_inst = com_inst

    def Features(self) -> tuple[IFeature]:
        """Gets the features in a part document."""
        return tuple(map(lambda x: IFeature(x), self.com_inst.Features))
