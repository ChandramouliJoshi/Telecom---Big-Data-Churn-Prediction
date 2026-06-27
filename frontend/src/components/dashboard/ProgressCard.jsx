function ProgressCard({ title, value }) {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">
      <div className="flex justify-between mb-4">
        <span>{title}</span>
        <span>{value}%</span>
      </div>

      <div className="w-full bg-slate-700 rounded-full h-3">
        <div
          className="bg-blue-500 h-3 rounded-full"
          style={{
            width: `${value}%`,
          }}
        />
      </div>
    </div>
  );
}

export default ProgressCard;