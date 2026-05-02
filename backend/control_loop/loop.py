from config.settings import MAX_STEPS, RETRY_LIMIT


def run_loop(plan, executor):
    steps = plan.get("steps", []) if isinstance(plan, dict) else getattr(plan, "steps", [])
    results = []

    if len(steps) > MAX_STEPS:
        print(f"[AGENT] Step 0: Plan has more than MAX_STEPS ({MAX_STEPS}). Truncating.")

    for index, step in enumerate(steps[:MAX_STEPS], start=1):
        step_id = step.get("id") if isinstance(step, dict) else getattr(step, "id", index)
        print(f"[AGENT] Step {index}: Starting (id={step_id})")

        step_result = None
        for attempt in range(1, RETRY_LIMIT + 1):
            try:
                # Retry placeholder: rerun the same step when execution raises an exception.
                if hasattr(executor, "execute"):
                    step_result = executor.execute(step)
                else:
                    step_result = executor(step)
                break
            except Exception as exc:
                print(f"[AGENT] Step {index}: Error on attempt {attempt}/{RETRY_LIMIT}: {exc}")
                if attempt == RETRY_LIMIT:
                    step_result = {"status": "error", "step_id": step_id, "message": str(exc)}

        print(f"[RESULT] Step {index}: {step_result}")
        results.append(step_result)

    print(f"[RESULT] Completed {len(results)} step(s).")
    return results