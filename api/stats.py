from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Generate demo stats for Vercel deployment
        stats = {
            'total_opportunities': 4,
            'avg_confidence': '84.5%',
            'total_profit': '15,800',
            'high_confidence': 3,
            'last_updated': datetime.now().isoformat()
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = json.dumps(stats)
        self.wfile.write(response.encode())