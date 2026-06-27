function InsightCard({ insight }) {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-4">
      <p className="text-slate-300">
        {insight}
      </p>
    </div>
  );
}

export default InsightCard;