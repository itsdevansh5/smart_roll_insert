
"""
REAL LLM implementation.
Not executed by default due to quota exhaustion.
"""

def llm_score_transcript_segment_real(text: str) -> dict:
    """
    Example OpenAI / Gemini logic (pseudo-real).
    This function is NOT called unless USE_LLM=true.
    """

    # Example prompt (documented)
    prompt = f"""
    Given a sentence from a talking-head video,
    return JSON:
    {{
      "visual_relevance": 0-1,
      "speech_importance": 0-1
    }}

    Sentence: "{text}"
    """

    # PSEUDO CODE (documented, not executed)
    """
    response = client.generate(prompt)
    return json.loads(response)
    """

    raise RuntimeError("LLM quota exhausted – real LLM disabled")
