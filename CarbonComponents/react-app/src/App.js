import React, { useState, useEffect } from 'react';
import { Button } from '@carbon/ibm-security';
import { get } from './utils/axiosUtils';
import logo from './logo.svg';
import './App.scss';

function App() {
  const [currentTime, setCurrentTime] = useState(0);
  const [offenses, setOffenses] = useState(undefined);

  const fetchTime = async() => {
      const data = await get('/time', window.location.href);
      setCurrentTime(data.time);
  }

  const fetchAllOffenses = async() => {
      const data = await get('/offenses', window.location.href);
      setOffenses(data.offenses);
  }

  useEffect(() => {
    fetchTime();
    fetchAllOffenses();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <p>The current time is {currentTime}.</p>
        <p>The ID of the first offense is... {offenses ? offenses[0].id : '...'}</p>
        <Button>Click me</Button>
      </header>
    </div>
  );
}

export default App;
