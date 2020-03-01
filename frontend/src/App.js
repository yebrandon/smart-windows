import React from 'react';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import Settings from "./components/Settings";
import Footing from "./components/Footing";
import Home from "./components/Home";
import Mode from "./components/Mode";
import Actions from "./components/Actions";

function App() {
	return (
		<div className="App">
			<Router>
				<div className="heading-container">
					{/* <img className="dunin-logo" src={Dunin} alt="Dunin"></img> */}
					<NavBar></NavBar>
				</div>
				<Switch>
					
					<Route path="/" exact component={Home} />
					<Route path="/home" exact component={Home} />
					<Route path = "/settings" exact component = {Settings}/>
					<Route path = "/mode" exact component = {Mode}/>
					<Route path = "/actions" exact component = {Actions}/>
          			
				</Switch>
			</Router>
			<Footing></Footing>
		</div>
  );
}

export default App;
