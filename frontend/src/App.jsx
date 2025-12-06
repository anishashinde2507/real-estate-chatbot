/**
 * Main App Component
 * Orchestrates all sub-components and manages API communication.
 */

import React, { useState } from 'react';
import ChatWindow from './components/ChatWindow';
import SummaryCard from './components/SummaryCard';
import TrendChart from './components/TrendChart';
import DataTable from './components/DataTable';
import { sendQuery } from './api/queryApi';
import './App.css';

function App() {
  const [analysis, setAnalysis] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSendMessage = async (message, callback) => {
    setIsLoading(true);
    setError(null);

    try {
      // Send query to backend
      const result = await sendQuery(message);

      // Update analysis state
      setAnalysis(result);

      // Generate bot response based on type
      if (result.type === 'comparison') {
        const botResponse = result.areas && result.areas.length > 0
          ? `✅ Comparison complete! Showing trends for ${result.areas.join(' and ')}.`
          : '❌ Could not find the requested areas.';
        callback(botResponse);
      } else {
        const botResponse =
          result.area && result.table && result.table.length > 0
            ? `✅ Analysis complete for ${result.area}! Found ${result.table.length} records.`
            : '❌ No data found for the requested area. Try asking about: Wakad, Akurdi, Aundh, Ambegaon Budruk, or Baner.';
        callback(botResponse);
      }
    } catch (err) {
      const errorMsg =
        '⚠️ Error connecting to backend. Please ensure the Django server is running on http://localhost:8000';
      setError(errorMsg);
      callback(errorMsg);
      console.error('Error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-container">
      <div className="app-layout">
        {/* Chat Section */}
        <div className="chat-section">
          <ChatWindow onSendMessage={handleSendMessage} isLoading={isLoading} />
        </div>

        {/* Results Section */}
        <div className="results-section">
          {analysis && (
            <>
              {/* Summary and Chart Row */}
              <div className="row two-columns">
                <div className="column">
                  <SummaryCard summary={analysis?.summary} />
                </div>
                <div className="column">
                  <TrendChart
                    data={analysis?.chart || { years: [], values: [] }}
                  />
                </div>
              </div>

              {/* Table Row - Handle both single and comparison modes */}
              {analysis.type === 'comparison' ? (
                // Multiple tables for comparison
                <div className="row full-width">
                  <div style={{ width: '100%' }}>
                    <h3 style={{ marginTop: '20px', textAlign: 'center' }}>📊 Detailed Comparison Data</h3>
                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', marginTop: '15px' }}>
                      {analysis.areas && analysis.areas.map((areaName) => (
                        <div key={areaName}>
                          <h4 style={{ padding: '10px', background: '#f5f5f5', borderRadius: '4px' }}>{areaName}</h4>
                          <DataTable data={analysis.tables?.[areaName]} />
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              ) : (
                // Single table for single area
                <div className="row full-width">
                  <DataTable data={analysis?.table} />
                </div>
              )}
            </>
          )}
        </div>
      </div>

      {error && <div className="error-banner">{error}</div>}
    </div>
  );
}

export default App;
