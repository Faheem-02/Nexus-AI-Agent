from tools.browser_tool import BrowserTool
from tools.base_tool import BaseTool


class GoogleToolPlaceholder(BaseTool):
    def execute(self, action: dict) -> dict:
        return {
            "status": "success",
            "tool": "google",
            "action": action.get("action"),
            "result": "Google tool placeholder result",
        }


class Executor:
    def __init__(self):
        self.tool_map = {
            "browser": BrowserTool,
            "google": GoogleToolPlaceholder,
        }

    def execute(self, step: dict) -> dict:
        query = str(step.get("input", "")).lower()

        if "latest" in query or "find" in query:
            execution_mode = "browser"
        else:
            execution_mode = "default"

        print(f"[STRATEGY] Mode selected: {execution_mode}")

        if execution_mode == "default":
            return {
                "status": "success",
                "tool": "fast",
                "action": "direct",
                "result": f"[FAST MODE] Answer for: {step.get('input')}",
            }

        if execution_mode == "browser":
            tool_name = "browser"
        else:
            tool_name = step.get("tool")

        tool_class = self.tool_map.get(tool_name)

        print(f"[EXECUTOR] Using tool: {tool_name}")

        if tool_class is None:
            return {"status": "error", "message": f"Unsupported tool: {tool_name}"}

        action = {
            "tool": tool_name,
            "input": step.get("input"),
            "action": "search" if tool_name == "browser" else "execute",
        }

        tool = tool_class()
        return tool.execute(action)
