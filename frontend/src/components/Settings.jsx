import React from "react"
import axios from "axios"
import "./Settings.css"
import TimeInput from 'react-time-input';
import TimeField from 'react-simple-timefield';

class Settings extends React.Component 
{
	constructor(props) 
	{
		super(props);
		this.state = 
		{
			country :'',
			city : '',
			pref_temp: 0.0,
			mode:'auto',
		};
	}

	changeHandler = (e) =>
	{
		this.setState({[e.target.name]: e.target.value})
	}

	handleSubmit = (e) =>
    {
		e.preventDefault()
		console.log(this.state)
		axios
			.post('http//:localhost:5000/data/settings', this.state)
			.then(response => {
				console.log(response)
			})
			.catch(error =>{
				console.log(error)
			})
	}


	render() 
	{

		const { city, country, pref_temp, mode, open_time } = this.state
		return (
			<>
				<h1>Settings</h1>
				<form onSubmit={this.handleSubmit}>

				<label>Preferred Temperature (Celcius): </label>
				<input type="number" name="pref_temp" value = {parseFloat(pref_temp)} onChange={this.changeHandler} />
				<br></br>

				<label>Country: </label>
				<input type="text" name="country" onChange={this.changeHandler} />
				<br></br>
				
				<label>City: </label>
				<input type="text" name="city" onChange={this.changeHandler} />
				<br></br>

				<label for="mode">Choose a mode:</label>
				<select id="mode" name="mode" onChange = {this.changeHandler}>
					<option value="auto">Automatic</option>
					<option value="man">Manual</option>
				</select>
				<br></br>

				<button type = "submit">Submit</button>
				</form>

			</>
		);
	}
}


export default Settings;