
import os
from services.mock_llm import llm_score_transcript_segment_mock
from services.llm_client import llm_score_transcript_segment_real

USE_LLM = os.getenv("USE_LLM", "false").lower() == "true"

def score_transcript_segments(segments):
    scored = []

    for seg in segments:
        if USE_LLM:
            scores = llm_score_transcript_segment_real(seg["text"])
        else:
            scores = llm_score_transcript_segment_mock(seg["text"])

        scored.append({
            **seg,
            "visual_relevance": scores["visual_relevance"],
            "speech_importance": scores["speech_importance"]
        })

    return scored
