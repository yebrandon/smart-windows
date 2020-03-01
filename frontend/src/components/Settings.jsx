import React from "react";
import axios from "axios";
import Form from "./Form.jsx";
import "./Settings.css";

var querystring = require("querystring")
class Settings extends React.Component 
{
	constructor(props) 
	{
		super(props);
		this.state = {
			country: '',
			city:'',
			pref_temp: 0.0,
			open_time: [],
			close_time: [],
			mode:'',
		  };
		this.handleCountryChange = this.handleCountryChange.bind(this);
		this.handleCityChange = this.handleCityChange.bind(this);
		this.handleSubmit = this.handleSubmit.bind(this);
		this.handleTempChange = this.handleTempChange.bind(this);
		this.sendLocation = this.sendLocation.bind(this);
		this.sendTemp = this.sendTemp.bind(this);
	}

	async sendLocation()
    {
		const response = await axios.post('http://localhost:5000/data/settings', { "country" : this.country, "city" : this.city})
	}

	async sendTemp()
    {
        const response = await axios.post('http://localhost:5000/data/settings', this.pref_temp)
	}
	async sendOpen()
    {
        const response = await axios.post('http://localhost:5000/data/settings', this.open_time)
	}
	async sendClose()
    {
        const response = await axios.post('http://localhost:5000/data/settings', this.pref_temp)
	}
	async sendMode()
    {
        const response = await axios.post('http://localhost:5000/data/settings', this.mode)
	}
  
	handleCountryChange (evt) 
	{
		this.setState({ country: evt.target.value });
	}
	handleCityChange (evt) 
	{
		this.setState({ city: evt.target.value });
	}
	  
	handleTempChange (evt) 
	{
		this.setState({ pref_temp: evt.target.value });
	}

	handleOpenChange (evt) 
	{
		this.setState({ open_time: evt.target.value });
	}

	handleCloseChange (evt) 
	{
		this.setState({ close_temp: evt.target.value });
	}

	handleSubmit(event) 
    {
		event.preventDefault();
		// this.sendMode();
		this.sendLocation();
		// this.sendTemp();
		// this.sendClose();
		// this.sendOpen();
    }

	render() 
	{
		return (
			<>
				<h1>Settings</h1>
				<form onSubmit={this.handleSubmit}>
      
				<label for="mode">Choose a mode:</label>
				<select id="mode" name="mode">
					<option value="auto">Automatic</option>
					<option value="man">Manual</option>
				</select>
				<br></br>

				<label>Country: </label>
				<input type="text" name="country" onChange={this.handleCountryChange} />
				<br></br>
				
				<label>City: </label>
				<input type="text" name="city" onChange={this.handleCityChange} />
				<br></br>

				<label>Preferred Temperature (Celcius): </label>
				<input type="number" name="pref_temp" onChange={this.handleTempChange} />
				<br></br>

				{/*<label>Open Time: </label>
				<input type="time" name="open_temp" onChange={this.handleOpenChange} />
				<br></br>*/}

				{/*<label>Close Time: </label>
				<input type="time" name="open_temp" onChange={this.handleCloseChange} />
				<br></br>*/}

				<input type="submit" value="Submit" />
				</form>

			</>
		);
	}
}


export default Settings;