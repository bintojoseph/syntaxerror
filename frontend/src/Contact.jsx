import React from 'react';

const Contact = () => {
  const phoneNumber = "65865656565";
  const emailAddress = "safafsa@gmail.com";

  return (
    <div className="container mx-auto p-4 flex flex-col items-center p-10vh justify-center h-screen" id="contact" >
      <h2 className="text-5xl font-bold mb-4">Contact Us</h2>
      <div className='flex flex-col'>

      
      <div className="mb-4 m-20">
        <label className="block text-gray-700 font-bold mb-2 text-3xl text-center">Phone</label>
        <p className='text-center text-xl mb-4'>{phoneNumber}</p>
      </div>
      <div className="mb-4 text-center">
        <label className="block text-gray-700 font-bold mb-2 text-3xl">Email</label>
        <p className='text-center text-xl mb-4'>{emailAddress}</p>
      </div>
    </div>
    </div>
  );
};

export default Contact;
