import React from "react";

const Rating = ({ stars, onChange }) => {
  const starIds = [1, 2, 3, 4, 5];
  const starData = starIds.map(id => ({
    id: id,
    active: id <= stars
  }));
  return (
    <div>
      {starData.map(star => (
        <span
          style={{ color: star.active ? "gold" : "lightgrey" }}
          onClick={() => {
            onChange && onChange(star.id);
          }}
        >
          {star.active ? "★" : "☆"}
        </span>
      ))}
    </div>
  );
};

export default Rating;
