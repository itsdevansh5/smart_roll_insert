# Smart B-Roll Inserter for UGC Videos

## Overview

This project implements a **Smart B-Roll Insertion Planner** for short UGC (User Generated Content) talking-head videos.

Given:
- One **A-roll video** (speaker talking to camera)
- Multiple **B-roll clips** (contextual visuals)

The system automatically:
- Understands **what is being said and when**
- Understands **what each B-roll clip represents**
- Decides **where B-roll should be inserted**
- Outputs a **structured timeline plan in JSON format**

The focus of this assignment is **system design, reasoning, and timeline planning**, not UI polish or video editing effects.

---

## Key Features

- Timestamped A-roll transcript (mocked for reliability)
- Semantic scoring to identify visually valuable moments
- Intelligent B-roll matching with constraints
- Structured JSON timeline output
- Simple React frontend to trigger plan generation
- Clean, modular backend architecture
- LLM-ready design with documented trade-offs

---

## Architecture Overview

```
A-Roll Video
   ↓
(Mocked Transcript with Timestamps)
   ↓
Semantic Scoring (LLM-replaceable logic)
   ↓
B-Roll Metadata Understanding
   ↓
Matching Logic + Constraints
   ↓
Timeline Plan (JSON Output)
```

---

## Backend Structure

```
backend/
├── app.py
├── requirements.txt
├── services/
│   ├── transcription.py
│   ├── semantic_scoring.py
│   ├── mock_llm.py
│   ├── llm_client.py
│   ├── broll_analysis.py
│   ├── matcher.py
│   └── planner.py
└── output/
    └── timeline_plan.json
```

---

## Frontend Structure

```
frontend/
├── package.json
├── src/
│   ├── App.jsx
│   ├── api.js
│   └── components/
│       ├── UploadSection.jsx
│       ├── TranscriptView.jsx
│       └── TimelineView.jsx
```

---

## API Endpoint

### POST /generate-plan

Example response:

```json
{
  "aroll_duration_sec": 65,
  "insertions": [
    {
      "start_sec": 9.1,
      "duration_sec": 2.5,
      "broll_id": "broll_3",
      "confidence": 0.8,
      "reason": "B-roll matches spoken context"
    }
  ]
}
```

---

## LLM Usage Note

The system is designed to integrate with LLM APIs (OpenAI / Gemini).
Due to exhausted API quota during development, LLM execution is mocked
using deterministic logic. Real LLM logic is implemented and can be
enabled via configuration without changing core code.

---

## How to Run

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Trade-Offs

- Mock transcription for reliability
- Mock LLM execution to avoid quota issues
- Focus on reasoning and system design
- Minimal UI for clarity

---

## Conclusion

This project focuses on correctness, explainability, and clean system
design, aligned with the intent of the assignment.
