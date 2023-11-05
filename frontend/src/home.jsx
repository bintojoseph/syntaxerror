import React, { useState } from 'react';
import './App.css';
import NavbarComponent from './NavbarComponent.jsx'
import Contact from './Contact.jsx';
import Banner from './banner.jsx';
import hotel from '../public/images/hotel.jpeg';

function home(){
    
  return (
    <div className="">
      <NavbarComponent/>  
      <Banner/> 
      <h1 className="text-5xl font-bold mt-10 mb-10 text-center">Veg Menu</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 ml-20 mr-10">
        {dishes.map((dish, index) => (
          <div key={index} className="bg-white p-4 mr-10 mb-10 rounded shadow">
            <img
              src={dish.image}
              alt={dish.name}
              className="mb-2 rounded-md w-full h-60 object-cover"
              onClick={()=>openModal(dish)}
            />
            <div className="text-xl font-bold text-black">{dish.name}</div>
            <div className='text-black'>{dish.price}</div>
          </div>
        ))}
      </div>

      {/* Modal */}
      {selectedDish && (
        <div className="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50">
          <div className="bg-white p-8 max-w-md rounded shadow-lg flex justify-between bg-gray-100 w-1/2 ">
            <div>
              <img className="mb-2 rounded-md w-full h-60 object-cover" src={selectedDish.image} alt="" />
            </div>
            <div className='flex-col flex  justify-between items-center'>
              <div>
                <h2 className="text-xl text-center text-black font-bold mb-4 mt-10">{selectedDish.name}</h2>
                <p  className='text-black'>{selectedDish.ingredients}</p>
              </div>
              <div>
                  <button onClick={closeModal} className="mt-4 px-4 py-2 bg-blue-500 text-white mb-10 rounded-md">
                    Close
                  </button> 
              </div>
            </div>
         
          </div>
        </div>
      )}
    <Contact/>

    </div>
  );
}

export default App;
