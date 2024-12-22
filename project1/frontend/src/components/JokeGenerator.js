import React, { useState } from 'react';
import axios from 'axios';

function JokeGenerator() {
  const [jokes, setJokes] = useState([]);
  const [bestJoke, setBestJoke] = useState("");

  const generateJokes = async () => {
    const response = await axios.post('http://localhost:5000/generate');
    setJokes(response.data.jokes);
  };

  const pickBestJoke = async () => {
    const response = await axios.post('http://localhost:5000/pick', { jokes });
    setBestJoke(response.data.best_joke);
  };

  return (
    <div className="p-4 max-w-lg mx-auto">
      <button
        onClick={generateJokes}
        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Generate Jokes
      </button>
      <div className="mt-4">
        {jokes.map((joke, index) => (
          <p key={index} className="p-2 border-b border-gray-300">{joke}</p>
        ))}
      </div>
      <button
        onClick={pickBestJoke}
        disabled={jokes.length === 0}
        className={`mt-4 bg-green-500 text-white px-4 py-2 rounded ${jokes.length === 0 ? "opacity-50" : "hover:bg-green-700"}`}
      >
        Pick the Best Joke
      </button>
      {bestJoke && <h3 className="mt-4 text-xl font-bold">Best Joke: {bestJoke}</h3>}
    </div>
  );
  
}

export default JokeGenerator;
