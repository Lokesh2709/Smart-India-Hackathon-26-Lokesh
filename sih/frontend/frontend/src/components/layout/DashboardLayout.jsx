import Sidebar from "./Sidebar";
import Topbar from "./Topbar";

const DashboardLayout = ({
  children
}) => {
  return (
    <div className="flex">

      <Sidebar />

      <main className="flex-1 p-6">

        <Topbar />

        <div className="mt-6">
          {children}
        </div>

      </main>

    </div>
  );
};

export default DashboardLayout;
