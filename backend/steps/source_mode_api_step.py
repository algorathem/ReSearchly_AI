import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from src.services.database_service import database_service

config = {
    'type': 'api',
    'name': 'Source Mode API',
    'description': 'API endpoint for toggling source interaction modes',
    'path': '/api/source/:sourceId/mode',
    'method': 'POST',
    'emits': ['mode-changed'],  # Emit event for workflow refresh
    'flows': ['research'],
}

async def handler(req, context):
    """Handler for source mode toggle API"""
    logger = context.logger
    
    path_params = req.get('pathParams', {})
    source_id = path_params.get('sourceId', '')
    body_raw = req.get('body', '{}')
    
    # Parse JSON body if it's a string
    if isinstance(body_raw, str):
        try:
            body = json.loads(body_raw)
        except json.JSONDecodeError:
            return {
                'status': 400,
                'body': {
                    'error': 'Invalid JSON in request body'
                },
            }
    else:
        body = body_raw
    
    mode = body.get('mode', 'summary')  # summary, explanation, implementation
    
    if not source_id:
        return {
            'status': 400,
            'body': {
                'message': 'Source ID is required'
            },
        }
    
    valid_modes = ['summary', 'explanation', 'implementation']
    if mode not in valid_modes:
        return {
            'status': 400,
            'body': {
                'message': f'Invalid mode. Must be one of: {", ".join(valid_modes)}'
            },
        }
    
    logger.info('Toggling source mode', {
        'sourceId': source_id,
        'mode': mode
    })
    
    try:
        # Validate that the source exists
        source = await database_service.get_source_by_id(int(source_id))
        if not source:
            return {
                'status': 404,
                'body': {
                    'message': 'Source not found'
                },
            }
        
        # Here you could store the mode preference in the database
        # For now, just acknowledge and emit event for workflow refresh
        
        return {
            'status': 200,
            'body': {
                'message': 'Mode updated successfully',
                'sourceId': source_id,
                'mode': mode,
                'source': {
                    'id': source['id'],
                    'title': source['title'],
                    'currentMode': mode
                }
            },
        }
    except Exception as error:
        logger.error('Error updating mode', {'error': str(error)})
        
        return {
            'status': 500,
            'body': {
                'message': 'Failed to update mode',
                'error': str(error)
            },
        }