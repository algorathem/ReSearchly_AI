import sys
import os
sys.path.insert(0, os.getcwd())

from steps.source_mode_api_step import handler
import asyncio

async def test_handler():
    # Test valid mode
    req = {
        'pathParams': {'sourceId': '1'},
        'body': {
            'mode': 'summary'
        }
    }

    # Mock context
    class MockLogger:
        def info(self, msg, data=None):
            print(f"INFO: {msg}", data or "")
        def error(self, msg, data=None):
            print(f"ERROR: {msg}", data or "")

    class MockContext:
        def __init__(self):
            self.logger = MockLogger()

    context = MockContext()

    print("=== Testing Valid Mode ===")
    try:
        result = await handler(req, context)
        print("Handler result:")
        print(f"Status: {result['status']}")
        print(f"Message: {result['body']['message']}")
        if 'source' in result['body']:
            print(f"Source: {result['body']['source']}")
    except Exception as e:
        print(f"Handler failed: {e}")
        import traceback
        traceback.print_exc()

    print("\n=== Testing Invalid Mode ===")
    # Test invalid mode
    req_invalid = {
        'pathParams': {'sourceId': '1'},
        'body': {
            'mode': 'invalid_mode'
        }
    }

    try:
        result = await handler(req_invalid, context)
        print("Handler result:")
        print(f"Status: {result['status']}")
        print(f"Message: {result['body']['message']}")
    except Exception as e:
        print(f"Handler failed: {e}")

    print("\n=== Testing Non-existent Source ===")
    # Test non-existent source
    req_missing = {
        'pathParams': {'sourceId': '999'},
        'body': {
            'mode': 'summary'
        }
    }

    try:
        result = await handler(req_missing, context)
        print("Handler result:")
        print(f"Status: {result['status']}")
        print(f"Message: {result['body']['message']}")
    except Exception as e:
        print(f"Handler failed: {e}")

if __name__ == "__main__":
    asyncio.run(test_handler())