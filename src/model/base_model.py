class BaseModel:
    def to_dict(self) -> dict:
        raise NotImplementedError("Subclasses must implement the to_dict method")
    
    @classmethod
    def from_dict(cls, data) -> any:
        raise NotImplementedError("Subclasses must implement the from_dict method")