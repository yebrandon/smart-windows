import React from "react";
import "./Layout.css";
import Settings from "./Settings";
import { Link } from 'react-router-dom';
import Toggle from './Toggle';
import SetTime from './SetTime';
import axios from "axios"
import TimeField from 'react-simple-timefield';

class Layout extends React.Component{

	constructor(props) 
	{
		super(props);
		this.state = 
		{
            temp:'',
            windowState:'',
            open_time:"00:00",
            close_time:"00.00"
		};
	}

	changeHandler = (e) =>
	{
		this.setState({[e.target.name]: e.target.value})
	}

	handleSubmit = (e) =>
    {
		e.preventDefault()
		console.log(this.state.open_time)
		console.log(this.state.close_time)
		axios
			.post('http//:localhost:5000/data/settings', this.state.open_time)
			.then(response => {
				console.log(response)
			})
			.catch(error =>{
				console.log(error)
            })
        axios
			.post('http//:localhost:5000/data/settings', this.state.close_time)
			.then(response => {
				console.log(response)
			})
			.catch(error =>{
				console.log(error)
			})
	}

    async getTemp(){
        const response =
          await axios.get("http//:localhost:5000/data/temp")
        console.log(response.data)
        this.temp =  response.data
    }

    async getWindowState(){
        const response =
          await axios.get("http//:localhost:5000/data/windowState")
        console.log(response.data)
        this.windowState = response.data
    }

    render(){
        return(
            <div>
                <h1>Open/Close Windows</h1>
                <form onSubmit={this.handleSubmit}>
                Window Opens At: <TimeField name = "open_time" value={this.state.open_time} onChange={this.changeHandler} />
                <br></br>
                Window Closes At: <TimeField name = "close_time" value={this.state.close_time} onChange={this.changeHandler} />
                <br></br>
                <button type = "submit">Set</button>
                </form>
            
                Window Status: {this.state.windowState}
                <br></br>
                Temperature: {this.state.temp}
                <br></br>


                <img src="https://i.stack.imgur.com/HplbK.png" width="400" height="200" alt="20 Crescent Drive, Kingston" ></img>

                <Toggle type="Toggle" id = "On"></Toggle>
                
                

                <Link to="/Settings">
					<button type="button" name = "f">
						Back
					</button>
				</Link>
            </div>
            
        )
    }
}


export default Layout;