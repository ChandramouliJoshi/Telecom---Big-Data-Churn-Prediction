import MainLayout from "@/layouts/MainLayout";

import StatCard from "@/components/dashboard/StatCard";
import ProgressCard from "@/components/dashboard/ProgressCard";
import PipelineCard from "@/components/dashboard/PipelineCard";
import InsightCard from "@/components/dashboard/InsightCard";
import ChurnChart from "@/components/analytics/ChurnChart";
import InternetServiceChart from "@/components/analytics/InternetServiceChart";

import {
  stats,
  progress,
  insights,
} from "@/data/dashboardData";

function Dashboard() {
  return (
    <MainLayout>
      <h1 className="text-4xl font-bold mb-8">
        Dashboard
      </h1>

      <div className="grid grid-cols-4 gap-6 mb-8">
        {stats.map((item) => (
          <StatCard
            key={item.title}
            {...item}
          />
        ))}
      </div>
      <div className="grid grid-cols-2 gap-6 mb-8">
        <ChurnChart />
        <InternetServiceChart />
      </div>

      <div className="mb-8">
        <PipelineCard />
      </div>

      <div className="space-y-4">
        {insights.map((insight) => (
          <InsightCard
            key={insight}
            insight={insight}
          />
        ))}
      </div>
    </MainLayout>
  );
}

export default Dashboard;