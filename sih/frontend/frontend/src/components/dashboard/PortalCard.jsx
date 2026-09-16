import { useNavigate } from "react-router-dom";

const PortalCard = ({
  title,
  description,
  route
}) => {

  const navigate = useNavigate();

  return (
    <div
      onClick={() => navigate(route)}
      className="
      cursor-pointer
      rounded-3xl
      p-8
      bg-gradient-to-br
      from-green-100
      to-green-300
      shadow-lg
      transition-all
      duration-300
      hover:-translate-y-2
      hover:scale-105
      hover:shadow-2xl
      "
    >
      <h2
        className="
        text-3xl
        font-bold
        transition-colors
        duration-300
        hover:text-amber-700
        "
      >
        {title}
      </h2>

      <p className="mt-4">
        {description}
      </p>
    </div>
  );
};

export default PortalCard;