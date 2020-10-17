import React from "react";
import { render } from "react-dom";
import { BrowserRouter, Switch, Route, Redirect } from "react-router-dom";
import Home from "./components/Home";
//import About from "./About";
//import Contacts from "./Contacts";
import Navbar from './components/navbar'

const App = () => (
    <BrowserRouter>
        <Navbar />
        <Switch>
            <Route path="/" component={Home}/>
            <Redirect to="/" />
        </Switch>
    </BrowserRouter>
);

render(<App />, document.getElementById("root"));