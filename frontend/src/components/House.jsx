import React from "react";
import "./House.css";
import { Link } from 'react-router-dom';

class House extends React.Component {

	render() {
		return (
			<div>
				<h1>Your house(s)</h1>
					<img src="https://previews.123rf.com/images/bruno1998/bruno19981009/bruno1998100900013/7697370-glossy-illustration-of-a-simple-house-with-one-window-and-door.jpg" width="200" height="80" alt="20 Crescent Drive, Kingston" ></img>
				<p> Pick a house </p>

				<Link to="/Layout">
					<button type="button">
						Continue
					</button>
				</Link>

			</div>
		);
	}
}

export default House;
