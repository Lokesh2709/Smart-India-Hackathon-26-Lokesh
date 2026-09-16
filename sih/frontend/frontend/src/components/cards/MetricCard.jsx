const MetricCard = ({ title, value }) => {
  return (
    <div className="bg-green-200 rounded-2xl shadow-lg p-6 hover:scale-105 transition">
      <h3 className="text-green-900 font-semibold">
        {title}
      </h3>

      <p className="text-4xl font-bold mt-2">
        {value}
      </p>
    </div>
  );
};

export default MetricCard;
