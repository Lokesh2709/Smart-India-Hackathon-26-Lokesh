const AnalyticsTile = ({
  title
}) => {
  return (
    <div
      className="
      bg-gradient-to-br
      from-green-100
      to-green-200
      rounded-2xl
      p-4
      shadow
      cursor-pointer
      hover:scale-105
      hover:shadow-xl
      transition-all
      duration-300
      "
    >
      <h3
        className="
        font-semibold
        text-lg
        hover:text-amber-700
        transition-colors
        "
      >
        {title}
      </h3>
    </div>
  );
};

export default AnalyticsTile;