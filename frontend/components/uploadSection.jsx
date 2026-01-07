
import { useState } from "react";
import { generatePlan } from "./api";
import UploadSection from "./components/UploadSection";
import TranscriptView from "./components/TranscriptView";
import TimelineView from "./components/TimelineView";

export default function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    setLoading(true);
    const data = await generatePlan();
    setResult(data);
    setLoading(false);
  };

  return (
    <div style={{ padding: 24 }}>
      <h1>Smart B-Roll Inserter</h1>

      <UploadSection onGenerate={handleGenerate} loading={loading} />

      {result && (
        <>
          <TranscriptView insertions={result.insertions} />
          <TimelineView result={result} />
        </>
      )}
    </div>
  );
}
