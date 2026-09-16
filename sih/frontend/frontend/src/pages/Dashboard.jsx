import { useEffect, useState } from "react";

import DashboardLayout from "../components/layout/DashboardLayout";

import MetricCard from "../components/cards/MetricCard";

import WelcomeBanner from "../components/dashboard/WelcomeBanner";

import PortalCard from "../components/dashboard/PortalCard";

import AnalyticsSection from "../components/dashboard/AnalyticsSection";

import {
  getDashboardSummary
} from "../services/governmentService";

const Dashboard = () => {

  const [summary, setSummary] =
    useState({
      total_students: 0,
      total_recruiters: 0,
      total_skills: 0,
      active_challenges: 0,
      active_government_jobs: 0,
      active_campaigns: 0
    });

  useEffect(() => {
    loadDashboard();
  }, []);

  const loadDashboard = async () => {

    try {

      const response =
        await getDashboardSummary();

      setSummary(response.data);

    } catch (err) {

      console.error(err);

    }
  };

  return (
    <DashboardLayout>

      <WelcomeBanner />

      {/* Portal Cards */}

      <div className="grid grid-cols-2 gap-6 mt-8">

        <PortalCard
          title="Student Portal"
          description="Monitor student skills, projects, badges, AI evaluations and proof of work."
          route="/students"
        />

        <PortalCard
          title="Recruiter Portal"
          description="Monitor recruiters, hiring activity, industry demand and recruitment campaigns."
          route="/recruiters"
        />

      </div>

      {/* KPI */}

      <div className="grid grid-cols-3 gap-4 mt-10">

        <MetricCard
          title="Students"
          value={summary.total_students}
        />

        <MetricCard
          title="Recruiters"
          value={summary.total_recruiters}
        />

        <MetricCard
          title="Skills"
          value={summary.total_skills}
        />

        <MetricCard
          title="Challenges"
          value={summary.active_challenges}
        />

        <MetricCard
          title="Gov Jobs"
          value={summary.active_government_jobs}
        />

        <MetricCard
          title="Campaigns"
          value={summary.active_campaigns}
        />

      </div>

      <AnalyticsSection />

    </DashboardLayout>
  );
};

export default Dashboard;