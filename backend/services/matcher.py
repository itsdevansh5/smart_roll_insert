
def match_brolls(segments, brolls):
    matches = []
    used_brolls = set()

    for seg in segments:
        if seg["visual_relevance"] < 0.6:
            continue
        if seg["speech_importance"] > 0.7:
            continue

        for b in brolls:
            if b["broll_id"] in used_brolls:
                continue

            if any(word in seg["text"].lower() for word in b["description"].lower().split()):
                matches.append({
                    "start_sec": seg["start"],
                    "duration_sec": min(b["duration_sec"], seg["end"] - seg["start"]),
                    "broll_id": b["broll_id"],
                    "confidence": round(seg["visual_relevance"], 2),
                    "reason": f"B-roll matches spoken context: {b['description']}"
                })
                used_brolls.add(b["broll_id"])
                break

        if len(matches) >= 5:
            break

    return matches
