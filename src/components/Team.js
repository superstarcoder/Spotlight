import React from "react";
import TeamMember from "./TeamMember"
import Danny from "../img/team-1.jpg"; 
import Neranjan from "../img/team-2.jpg"
import Charan from "../img/team-3.jpg"
import Leo from "../img/team-4.jpg"
import Container from "react-bootstrap/Container"
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"
import "../css/Team.css"

function Team(){
    return(
        <Container style = {{"paddingTop":  "200px"}}>
        <Row className="justify-content-md-center">
            <Col xs = "6" lg="3" className = "col">
                <TeamMember name = "Dhanish N" img = {Danny} content = "backend"/>
            </Col>
            <Col xs = "6" lg="3" className = "col">
                <TeamMember name = "Neranjan M" img = {Neranjan} content = "backend"/>
            </Col>
            <Col xs = "6" lg="3" className = "col">
                <TeamMember name = "Charan B" img = {Charan}  content = "backend"/>
            </Col>
            <Col xs = "6" lg="3" className = "col">
                <TeamMember name = "Leo X" img = {Leo} content = "frontend"/>
            </Col>
        </Row>
    </Container>
    )
}

export default Team;