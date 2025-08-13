"""
Ultra-minimal SentinelAgents handler - NO EXTERNAL DEPENDENCIES
ARM64 compatible, no Pydantic, pure Python stdlib
"""
import json
import os
from datetime import datetime, timezone

def lambda_handler(event, context):
    """ARM64 compatible minimal handler"""
    
    try:
        # Pure Python stdlib response
        response_data = {
            'message': 'SentinelAgents Agentic - ARM64 Minimal',
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'version': '1.0.0-arm64-minimal',
            'stage': os.environ.get('AWS_STAGE', 'dev'),
            'architecture': 'ARM64',
            'runtime': 'python3.11',
            'dependencies': 'none',
            'size_mb': '<1MB'
        }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type,Authorization'
            },
            'body': json.dumps(response_data, indent=2)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }
