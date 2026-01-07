
from fastapi import FastAPI
from services.transcription import transcribe_aroll
from services.semantic_scoring import score_transcript_segments
from services.broll_analysis import analyze_brolls
from services.matcher import match_brolls
from services.planner import generate_timeline_plan

app = FastAPI(title="Smart B-Roll Inserter")

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/generate-plan")
def generate_plan():
    # Step 1: Transcription (mocked)
    transcript = transcribe_aroll("assets/a_roll.mp4")

    # Step 2: Semantic scoring
    scored_segments = score_transcript_segments(transcript)

    # Step 3: B-roll understanding
    brolls = analyze_brolls()

    # Step 4: Matching
    matches = match_brolls(scored_segments, brolls)

    # Step 5: Timeline plan
    timeline = generate_timeline_plan(
        aroll_duration=65.0,
        matches=matches
    )

    return timeline
