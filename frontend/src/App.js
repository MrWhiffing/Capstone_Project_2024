import React, { useState } from 'react';
import './App.css';
import FertilizerForm from './components/FertilizerForm';
import FertilizerResult from './components/FertilizerResult';
import Loader from './components/Loader';

function App() {
  const [fertilizer, setFertilizer] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (data) => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch('http://127.0.0.1:5000/recommend-fertilizer', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      const result = await response.json();
      setFertilizer(result.recommended_fertilizer);
    } catch (err) {
      setError('An error occurred. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Fertilizer Recommendation System</h1>
      <FertilizerForm onSubmit={handleSubmit} />
      {loading && <Loader />}
      {error && <p>{error}</p>}
      {fertilizer && <FertilizerResult fertilizer={fertilizer} />}
    </div>
  );
}

export default App;
