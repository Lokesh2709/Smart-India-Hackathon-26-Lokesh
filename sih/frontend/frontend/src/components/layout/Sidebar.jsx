import {
  LayoutDashboard,
  Users,
  Building2,
  BarChart3,
  Briefcase
} from "lucide-react";

import { Link } from "react-router-dom";

const Sidebar = () => {
  return (
    <aside className="w-64 min-h-screen bg-green-300 p-5 shadow-xl">

      <h1 className="text-2xl font-bold mb-10">
        Gov Portal
      </h1>

      <div className="space-y-6">

        <Link
          to="/"
          className="flex gap-3 items-center"
        >
          <LayoutDashboard size={20} />
          Dashboard
        </Link>

        <Link
          to="/students"
          className="flex gap-3 items-center"
        >
          <Users size={20} />
          Students
        </Link>

        <Link
          to="/recruiters"
          className="flex gap-3 items-center"
        >
          <Building2 size={20} />
          Recruiters
        </Link>

        <Link
          to="/analytics"
          className="flex gap-3 items-center"
        >
          <BarChart3 size={20} />
          Analytics
        </Link>

        <Link
          to="/jobs"
          className="flex gap-3 items-center"
        >
          <Briefcase size={20} />
          Jobs
        </Link>

      </div>

    </aside>
  );
};

export default Sidebar;