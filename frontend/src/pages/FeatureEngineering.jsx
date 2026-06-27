import MainLayout from "@/layouts/MainLayout";

function FeatureEngineering() {
  return (
    <MainLayout>
      <h1 className="text-4xl font-bold mb-8">
        Feature Engineering
      </h1>

      <div className="space-y-6">
        <div className="bg-slate-900 rounded-2xl p-6">
          Spark SQL Aggregations
        </div>

        <div className="bg-slate-900 rounded-2xl p-6">
          VectorAssembler Pipeline
        </div>

        <div className="bg-slate-900 rounded-2xl p-6">
          DAG Visualization
        </div>
      </div>
    </MainLayout>
  );
}

export default FeatureEngineering;