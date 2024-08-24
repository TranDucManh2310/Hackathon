import React from 'react';

class ChatInput extends React.Component {
  state = {
    message: ''
  };

  handleChange = (event) => {
    this.setState({ message: event.target.value });
  };

  handleSubmit = (event) => {
    event.preventDefault();
    this.props.sendMessage(this.state.message);
    this.setState({ message: '' });
  };

  render() {
    return (
      <form className="chat-input" onSubmit={this.handleSubmit}>
        <input
          type="text"
          placeholder="Type a message..."
          value={this.state.message}
          onChange={this.handleChange}
        />
        <button type="submit">Send</button>
      </form>
    );
  }
}

export default ChatInput;