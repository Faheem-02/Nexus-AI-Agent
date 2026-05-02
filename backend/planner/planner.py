import json

from openai import OpenAI
from openai import AuthenticationError, RateLimitError

from config.settings import OPENAI_API_KEY
from schemas.plan_schema import Plan


class Planner:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def create_plan(self, user_goal: str) -> Plan:
        mock_plan = {
            "steps": [
                {
                    "id": "1",
                    "task": "Search for information",
                    "tool": "browser",
                    "input": user_goal,
                }
            ]
        }

        if not OPENAI_API_KEY:
            return Plan.model_validate(mock_plan)

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": "Return only valid JSON."},
                    {
                        "role": "user",
                        "content": (
                            "Create a plan for this goal. "
                            "Return JSON in this exact shape: "
                            '{"steps":[{"id":"string","task":"string","tool":"string","input":"any"}]}. '
                            f"Goal: {user_goal}"
                        ),
                    },
                ],
            )

            content = response.choices[0].message.content or '{"steps":[]}'
            return Plan.model_validate(json.loads(content))
        except AuthenticationError:
            return Plan.model_validate(mock_plan)
        except RateLimitError as exc:
            # Use mock only when quota/credits are exhausted.
            if "insufficient_quota" in str(exc).lower():
                return Plan.model_validate(mock_plan)
            raise
        except Exception:
            # Non-auth/quota failures should not silently mask API issues.
            raise
