import React from "react";
import "./Mode.css";
import Toggle from "./Toggle.jsx";

class Mode extends React.Component {
	render() {
		return (
			<>
				<h1> Click to switch the mode </h1>
				<Toggle></Toggle>
			</>

			

		);
	}
}

export default Mode;
