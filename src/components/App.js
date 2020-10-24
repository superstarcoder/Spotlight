import React from 'react';
import AppBar from "./Navbar"
import { BrowserRouter as Router, Route, Switch} from "react-router-dom"
import Footer from "./Footer"
function App() {
  return (
    <Router>
        <AppBar />
        <Footer/>
    </Router>
  );
}

export default App;
