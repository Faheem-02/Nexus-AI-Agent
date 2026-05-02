class BaseTool:
    def execute(self, action: dict) -> dict:
        raise NotImplementedError
