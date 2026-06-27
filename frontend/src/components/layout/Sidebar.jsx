import {
  LayoutDashboard,
  Database,
  Cpu,
  BarChart3,
} from "lucide-react";
import { NavLink } from "react-router-dom";

const menuItems = [
  {
    title: "Dashboard",
    icon: LayoutDashboard,
    path: "/",
  },
  {
    title: "Data Pipeline",
    icon: Database,
    path: "/pipeline",
  },
  {
    title: "Feature Engineering",
    icon: Cpu,
    path: "/features",
  },
  {
    title: "Model Performance",
    icon: BarChart3,
    path: "/performance",
  },
];

function Sidebar() {
  return (
    <aside className="w-72 bg-slate-950 border-r border-slate-800 p-6">
      <h1 className="text-2xl font-bold mb-10">
        SparkScale
      </h1>

      <nav className="space-y-3">
        {menuItems.map((item) => (
          <NavLink
            key={item.title}
            to={item.path}
            className={({ isActive }) =>
              `flex items-center gap-3 p-4 rounded-xl transition ${
                isActive
                  ? "bg-blue-600 text-white"
                  : "text-slate-400 hover:bg-slate-900"
              }`
            }
          >
            <item.icon size={20} />
            {item.title}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}

export default Sidebar;