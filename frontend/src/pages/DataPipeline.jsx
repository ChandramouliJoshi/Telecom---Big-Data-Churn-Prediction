import MainLayout from "@/layouts/MainLayout";

function DataPipeline() {
  return (
    <MainLayout>
      <h1 className="text-4xl font-bold mb-8">
        Data Pipeline
      </h1>

      <div className="grid grid-cols-2 gap-6">
        <div className="bg-slate-900 rounded-2xl p-6">
          <h2 className="text-xl font-semibold mb-4">
            Dataset Information
          </h2>

          <p>Total Rows : 7043</p>
          <p>Total Columns : 33</p>
        </div>

        <div className="bg-slate-900 rounded-2xl p-6">
          <h2 className="text-xl font-semibold mb-4">
            Validation Status
          </h2>

          <p>✓ Missing Values Checked</p>
          <p>✓ Duplicate Records Checked</p>
          <p>✓ Dataset Ready for Modeling</p>
        </div>
      </div>
    </MainLayout>
  );
}

export default DataPipeline;