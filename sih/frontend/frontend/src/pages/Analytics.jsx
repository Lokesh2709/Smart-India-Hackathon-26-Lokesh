import { useEffect, useState } from "react";

import DashboardLayout
from "../components/layout/DashboardLayout";

import SectorDemandChart
from "../components/charts/SectorDemandChart";

import SkillGapChart
from "../components/charts/SkillGapChart";

import {
  getHighestSkilledSectors,
  getSkillGap
}
from "../services/governmentService";

const Analytics = () => {

  const [sectors, setSectors] =
    useState([]);

  const [skillGap, setSkillGap] =
    useState([]);

  useEffect(() => {

    loadAnalytics();

  }, []);

  const loadAnalytics = async () => {

    try {

      const sectorsData =
        await getHighestSkilledSectors();

      setSectors(
        sectorsData.data
      );

      const gapData =
        await getSkillGap();

      setSkillGap(
        gapData.data
      );

    } catch (err) {

      console.error(err);

    }
  };

  return (

    <DashboardLayout>

      <h1
        className="
        text-3xl
        font-bold
        mb-8
      "
      >
        Government Analytics
      </h1>

      <div
        className="
        grid
        grid-cols-2
        gap-6
      "
      >

        <SectorDemandChart
          data={sectors}
        />

        <SkillGapChart
          data={skillGap}
        />

      </div>

    </DashboardLayout>
  );
};

export default Analytics;