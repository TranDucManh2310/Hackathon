import React from 'react';

class ChatBox extends React.Component {
  render() {
    return (
      <div className="chat-box">
        {this.props.messages.map((message, index) => (
          <p key={index} className={message.sender}>
            {message.text}
          </p>
        ))}
      </div>
    );
  }
}

export default ChatBox;