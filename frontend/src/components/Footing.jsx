import React from "react";
import "./Footer.css";
import * as Text from ".././strings.json";
class Footing extends React.Component {
	render() {
		const building = Text.Footer.building;
		const email = Text.Footer.email;
		const info = Text.Footer.info;
		const street = Text.Footer.street;
		return (
			<div className="footer">
				<ul className="footer-list contact-info">
					<li>{info}</li>
					<li>{email}</li>
				</ul>
				<ul className="footer-list location">
					<li>{building}</li>
					<li>{street}</li>
				</ul>
			</div>
		);
	}
}

export default Footing;
