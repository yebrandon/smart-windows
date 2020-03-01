import React from "react";
import axios from "axios";

class Form extends React.Component 
{
    constructor(props) 
    {
      super(props);
      this.state = {value: ''};
      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
      this.sendLocation = this.sendLocation.bind(this);
    }

    async sendLocation()
    {
        var location = this.state.value
        const response = await axios.post('http://localhost:5000/data/settings', location)
    }
  
    handleChange(event) 
    {
      this.setState({value: event.target.value});
    }
  
    handleSubmit(event) 
    {
        this.sendLocation();
        
      alert('A location was submitted: ' + this.state.value);

      event.preventDefault();
    }
  
    render() {
      return (
        <form onSubmit={this.handleSubmit}>
          <label>

            <input type="text" value={this.state.value} onChange={this.handleChange} />
          </label>
          <input type="submit" value="Submit" />
        </form>
      );
    }
  }

  export default Form;