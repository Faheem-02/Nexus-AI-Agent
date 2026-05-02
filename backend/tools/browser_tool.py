from .base_tool import BaseTool
from .browser_adapter import BrowserAdapter


class BrowserTool(BaseTool):
    def execute(self, action: dict) -> dict:
        action_type = action.get("action")
        query = action.get("input")

        if action_type == "search":
            try:
                adapter = BrowserAdapter()
                result = adapter.search(query)
                return {
                    "status": "success",
                    "tool": "browser",
                    "action": "search",
                    "result": result,
                }
            except Exception:
                return {
                    "status": "success",
                    "tool": "browser",
                    "action": "search",
                    "result": f"Mock browser search result for query: {query}",
                }

        return {"status": "error", "message": f"Unsupported action: {action_type}"}
