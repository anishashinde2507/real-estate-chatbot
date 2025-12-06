/**
 * DataTable Component
 * Displays filtered real estate data in table format.
 */

import React from 'react';
import './DataTable.css';

const DataTable = ({ data }) => {
  if (!data || data.length === 0) {
    return (
      <div className="data-table-wrapper">
        <div className="table-header">
          <h3>📋 Property Data</h3>
        </div>
        <div className="empty-table">
          <p>No data to display. Send a query to see results.</p>
        </div>
      </div>
    );
  }

  // Get column headers from first row
  const columns = Object.keys(data[0]);

  return (
    <div className="data-table-wrapper">
      <div className="table-header">
        <h3>📋 Property Data ({data.length} rows)</h3>
      </div>
      <div className="table-container">
        <table className="data-table">
          <thead>
            <tr>
              {columns.map((col) => (
                <th key={col}>{col}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.map((row, idx) => (
              <tr key={idx} className={idx % 2 === 0 ? 'even' : 'odd'}>
                {columns.map((col) => (
                  <td key={`${idx}-${col}`}>
                    {typeof row[col] === 'number'
                      ? row[col].toFixed(0)
                      : row[col]}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default DataTable;
