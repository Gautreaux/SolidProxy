
from .IFeatureStatistics import IFeatureStatistics

class IFeatureManager:
    """Allows you to create features."""

    def __init__(self, com_inst):
        self.com_inst = com_inst

    def FeatureStatistics(self) -> IFeatureStatistics:
        """Gets statistics about the features in a part document."""
        return IFeatureStatistics(self.com_inst.FeatureStatistics)
