
def generate_timeline_plan(aroll_duration: float, matches: list):
    return {
        "aroll_duration_sec": aroll_duration,
        "insertions": matches
    }
