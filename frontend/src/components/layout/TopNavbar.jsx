import { Bell, Search } from "lucide-react";

function TopNavbar() {
  return (
    <header className="h-20 border-b border-slate-800 flex items-center justify-between px-8">
      <div className="flex items-center gap-3 bg-slate-900 rounded-xl px-4 py-2">
        <Search size={18} />
        <input
          placeholder="Search..."
          className="bg-transparent outline-none"
        />
      </div>

      <button className="bg-slate-900 p-3 rounded-xl">
        <Bell size={18} />
      </button>
    </header>
  );
}

export default TopNavbar;