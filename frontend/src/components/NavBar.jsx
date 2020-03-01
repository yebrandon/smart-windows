import React from "react";
import "./NavBar.css";
import { NavLink } from "react-router-dom";

class NavBar extends React.Component {
	render() {
		return (
			<>
			<nav className="Nav">
				<ul className="navitems">
					<NavLink
						className="link-item home"
						activeClassName="link-item-active home"
						to="/Home"
					>
						Home
					</NavLink>
					<NavLink
						className="link-item settings"
						activeClassName="link-item-active settings"
						to="/Settings"
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
