
def llm_score_transcript_segment_mock(text: str) -> dict:
    text = text.lower()

    visual_relevance = 0.8 if any(
        k in text for k in ["food", "hygiene", "open", "clean", "dikhta"]
    ) else 0.4

    speech_importance = 0.75 if any(
        k in text for k in ["zaroori", "health", "important"]
    ) else 0.4

    return {
        "visual_relevance": round(visual_relevance, 2),
        "speech_importance": round(speech_importance, 2)
    }
