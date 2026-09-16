const HubCard = ({
  title,
  description
}) => {
  return (
    <div
      className="
      bg-green-300
      rounded-3xl
      p-8
      shadow-xl
      hover:shadow-2xl
      hover:scale-105
      transition
      cursor-pointer
      "
    >
      <h2 className="text-2xl font-bold">
        {title}
      </h2>

      <p className="mt-4 text-green-900">
        {description}
      </p>
    </div>
  );
};

export default HubCard;
