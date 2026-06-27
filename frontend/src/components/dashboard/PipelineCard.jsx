function PipelineCard() {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">
      <h2 className="text-xl font-semibold mb-4">
        Pipeline Status
      </h2>

      <p className="text-slate-400">
        Data Processing → Feature Engineering → Modeling → Deployment
      </p>
    </div>
  );
}

export default PipelineCard;