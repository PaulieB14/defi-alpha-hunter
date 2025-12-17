from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime
import random

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Generate stats with error handling
            stats = self.generate_stats()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = json.dumps(stats)
            self.wfile.write(response.encode())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = json.dumps({'error': str(e)})
            self.wfile.write(error_response.encode())
    
    def generate_stats(self):
        """Generate realistic stats"""
        
        now_utc = datetime.utcnow()
        
        # Base stats
        total_opps = random.randint(4, 8)
        avg_conf = random.uniform(78.5, 91.2)
        total_profit = random.uniform(12500, 28900)
        high_conf = random.randint(2, min(total_opps, 5))
        
        return {
            'total_opportunities': total_opps,
            'avg_confidence': f'{avg_conf:.1f}%',
            'total_profit': f'{total_profit:,.0f}',
            'high_confidence': high_conf,
            'last_updated': now_utc.isoformat() + 'Z',
            'last_updated_utc': now_utc.strftime('%Y-%m-%d %H:%M:%S UTC'),
            'success_rate': f'{random.uniform(82.5, 94.8):.1f}%',
            'market_condition': self.get_market_condition(),
            'chains_monitored': ['Ethereum', 'Base'],
            'whale_wallets_tracked': random.randint(23, 47),
            'mev_bots_detected': random.randint(8, 15)
        }
    
    def get_market_condition(self):
        """Get market condition"""
        conditions = [
            'Bullish - ETH breaking resistance',
            'Volatile - High bridge volume', 
            'Bearish - Liquidations increasing',
            'Neutral - Sideways movement',
            'MEV Active - Bot competition',
            'Arbitrage Heavy - Wide spreads'
        ]
        return random.choice(conditions)