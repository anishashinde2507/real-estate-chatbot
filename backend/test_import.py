#!/usr/bin/env python
# Test if services module imports correctly
try:
    from api.services import RealEstateService
    print("SUCCESS: Services module imports OK")
    service = RealEstateService()
    print(f"SUCCESS: Service initialized, data loaded")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
