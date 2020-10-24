import React from "react";
import { LinkContainer } from 'react-router-bootstrap';
import NavItem from "react-bootstrap/NavItem"
import "../css/Links.css"
function Links(){
    return(
        <>
            <LinkContainer className = "LinkItem"to="/">
                <NavItem>Home</NavItem>
            </LinkContainer>

            <LinkContainer className = "LinkItem" to="/about">
              <NavItem >About</NavItem>
            </LinkContainer>

            <LinkContainer className = "LinkItem" to="/discover">
              <NavItem >Discover</NavItem>
            </LinkContainer>

            <LinkContainer className = "LinkItem" to="/features">
              <NavItem>Features</NavItem>
            </LinkContainer>

            <LinkContainer className = "LinkItem" to="/suggest">
              <NavItem >Suggest</NavItem>
            </LinkContainer>

            <LinkContainer className = "LinkItem" to="/contact">
              <NavItem >Contact</NavItem>
            </LinkContainer>
        </>
    )
}

export default Links;