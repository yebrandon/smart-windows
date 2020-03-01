import React from "react";
import "./NavBar.css";
import { NavLink } from "react-router-dom";

class NavBar extends React.Component {
	render() {
		return (
			<>
			<h1>SMART WINDOWS</h1>
			<nav className="Nav">
				<ul className="navitems">
					<NavLink
						className="link-item home"
						activeClassName="link-item-active home"
						to="/home"
					>
						Home
					</NavLink>
					<NavLink
						className="link-item settings"
						activeClassName="link-item-active settings"
						to="/settings"
					>
						Settings
					</NavLink>

				</ul>
			</nav>
			</>
		);
	}
}

export default NavBar;
