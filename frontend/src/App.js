import React from 'react';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import Settings from "./components/Settings";
import Footing from "./components/Footing";
import Home from "./components/Home";
import Mode from "./components/Mode";
import Actions from "./components/Actions";
import Layout from "./components/Layout"
import SetTime from './components/SetTime';
import House from './components/House';

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
					<Route path="/Home" exact component={Home} />
					<Route path = "/Settings" exact component = {Settings}/>
					<Route path="/Layout" exact component={Layout}/>
					<Route path = "/Actions" exact component = {Actions}/>
					<Route path = "/House" exact component = {House}/>
					<Route path="/SetTime" exact component={SetTime}/>
          			
				</Switch>
			</Router>
			<Footing></Footing>
		</div>
  );
}

export default App;
