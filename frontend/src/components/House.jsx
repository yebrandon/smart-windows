import React from "react";
import "./House.css";
import { Link } from 'react-router-dom';

class House extends React.Component {

	render() {
		return (
			<div>
				<h1>Your house(s)</h1>
					<img src="https://purepng.com/public/uploads/large/purepng.com-big-househousebuildinghomewood-houseconcrete-house-1701528487135irhd4.png" width="200" alt="20 Crescent Drive, Kingston" ></img>

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
