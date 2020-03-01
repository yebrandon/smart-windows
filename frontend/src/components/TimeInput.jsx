import TimeField from 'react-simple-timefield';
 
class TimeInput extends React.Component {
  constructor(...args) {
    super(...args);
 
    this.state = {
      time: '12:34'
    };
 
    this.onTimeChange = this.onTimeChange.bind(this);
  }
 
  onTimeChange(event, time) 
  {
    this.setState({time});
  }
 
  render() 
  {
    const {time} = this.state;
 
    return (
      <TimeField value={time} onChange={this.onTimeChange} />
    );
  }
}

export default TimeInput