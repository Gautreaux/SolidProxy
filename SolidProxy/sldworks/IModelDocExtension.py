
class IModelDocExtension:
    """Allows access to the model."""
    # Technically Extends IModelDoc but that would create a circular import

    def __init__(self, com_object) -> None:
        self.com_object = com_object
