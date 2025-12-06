"""
REST API views for real estate chatbot.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from .services import RealEstateService
from .serializers import QueryRequestSerializer, QueryResponseSerializer


# Initialize service (singleton pattern)
service = RealEstateService()


class QueryView(APIView):
    """
    API endpoint for processing real estate queries.
    
    POST /api/query
    - Accepts user message
    - Returns summary, chart data, and filtered table
    """

    def post(self, request, *args, **kwargs):
        """
        Process user query and return analysis results.
        
        Request body:
        {
            "message": "Analyze Wakad"
        }
        
        Response:
        {
            "area": "Wakad",
            "summary": "...",
            "chart": {"years": [...], "values": [...]},
            "table": [...]
        }
        """
        # Validate input
        serializer = QueryRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"error": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Get user message
        message = serializer.validated_data['message']

        try:
            # Perform analysis
            result = service.analyze_query(message)

            # Validate output
            response_serializer = QueryResponseSerializer(result)
            
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                {"error": f"Analysis failed: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class DebugView(APIView):
    """Debug endpoint to verify LLM integration."""
    
    def get(self, request):
        """Check HuggingFace API key and LLM configuration."""
        api_key = settings.HUGGINGFACE_API_KEY
        is_configured = bool(api_key and len(api_key) > 10)
        
        # Test with sample data
        test_data = service.filter_by_area("Akurdi")
        
        return Response({
            "status": "OK",
            "api_key_configured": is_configured,
            "api_key_preview": f"{api_key[:10]}...{api_key[-5:]}" if api_key else "NOT SET",
            "sample_data_rows": len(test_data),
            "test_llm": "Available" if is_configured else "Not Available"
        })
    
    def post(self, request):
        """Test LLM summary generation directly."""
        import sys
        try:
            area = request.data.get("area", "Akurdi")
            area_data = service.filter_by_area(area)
            
            if area_data.empty:
                return Response({"error": f"No data for area: {area}"}, status=400)
            
            # Capture what happens during LLM call
            import io
            from contextlib import redirect_stdout, redirect_stderr
            
            f_out = io.StringIO()
            f_err = io.StringIO()
            
            with redirect_stdout(f_out), redirect_stderr(f_err):
                # Generate LLM summary
                summary = service.generate_llm_summary(area, area_data)
            
            output = f_out.getvalue()
            errors = f_err.getvalue()
            
            return Response({
                "area": area,
                "summary": summary,
                "data_rows": len(area_data),
                "debug_output": output,
                "debug_errors": errors
            })
        except Exception as e:
            import traceback
            return Response({
                "error": str(e),
                "traceback": traceback.format_exc()
            }, status=500)


