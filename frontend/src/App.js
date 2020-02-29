import React from 'react';
import logo from './logo.svg';
import './App.css';

import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import navBar from "./components/navBar";
import settings from "./components/settings";
import Footing from "./components/Footing";
import home from "./components/home"


function App() {
	return (
		<div className="App">
			<Router>
				<div className="heading-container">
					{/* <img className="dunin-logo" src={Dunin} alt="Dunin"></img> */}
					<navBar></navBar>
				</div>
				<Switch>
					<Route path="/" exact component={home} />
				</Switch>
			</Router>
			<Footing></Footing>
		</div>
  );
}

export default App;
