import MainLayout from "@/layouts/MainLayout";

function ModelPerformance() {
  return (
    <MainLayout>
      <h1 className="text-4xl font-bold mb-8">
        Model Performance
      </h1>

      <div className="grid grid-cols-5 gap-6">
        <div className="bg-slate-900 rounded-2xl p-6">
          Accuracy
          <h2 className="text-3xl font-bold mt-3">
            84.6%
          </h2>
        </div>

        <div className="bg-slate-900 rounded-2xl p-6">
          Precision
          <h2 className="text-3xl font-bold mt-3">
            79.5%
          </h2>
        </div>

        <div className="bg-slate-900 rounded-2xl p-6">
          Recall
          <h2 className="text-3xl font-bold mt-3">
            80.5%
          </h2>
        </div>

        <div className="bg-slate-900 rounded-2xl p-6">
          F1 Score
          <h2 className="text-3xl font-bold mt-3">
            79.7%
          </h2>
        </div>

        <div className="bg-slate-900 rounded-2xl p-6">
          ROC-AUC
          <h2 className="text-3xl font-bold mt-3">
            84.6%
          </h2>
        </div>
      </div>
    </MainLayout>
  );
}

export default ModelPerformance;