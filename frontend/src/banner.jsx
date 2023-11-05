import React from 'react';

import hotel from '../public/images/hotel.jpeg';

const Banner = () => {
  return (
    <div className="banner">
      <h1>Welcome to Our Restaurant</h1>
    <img src={hotel} alt="" />
    </div>
  );
};

export default Banner;
