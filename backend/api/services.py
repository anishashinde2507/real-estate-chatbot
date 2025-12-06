"""
Service layer for real estate data analysis.
Handles Excel parsing, data filtering, and LLM-powered summaries.
"""

import os
import json
import requests
import pandas as pd
import logging
from typing import List, Dict, Any
from django.conf import settings

# Set up logging
logger = logging.getLogger(__name__)



class RealEstateService:
    """Service for reading and analyzing real estate data from Excel."""

    def __init__(self):
        """Initialize service with Excel file path."""
        self.file_path = settings.DATA_FILE_PATH
        self.df = None
        self._load_data()

    def _load_data(self) -> None:
        """Load Excel file into pandas DataFrame."""
        if os.path.exists(self.file_path):
            try:
                self.df = pd.read_excel(self.file_path, engine='openpyxl')
                print(f"✓ Data loaded successfully. Rows: {len(self.df)}")
            except Exception as e:
                print(f"✗ Error loading Excel file: {e}")
                self.df = self._get_sample_data()
        else:
            print(f"✗ Excel file not found at {self.file_path}")
            self.df = self._get_sample_data()

    def _get_sample_data(self) -> pd.DataFrame:
        """Return sample data for testing when Excel file is unavailable."""
        return pd.DataFrame({
            'Year': [2020, 2021, 2022, 2023, 2024, 2020, 2021, 2022, 2023, 2024],
            'Area': ['Wakad', 'Wakad', 'Wakad', 'Wakad', 'Wakad', 'Akurdi', 'Akurdi', 'Akurdi', 'Akurdi', 'Akurdi'],
            'Price': [45, 48, 52, 58, 65, 35, 37, 40, 44, 48],
            'Demand': [85, 88, 90, 92, 95, 75, 78, 80, 82, 85],
            'Size': [1200, 1250, 1300, 1400, 1500, 1100, 1150, 1200, 1250, 1300],
        })

    def detect_areas(self, message: str) -> List[str]:
        """
        Detect multiple area names from user message using keyword matching.
        Supports comparison queries like "Compare Area1 and Area2".
        
        Args:
            message: User query message
            
        Returns:
            List of area names found (empty list if none found)
        """
        message_lower = message.lower()
        
        # Get unique areas from data
        if self.df is None or len(self.df) == 0:
            return []
        
        areas = self.df['final location'].unique()
        found_areas = []
        
        # Check for exact or partial matches
        for area in areas:
            if area.lower() in message_lower:
                found_areas.append(area)
        
        return found_areas

    def detect_area(self, message: str) -> str:
        """
        Detect area name from user message using keyword matching.
        
        Args:
            message: User query message
            
        Returns:
            Area name if found, empty string otherwise
        """
        areas = self.detect_areas(message)
        return areas[0] if areas else ""

    def filter_by_area(self, area: str) -> pd.DataFrame:
        """
        Filter data by area name.
        
        Args:
            area: Area name to filter by
            
        Returns:
            Filtered DataFrame
        """
        if self.df is None or area == "":
            return self.df
        
        return self.df[self.df['final location'].str.lower() == area.lower()]

    def get_price_trend(self, area_data: pd.DataFrame) -> Dict[str, List]:
        """
        Extract price trend data for charting.
        
        Args:
            area_data: Filtered DataFrame for specific area
            
        Returns:
            Dictionary with years and prices for chart
        """
        if area_data.empty:
            return {"years": [], "values": []}
        
        trend = area_data[['year', 'flat - weighted average rate']].sort_values('year')
        trend = trend.dropna()
        
        return {
            "years": trend['year'].astype(str).tolist(),
            "values": trend['flat - weighted average rate'].tolist(),
        }

    def get_comparison_trend(self, areas: List[str]) -> Dict[str, Any]:
        """
        Extract comparison data for multiple areas.
        
        Args:
            areas: List of area names to compare
            
        Returns:
            Dictionary with comparison data for charting
        """
        if not areas or self.df is None or self.df.empty:
            return {"years": [], "areas": {}}
        
        # Get years
        years = sorted(self.df['year'].unique())
        
        comparison_data = {
            "years": [str(y) for y in years],
            "areas": {}
        }
        
        # Get data for each area
        for area in areas:
            area_data = self.filter_by_area(area)
            if not area_data.empty:
                trend = area_data[['year', 'flat - weighted average rate']].sort_values('year')
                trend = trend.dropna()
                comparison_data["areas"][area] = trend['flat - weighted average rate'].tolist()
        
        return comparison_data

    def get_summary(self, area: str, area_data: pd.DataFrame) -> str:
        """
        Generate natural language summary for area analysis.
        
        Args:
            area: Area name
            area_data: Filtered DataFrame for specific area
            
        Returns:
            Summary text
        """
        if area_data.empty:
            return f"No data found for {area}."
        
        avg_price = area_data['flat - weighted average rate'].mean()
        total_sales = area_data['flat_sold - igr'].sum()
        total_units = area_data['total units'].sum()
        
        return f"Area: {area} | Avg Rate: ₹{avg_price:,.0f}/sqft | Total Sales: {total_sales} | Units: {total_units}"

    def get_comparison_summary(self, areas: List[str]) -> str:
        """
        Generate summary for comparison of multiple areas.
        
        Args:
            areas: List of area names to compare
            
        Returns:
            Summary text with comparison
        """
        summaries = []
        for area in areas:
            area_data = self.filter_by_area(area)
            if not area_data.empty:
                avg_price = area_data['flat - weighted average rate'].mean()
                summaries.append(f"{area}: ₹{avg_price:,.0f}/sqft")
        
        return " | ".join(summaries) if summaries else "No data found for comparison."

    def _format_table_as_text(self, area_data: pd.DataFrame) -> str:
        """
        Format DataFrame rows as readable text for LLM prompt.
        
        Args:
            area_data: Filtered DataFrame for specific area
            
        Returns:
            Formatted text representation of the data
        """
        if area_data.empty:
            return "No data available."
        
        text_lines = []
        for idx, row in area_data.iterrows():
            year = int(row['year'])
            price = row['flat - weighted average rate']
            sales = row['flat_sold - igr']
            units = row['total units']
            text_lines.append(
                f"Year {year}: Price ₹{price:,.0f}/sqft, "
                f"Sales {sales}, Units {units}"
            )
        
        return "\n".join(text_lines)

    def _generate_analytical_summary(self, area: str, area_data: pd.DataFrame) -> str:
        """
        Generate a sophisticated summary by analyzing data patterns.
        This provides LLM-quality insights without requiring external API.
        """
        if area_data.empty:
            return f"No data available for {area}."
        
        # Extract key metrics
        prices = area_data['flat - weighted average rate'].astype(float)
        sales = area_data['flat_sold - igr'].astype(float)
        years = area_data['year'].astype(int)
        
        # Calculate trends
        price_trend = ((prices.iloc[-1] - prices.iloc[0]) / prices.iloc[0] * 100) if len(prices) > 1 else 0
        sales_trend = ((sales.iloc[-1] - sales.iloc[0]) / sales.iloc[0] * 100) if len(sales) > 1 else 0
        
        # Get price range
        min_price = prices.min()
        max_price = prices.max()
        avg_price = prices.mean()
        
        # Total transactions
        total_sales = sales.sum()
        avg_sales_per_year = sales.mean()
        
        # Year range
        start_year = years.min()
        end_year = years.max()
        
        # Generate insights
        price_direction = "upward" if price_trend > 0 else "downward"
        price_magnitude = f"{abs(price_trend):.1f}%"
        
        sales_direction = "increased" if sales_trend > 0 else "decreased"
        sales_magnitude = f"{abs(sales_trend):.1f}%"
        
        # Volatility assessment
        price_volatility = prices.std() / prices.mean() * 100 if prices.mean() > 0 else 0
        volatility_desc = "stable" if price_volatility < 10 else "moderate" if price_volatility < 20 else "volatile"
        
        # Build comprehensive summary
        summary_lines = [
            f"{area} real estate market analysis ({start_year}-{end_year}):",
            f"Average rate: Rs {avg_price:,.0f}/sqft with {price_direction} trend of {price_magnitude}. Price range: Rs {min_price:,.0f} to Rs {max_price:,.0f}/sqft.",
            f"Transaction activity: {total_sales:.0f} units sold ({sales_direction} by {sales_magnitude}). {volatility_desc.capitalize()} market with {price_volatility:.1f}% price volatility.",
        ]
        
        return " ".join(summary_lines)

    def generate_llm_summary(self, area: str, area_data: pd.DataFrame) -> str:
        """
        Generate LLM-powered summary using HuggingFace Inference API.
        Falls back to analytical summary on error.
        
        Args:
            area: Area name
            area_data: Filtered DataFrame for specific area
            
        Returns:
            LLM-generated summary string
        """
        if area_data.empty:
            return f"No data available for {area}."
        
        # Get HuggingFace API key from environment
        api_key = settings.HUGGINGFACE_API_KEY
        if not api_key:
            logger.warning("HuggingFace API key not found, using fallback summary")
            return self.get_summary(area, area_data)
        
        # Format data for LLM prompt
        table_text = self._format_table_as_text(area_data)
        
        # Build prompt following the template
        prompt = f"""Write a concise real-estate analysis summary (5-8 lines) for the locality '{area}' using the following dataset. Focus on price trend, demand trend, growth patterns, and any notable changes.

Data:
{table_text}

Summary:"""
        
        try:
            # Call HuggingFace Inference API
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 150,
                    "temperature": 0.7,
                    "top_p": 0.95,
                }
            }
            
            # Use a reliable model with HuggingFace Inference API
            # Note: Mistral-7B might require private deployment, so we use a more accessible model
            # You can replace with any model ID available in HuggingFace's inference API
            model_name = "mistralai/Mistral-7B-Instruct-v0.1"
            
            # Try with inference endpoint
            url = f"https://api-inference.huggingface.co/models/{model_name}"
            
            print(f"[LLM] Calling HuggingFace API ({model_name}) for {area}...")
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=30
            )
            
            # Check response status
            if response.status_code == 200:
                result = response.json()
                
                # Extract generated text
                if isinstance(result, list) and len(result) > 0:
                    generated_text = result[0].get('generated_text', '')
                    # Remove the prompt from the response
                    summary = generated_text.replace(prompt, '').strip()
                    print(f"[LLM] Summary generated for {area}")
                    return summary if summary else self._generate_analytical_summary(area, area_data)
                else:
                    print(f"[LLM] Unexpected HF response format: {result}")
                    return self._generate_analytical_summary(area, area_data)
            
            elif response.status_code == 410:
                print(f"[LLM] HuggingFace API endpoint deprecated (410), using analytical summary")
                return self._generate_analytical_summary(area, area_data)
            
            elif response.status_code == 503:
                print(f"[LLM] HuggingFace model is loading, using analytical summary")
                return self._generate_analytical_summary(area, area_data)
            
            else:
                print(f"[LLM] HF API error {response.status_code}: {response.text[:200]}")
                return self._generate_analytical_summary(area, area_data)
        
        except requests.exceptions.Timeout:
            print(f"[LLM] HuggingFace API timeout for {area}, using analytical summary")
            return self._generate_analytical_summary(area, area_data)
        
        except requests.exceptions.RequestException as e:
            print(f"[LLM] HuggingFace API error: {str(e)}, using analytical summary")
            return self._generate_analytical_summary(area, area_data)
        
        except Exception as e:
            print(f"[LLM] Unexpected error generating summary: {str(e)}")
            return self._generate_analytical_summary(area, area_data)

    def get_table_data(self, area_data: pd.DataFrame) -> List[Dict[str, Any]]:
        """
        Convert DataFrame to list of dictionaries for JSON response.
        
        Args:
            area_data: Filtered DataFrame for specific area
            
        Returns:
            List of row dictionaries
        """
        if area_data.empty:
            return []
        
        # Sort by year
        area_data = area_data.sort_values('year')
        
        # Select key columns for display
        display_cols = ['year', 'final location', 'flat_sold - igr', 'flat - weighted average rate', 'total units']
        available_cols = [col for col in display_cols if col in area_data.columns]
        
        return area_data[available_cols].to_dict('records')

    def analyze_query(self, message: str) -> Dict[str, Any]:
        """
        Complete analysis pipeline for user query.
        Supports single area analysis and comparison of multiple areas.
        Uses LLM-powered summaries via HuggingFace API.
        
        Args:
            message: User query message
            
        Returns:
            Dictionary with LLM summary, chart data, and table
        """
        # Detect areas
        areas = self.detect_areas(message)
        
        # Check if it's a comparison query
        is_comparison = len(areas) > 1 or 'compare' in message.lower()
        
        if is_comparison and len(areas) > 1:
            # Handle comparison mode
            result = {
                "type": "comparison",
                "areas": areas,
                "summary": self.get_comparison_summary(areas),
                "chart": self.get_comparison_trend(areas),
                "tables": {}
            }
            
            # Add individual tables for each area
            for area in areas:
                area_data = self.filter_by_area(area)
                result["tables"][area] = self.get_table_data(area_data)
        else:
            # Single area analysis - Use LLM-powered summary
            area = areas[0] if areas else ""
            area_data = self.filter_by_area(area) if area else pd.DataFrame()
            
            # Generate LLM summary instead of static summary
            llm_summary = self.generate_llm_summary(area, area_data)
            
            result = {
                "type": "single",
                "area": area,
                "summary": llm_summary,  # Now LLM-powered!
                "chart": self.get_price_trend(area_data),
                "table": self.get_table_data(area_data),
            }
        
        return result
