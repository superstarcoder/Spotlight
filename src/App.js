import React from 'react';
import Navbar from './components/navbar'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

function App() {
  return (
    <Router>
      
      <Navbar />
    </Router>
  );
}

export default App;
