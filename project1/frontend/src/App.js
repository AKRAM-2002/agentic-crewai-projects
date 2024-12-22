import React from 'react';
import JokeGenerator from './components/JokeGenerator';

function App() {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-6">Chuck Norris Joke App</h1>
      <JokeGenerator />
      <hr className="my-6" />
    
    </div>
  );
}

export default App;
