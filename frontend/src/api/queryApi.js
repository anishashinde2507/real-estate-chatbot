/**
 * API utility for communicating with Django backend.
 * Handles all HTTP requests to /api/query endpoint.
 */

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

/**
 * Send query to backend and get analysis.
 * 
 * @param {string} message - User query message
 * @returns {Promise<Object>} Analysis result with summary, chart, and table
 */
export const sendQuery = async (message) => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/query/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error sending query:', error);
    throw error;
  }
};
