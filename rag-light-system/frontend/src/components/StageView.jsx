const stages = [
  "Ingestion (Observation)",
  "Chunking (Diffraction)",
  "Embedding (Refraction)",
  "Retrieval (Reflection)",
  "Reasoning (Interpretation)",
  "Evaluation (Noise)"
];

export default function StageView() {
  return (
    <div className="grid grid-cols-3 gap-4">
      {stages.map(stage => (
        <div
          key={stage}
          className="p-4 border rounded-xl shadow-sm text-center"
        >
          {stage}
        </div>
      ))}
    </div>
  );
}
