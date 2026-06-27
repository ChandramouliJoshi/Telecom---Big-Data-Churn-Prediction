import { BrowserRouter, Routes, Route } from "react-router-dom";

import Dashboard from "@/pages/Dashboard";
import DataPipeline from "@/pages/DataPipeline";
import FeatureEngineering from "@/pages/FeatureEngineering";
import ChurnPrediction from "@/pages/ChurnPrediction";
import Analytics from "@/pages/Analytics";
import ModelPerformance from "@/pages/ModelPerformance";
import NotFound from "@/pages/NotFound";

function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/pipeline" element={<DataPipeline />} />
        <Route path="/features" element={<FeatureEngineering />} />
        <Route path="/prediction" element={<ChurnPrediction />} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="/performance" element={<ModelPerformance />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

export default AppRoutes;