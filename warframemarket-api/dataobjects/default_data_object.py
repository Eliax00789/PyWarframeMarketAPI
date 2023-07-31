class DefaultDataObject:
    def get_as_dict(self) -> dict:
        return vars(self)
