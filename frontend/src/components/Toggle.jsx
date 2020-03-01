import React from "react";
import axios from "axios";


class Toggle extends React.Component {
    constructor(props) {
      super(props);
      this.state = 
      {
        isToggleOn: true,
      };
  
    }


    handleClick = (e) => 
    {

        this.setState
        (prevState => ({
          isToggleOn: !prevState.isToggleOn
      }));

      if(this.state.isToggleOn)
      {
        console.log("open")
        axios
        .post("http//:localhost:5000/data/command", "open")
        .then(response => {
          console.log(response)
        })
        .catch(error =>{
          console.log(error)
        })
      }
      else
      {
        console.log("closed")
        axios
        .post("http//:localhost:5000/data/command", "closed")
        .then(response => {
          console.log(response)
        })
        .catch(error =>{
          console.log(error)
        })
      }
    }
  
    render() 
    {
      return (
        <button onClick={this.handleClick}>
          {this.state.isToggleOn ? 'Close' : 'Open'}
        </button>
      );
    }
  }

  export default Toggle;