import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

import {
  useEffect,
  useState
} from "react";

import {
  getTopStudentSkills,
  getTopDemandSkills
} from "../../services/governmentService";

const AnalyticsSection = () => {

  const [studentSkills, setStudentSkills] =
    useState([]);

  const [demandSkills, setDemandSkills] =
    useState([]);

  useEffect(() => {

    loadCharts();

  }, []);

  const loadCharts = async () => {

    try {

      const students =
        await getTopStudentSkills();

      const recruiters =
        await getTopDemandSkills();

      setStudentSkills(
        students.data
      );

      setDemandSkills(
        recruiters.data
      );

    } catch (err) {

      console.error(err);

    }
  };

  return (

    <div className="mt-12">

      <h2 className="text-3xl font-bold mb-6">
        Analytics Hub
      </h2>

      <div className="grid grid-cols-2 gap-6">

        <div className="bg-white p-5 rounded-xl shadow">

          <h3 className="font-bold mb-4">
            Top Student Skills
          </h3>

          <ResponsiveContainer
            width="100%"
            height={300}
          >

            <BarChart data={studentSkills}>

              <XAxis
                dataKey="skill_name"
              />

              <YAxis />

              <Tooltip />

              <Bar
                dataKey="count"
              />

            </BarChart>

          </ResponsiveContainer>

        </div>

        <div className="bg-white p-5 rounded-xl shadow">

          <h3 className="font-bold mb-4">
            Top Recruiter Demand
          </h3>

          <ResponsiveContainer
            width="100%"
            height={300}
          >

            <BarChart data={demandSkills}>

              <XAxis
                dataKey="skill_name"
              />

              <YAxis />

              <Tooltip />

              <Bar
                dataKey="count"
              />

            </BarChart>

          </ResponsiveContainer>

        </div>

      </div>

    </div>
  );
};

export default AnalyticsSection;