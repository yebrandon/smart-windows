import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import "./Home.css";
import Footing from "./Footing";
import Settings from "./Settings";
import { Link } from 'react-router-dom';
class Home extends React.Component {
	render() {
		return (
			<div>
				<h1>Smart Windows</h1>
				<h5>By Watermelon Tech</h5>
				
				<Link to="/House">
					<button type="button">
						Continue
					</button>
				</Link>
			</div>
		);
	}
}

export default Home;
