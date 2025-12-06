/**
 * SummaryCard Component
 * Displays summary information in card format.
 */

import React from 'react';
import './SummaryCard.css';

const SummaryCard = ({ summary }) => {
  return (
    <div className="summary-card">
      <div className="card-header">
        <h3>📊 Summary</h3>
      </div>
      <div className="card-content">
        <p>{summary || 'Send a query to see analysis summary here.'}</p>
      </div>
    </div>
  );
};

export default SummaryCard;
