from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime
import random

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Generate more dynamic stats that change over time
        stats = self.generate_dynamic_stats()
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = json.dumps(stats)
        self.wfile.write(response.encode())
    
    def generate_dynamic_stats(self):
        """Generate realistic stats that vary over time"""
        
        # Base stats with some randomness to simulate real-time changes
        total_opps = random.randint(4, 8)
        avg_conf = random.uniform(78.5, 91.2)
        total_profit = random.uniform(12500, 28900)
        high_conf = random.randint(2, min(total_opps, 5))
        
        # Add some time-based variation
        hour = datetime.now().hour
        
        # Higher activity during US/EU trading hours
        if 8 <= hour <= 22:
            total_opps += random.randint(1, 3)
            total_profit *= random.uniform(1.1, 1.4)
        
        # Weekend adjustments
        if datetime.now().weekday() >= 5:  # Weekend
            total_opps = max(2, total_opps - random.randint(1, 2))
            avg_conf *= random.uniform(0.9, 0.95)
        
        return {
            'total_opportunities': total_opps,
            'avg_confidence': f'{avg_conf:.1f}%',
            'total_profit': f'{total_profit:,.0f}',
            'high_confidence': high_conf,
            'last_updated': datetime.now().isoformat(),
            'market_conditions': self.get_market_condition(),
            'active_chains': random.randint(2, 4),
            'success_rate': f'{random.uniform(82.5, 94.8):.1f}%'
        }
    
    def get_market_condition(self):
        """Generate realistic market condition"""
        conditions = [
            'Bullish - High Volatility',
            'Neutral - Moderate Activity', 
            'Bearish - Liquidation Risk',
            'Sideways - Range Bound',
            'Volatile - High Opportunity'
        ]
        
        # Weight conditions based on time (simulate market cycles)
        hour = datetime.now().hour
        if 14 <= hour <= 16:  # US market open
            return random.choice(['Bullish - High Volatility', 'Volatile - High Opportunity'])
        elif 22 <= hour or hour <= 2:  # Asian markets
            return random.choice(['Neutral - Moderate Activity', 'Sideways - Range Bound'])
        else:
            return random.choice(conditions)