import React, { useEffect, useState } from 'react';
import ChatBox from './ChatBox';
import ChatInput from './ChatInput';

class Chat extends React.Component {
  // ... state và các phương thức khác ...

  componentDidMount() {
    this.socket = new WebSocket('ws://localhost:12345');
    this.socket.onmessage = (event) => {
      const botMessage = JSON.parse(event.data);
      this.setState(prevState => ({
        messages: [...prevState.messages, { text: botMessage, sender: 'bot' }]
      }));
    };
  }

  sendMessage = (message) => {
    this.socket.send(JSON.stringify(message));
    this.setState(prevState => ({
      messages: [...prevState.messages, { text: message, sender: 'user' }]
    }));
  };

  getBotMessage = async (message) => {
    // Call the chatbot API here
    // For now, let's just return a dummy message
    return "I'm a chatbot. You said: " + message;
  };

  render() {
    return (
      <div className="chat">
        <ChatBox messages={this.state.messages} />
        <ChatInput sendMessage={this.sendMessage} />
      </div>
    );
  }
}

export default Chat;