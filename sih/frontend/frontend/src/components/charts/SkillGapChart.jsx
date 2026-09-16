import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip
} from "recharts";

const SkillGapChart = ({ data }) => {

  return (

    <div className="bg-white p-5 rounded-xl shadow">

      <h3 className="font-bold mb-4">

        Skill Gap

      </h3>

      <ResponsiveContainer
        width="100%"
        height={300}
      >

        <BarChart data={data}>

          <XAxis dataKey="skill_name" />

          <YAxis />

          <Tooltip />

          <Bar dataKey="gap" />

        </BarChart>

      </ResponsiveContainer>

    </div>
  );
};

export default SkillGapChart;