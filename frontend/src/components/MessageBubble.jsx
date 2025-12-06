/**
 * MessageBubble Component
 * Displays a single chat message (user or bot).
 */

import React from 'react';
import './MessageBubble.css';

const MessageBubble = ({ message, isUser }) => {
  return (
    <div className={`message-bubble ${isUser ? 'user' : 'bot'}`}>
      <div className={`bubble-content ${isUser ? 'user-content' : 'bot-content'}`}>
        {isUser ? '👤' : '🤖'}
        <span>{message}</span>
      </div>
    </div>
  );
};

export default MessageBubble;
