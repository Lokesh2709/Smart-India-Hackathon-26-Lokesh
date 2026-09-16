import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip
} from "recharts";

const SectorDemandChart = ({ data }) => {

  return (

    <div className="bg-white p-5 rounded-xl shadow">

      <h3 className="font-bold mb-4">

        Highest Skilled Sectors

      </h3>

      <ResponsiveContainer
        width="100%"
        height={300}
      >

        <BarChart data={data}>

          <XAxis dataKey="sector" />

          <YAxis />

          <Tooltip />

          <Bar dataKey="count" />

        </BarChart>

      </ResponsiveContainer>

    </div>
  );
};

export default SectorDemandChart;