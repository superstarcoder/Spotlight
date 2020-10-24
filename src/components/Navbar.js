import React from "react";
import Navbar from "react-bootstrap/Navbar"
import Nav from "react-bootstrap/Nav"
import Links from "./Links"
import "../css/Navbar.css"

function AppBar(){
  return(
      <Navbar bg="primary" expand="lg">
      <Navbar.Brand href="#home">
      <img
        src = {require("../img/blah2.png")}
        alt = "logo"
        width = "200px"
      />
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
            <Links/>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  )
}

export default AppBar;
