import React from "react";
import { Link } from "react-router-dom";
import logo from "./img/blah2.png"
function Navbar(){
    return(
        <header className="header">
        <div className="container" style = {{background: "gray"}}>
            <div className="row">
                <div className="col-lg-2">
                    <div className="header__logo">
                    <Link to = "/">
                        <img src={logo} alt="Spotlight Logo"/>
                    </Link> 
                    </div>
                </div>
                <div className="col-lg-10">
                    <div className="header__nav__option">
                        <nav className="header__nav__menu mobile-menu">
                            <ul>
                                <li><Link to = "/" >Home</Link></li>
                                <li><Link to = "/about">About</Link></li>
                                <li><Link to = "/discover">Discover</Link></li>
                                <li><Link to = "/features">Features</Link></li>
                                <li><Link to = "/suggest">Suggest</Link></li>
                                <li><a href="/contact">Contact</a></li>
                                
                            </ul>
                        </nav>
                    </div>
                </div>
            </div>
            <div id="mobile-menu-wrap"></div>
        </div>
    </header>
    )
}

export default Navbar;