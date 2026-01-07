
export default function TranscriptView({ insertions }) {
  return (
    <div style={{ marginBottom: 24 }}>
      <h3>Transcript & Insertions</h3>

      <ul>
        {insertions.map((item, idx) => (
          <li key={idx}>
            <strong>{item.start_sec}s → {item.start_sec + item.duration_sec}s</strong>
            <br />
            B-Roll: {item.broll_id}
            <br />
            Reason: {item.reason}
          </li>
        ))}
      </ul>
    </div>
  );
}
