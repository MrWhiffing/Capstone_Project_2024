import React, { useState } from 'react';

const FertilizerForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({
    temperature: '',
    humidity: '',
    moisture: '',
    nitrogen: '',
    potassium: '',
    phosphorus: '',
    soilType: '',
    cropType: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Temperature:</label>
        <input type="number" name="temperature" value={formData.temperature} onChange={handleChange} />
      </div>
      <div>
        <label>Humidity:</label>
        <input type="number" name="humidity" value={formData.humidity} onChange={handleChange} />
      </div>
      <div>
        <label>Moisture:</label>
        <input type="number" name="moisture" value={formData.moisture} onChange={handleChange} />
      </div>
      <div>
        <label>Nitrogen:</label>
        <input type="number" name="nitrogen" value={formData.nitrogen} onChange={handleChange} />
      </div>
      <div>
        <label>Potassium:</label>
        <input type="number" name="potassium" value={formData.potassium} onChange={handleChange} />
      </div>
      <div>
        <label>Phosphorus:</label>
        <input type="number" name="phosphorus" value={formData.phosphorus} onChange={handleChange} />
      </div>
      <div>
        <label>Soil Type:</label>
        <input type="text" name="soilType" value={formData.soilType} onChange={handleChange} />
      </div>
      <div>
        <label>Crop Type:</label>
        <input type="text" name="cropType" value={formData.cropType} onChange={handleChange} />
      </div>
      <button type="submit">Get Recommendation</button>
    </form>
  );
};

export default FertilizerForm;
