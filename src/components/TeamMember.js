import React from "react"
import Card from "react-bootstrap/Card"
import "../css/TeamMember.css"
function TeamMember(props){
    return (
        <center>
                <Card className = "Member" >
                <Card.Img variant="top" src = {props.img} style = {{"height": "100%", "width": "100%"}}/>
                <Card.Body>
                    <center>
                    <Card.Title>{props.name}</Card.Title>
                    <Card.Text>
                        {props.content}
                    </Card.Text>
                    </center>
                </Card.Body>
            </Card>
        </center>
    )
}
export default TeamMember;