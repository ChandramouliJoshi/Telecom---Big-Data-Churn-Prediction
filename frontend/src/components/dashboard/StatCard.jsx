function StatCard({ title, value, change }) {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">
      <p className="text-slate-400 text-sm">
        {title}
      </p>

      <h2 className="text-3xl font-bold mt-3">
        {value}
      </h2>

      <p className="text-emerald-400 text-sm mt-3">
        {change}
      </p>
    </div>
  );
}

export default StatCard;