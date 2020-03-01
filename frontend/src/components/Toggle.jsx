import React from "react";
import axios from "axios";

class Toggle extends React.Component {
    constructor(props) {
      super(props);
      this.state = {isToggleOn: true};
  
      // This binding is necessary to make `this` work in the callback
      this.handleClick = this.handleClick.bind(this);
      this.sendAuto = this.sendAuto.bind(this);
      this.sendManual = this.sendManual.bind(this);
      this.test = this.test.bind(this);
    }

    test()
    {
        alert("a")
    }
    
    async sendAuto()
    {
        const response = await axios.post('http://localhost:5000/data/settings', { mode: 'auto', manual:'' });
    }

    async sendManual()
    {
        const response = await axios.post('http://localhost:5000/data/settings', { mode: 'manual', manual: {window1: 'open'} });
    }

    handleClick() 
    {
        this.state.isToggleOn ? this.sendAuto() : this.sendManual()
        this.setState(prevState => ({
            isToggleOn: !prevState.isToggleOn
        }));
    }
  
    render() 
    {
      return (
        <button onClick={this.handleClick}>
          {this.state.isToggleOn ? 'AUTO' : 'MANUAL'}
        </button>
      );
    }
  }

  export default Toggle;