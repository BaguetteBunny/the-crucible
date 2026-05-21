from data.configs import Tool

class Tool():
    def __init__(self, type: Tool, location: tuple[int, int]) -> None:
        self.type = type
        self.value: int = type.value
        self.location = location