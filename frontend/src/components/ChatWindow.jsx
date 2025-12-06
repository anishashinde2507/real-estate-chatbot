/**
 * ChatWindow Component
 * Manages chat messages and input area.
 */

import React, { useRef, useEffect, useState } from 'react';
import MessageBubble from './MessageBubble';
import './ChatWindow.css';

const ChatWindow = ({ onSendMessage, isLoading }) => {
  const [input, setInput] = useState('');
  const messagesEndRef = useRef(null);
  const [messages, setMessages] = useState([
    {
      id: 1,
      text: 'Hello! 👋 Welcome to Real Estate Analysis Chatbot. Ask me about any area like "Analyze Wakad" or "Show price trend for Akurdi".',
      isUser: false,
    },
  ]);

  // Auto-scroll to latest message
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = () => {
    if (input.trim() === '') return;

    // Add user message
    const userMessage = {
      id: messages.length + 1,
      text: input,
      isUser: true,
    };

    setMessages([...messages, userMessage]);
    setInput('');

    // Send to parent for API call
    onSendMessage(input, (botResponse) => {
      const botMessage = {
        id: messages.length + 2,
        text: botResponse,
        isUser: false,
      };
      setMessages((prev) => [...prev, botMessage]);
    });
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="chat-window">
      <div className="chat-header">
        <h2>💬 Real Estate Analysis Chatbot</h2>
      </div>

      <div className="messages-container">
        {messages.map((msg) => (
          <MessageBubble
            key={msg.id}
            message={msg.text}
            isUser={msg.isUser}
          />
        ))}
        {isLoading && (
          <div className="loading-indicator">
            <span></span>
            <span></span>
            <span></span>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="input-area">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Ask me about an area... e.g., 'Analyze Wakad'"
          disabled={isLoading}
          rows="2"
        />
        <button
          onClick={handleSend}
          disabled={isLoading || input.trim() === ''}
          className="send-button"
        >
          {isLoading ? '⏳' : '➤'}
        </button>
      </div>
    </div>
  );
};

export default ChatWindow;
