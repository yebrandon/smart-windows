import React from "react";
import "./Footer.css";
import * as Text from ".././strings.json";
class Footing extends React.Component {
	render() {
		const hours = Text.Footer.hours;
		const email = Text.Footer.email;
		const building = Text.Footer.building;
		const street = Text.Footer.street;
		const province = Text.Footer.province;
		const postalCode = Text.Footer.postalCode;
		return (
			<div className="footer">
				<ul className="footer-list contact-info">
					<li>{hours}</li>
					<li>{email}</li>
				</ul>
				<ul className="footer-list location">
					<li>{building}</li>
					<li>{street}</li>
					<li>{province}</li>
					<li>{postalCode}</li>
				</ul>
			</div>
		);
	}
}

export default Footing;
