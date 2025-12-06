/**
 * TrendChart Component
 * Displays price trend using Recharts line chart.
 */

import React from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from 'recharts';
import './TrendChart.css';

const TrendChart = ({ data }) => {
  // Check if this is a comparison (has areas) or single area data
  const isComparison = data.areas && Object.keys(data.areas).length > 0;

  let chartData;

  if (isComparison) {
    // Transform comparison data for Recharts
    chartData = data.years.map((year, index) => {
      const yearData = { year };
      // Add each area's data
      for (const [areaName, prices] of Object.entries(data.areas)) {
        yearData[areaName] = prices[index];
      }
      return yearData;
    });
  } else {
    // Transform single area data for Recharts
    chartData = data.years.map((year, index) => ({
      year,
      price: data.values ? data.values[index] : 0,
    }));
  }

  return (
    <div className="trend-chart">
      <div className="chart-header">
        <h3>📈 Price Trend</h3>
      </div>
      <div className="chart-content">
        {chartData.length > 0 ? (
          <ResponsiveContainer width="100%" height={250}>
            <LineChart
              data={chartData}
              margin={{ top: 5, right: 30, left: 0, bottom: 5 }}
            >
              <CartesianGrid strokeDasharray="3 3" stroke="#e0e0e0" />
              <XAxis
                dataKey="year"
                stroke="#999"
                style={{ fontSize: '12px' }}
              />
              <YAxis
                stroke="#999"
                style={{ fontSize: '12px' }}
                label={{ value: 'Price (₹/sqft)', angle: -90, position: 'insideLeft' }}
              />
              <Tooltip
                contentStyle={{
                  background: '#fff',
                  border: '1px solid #ccc',
                  borderRadius: '8px',
                }}
                formatter={(value) => isComparison ? `₹${value?.toLocaleString() || 0}/sqft` : `₹${value} Lakhs`}
                cursor={{ stroke: '#667eea', strokeWidth: 2 }}
              />
              {isComparison ? (
                // Multiple lines for comparison
                Object.keys(data.areas).map((areaName, index) => {
                  const colors = ['#667eea', '#f093fb', '#4facfe', '#00f2fe', '#ff6b6b'];
                  return (
                    <Line
                      key={areaName}
                      type="monotone"
                      dataKey={areaName}
                      stroke={colors[index % colors.length]}
                      strokeWidth={2}
                      dot={{ r: 4 }}
                      activeDot={{ r: 6 }}
                      isAnimationActive={true}
                      name={areaName}
                    />
                  );
                })
              ) : (
                // Single line for single area
                <Line
                  type="monotone"
                  dataKey="price"
                  stroke="#667eea"
                  strokeWidth={3}
                  dot={{ fill: '#667eea', r: 5 }}
                  activeDot={{ r: 7 }}
                  isAnimationActive={true}
                />
              )}
            </LineChart>
          </ResponsiveContainer>
        ) : (
          <div className="empty-state">No chart data available</div>
        )}
      </div>
    </div>
  );
};

export default TrendChart;
