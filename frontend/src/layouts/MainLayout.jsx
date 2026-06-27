import Sidebar from "@/components/layout/Sidebar";
import TopNavbar from "@/components/layout/TopNavbar";

function MainLayout({ children }) {
  return (
    <div className="min-h-screen bg-[#0B1120] text-white flex">
      <Sidebar />

      <div className="flex-1">
        <TopNavbar />

        <main className="p-8">
          {children}
        </main>
      </div>
    </div>
  );
}

export default MainLayout;