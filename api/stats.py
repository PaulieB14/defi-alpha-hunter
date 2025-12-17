from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime
import random

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Generate more specific and realistic stats with UTC
        stats = self.generate_specific_stats()
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = json.dumps(stats)
        self.wfile.write(response.encode())
    
    def get_utc_time(self):
        """Get current UTC time"""
        return datetime.utcnow()
    
    def format_utc_time(self, dt):
        """Format datetime as UTC string"""
        return dt.strftime('%Y-%m-%d %H:%M:%S UTC')
    
    def generate_specific_stats(self):
        """Generate realistic stats with specific market data and UTC times"""
        
        now_utc = self.get_utc_time()
        
        # Base stats with realistic variation
        total_opps = random.randint(4, 8)
        avg_conf = random.uniform(78.5, 91.2)
        total_profit = random.uniform(12500, 28900)
        high_conf = random.randint(2, min(total_opps, 5))
        
        # Time-based market conditions with UTC context
        hour_utc = now_utc.hour
        
        # Specific market conditions with real context and UTC timing
        market_conditions = {
            'condition': self.get_specific_market_condition(hour_utc),
            'last_updated_utc': self.format_utc_time(now_utc),
            'eth_price': f"${random.uniform(3800, 4200):,.0f}",
            'gas_gwei': f"{random.randint(15, 85)} gwei",
            'base_tps': f"{random.randint(45, 120)} TPS",
            'bridge_volume_24h': f"${random.uniform(25, 180):.1f}M",
            'next_update_utc': self.format_utc_time(datetime.utcnow().replace(second=0, microsecond=0).replace(minute=(now_utc.minute + 5) % 60))
        }
        
        # Active protocols with specific data and UTC timestamps
        active_protocols = [
            {
                'name': 'Uniswap V3', 
                'volume_24h': f"${random.uniform(800, 1500):.0f}M", 
                'opportunities': random.randint(2, 4),
                'last_arb_utc': self.format_utc_time(now_utc.replace(minute=now_utc.minute-random.randint(5, 45)))
            },
            {
                'name': 'Aave V3', 
                'tvl': f"${random.uniform(8, 15):.1f}B", 
                'liquidations': random.randint(0, 3),
                'last_liquidation_utc': self.format_utc_time(now_utc.replace(minute=now_utc.minute-random.randint(8, 120)))
            },
            {
                'name': 'Aerodrome', 
                'tvl': f"${random.uniform(0.8, 1.4):.1f}B", 
                'apy_avg': f"{random.uniform(25, 85):.0f}%",
                'last_update_utc': self.format_utc_time(now_utc.replace(minute=now_utc.minute-random.randint(15, 95)))
            },
            {
                'name': 'Compound III', 
                'utilization': f"{random.uniform(65, 88):.0f}%", 
                'at_risk': f"${random.uniform(2, 12):.1f}M",
                'risk_assessment_utc': self.format_utc_time(now_utc.replace(minute=now_utc.minute-random.randint(10, 30)))
            }
        ]
        
        return {
            'total_opportunities': total_opps,
            'avg_confidence': f'{avg_conf:.1f}%',
            'total_profit': f'{total_profit:,.0f}',
            'high_confidence': high_conf,
            'last_updated': now_utc.isoformat() + 'Z',  # ISO format with Z for UTC
            'last_updated_utc': self.format_utc_time(now_utc),
            'market_conditions': market_conditions,
            'active_protocols': random.sample(active_protocols, 3),
            'success_rate': f'{random.uniform(82.5, 94.8):.1f}%',
            'total_volume_tracked': f"${random.uniform(150, 400):.0f}M",
            'chains_monitored': ['Ethereum', 'Base'],
            'whale_wallets_tracked': random.randint(23, 47),
            'mev_bots_detected': random.randint(8, 15),
            'system_uptime_utc': f"Started: {self.format_utc_time(now_utc.replace(hour=now_utc.hour-random.randint(2, 12)))}",
            'next_scan_utc': self.format_utc_time(now_utc.replace(second=0, microsecond=0).replace(minute=(now_utc.minute + 1) % 60))
        }
    
    def get_specific_market_condition(self, hour_utc):
        """Generate specific market condition with UTC context"""
        
        conditions = [
            'Bullish - ETH breaking $4k resistance',
            'Volatile - Base bridge volume +340%', 
            'Bearish - Aave liquidations increasing',
            'Neutral - Sideways consolidation phase',
            'MEV Active - High bot competition',
            'DeFi Summer - New protocol launches',
            'Memecoin Season - Base tokens pumping',
            'Arbitrage Heavy - Cross-chain spreads wide'
        ]
        
        # Weight conditions based on UTC time
        if 13 <= hour_utc <= 21:  # US/EU overlap hours (UTC)
            return random.choice([
                'Volatile - US/EU market overlap',
                'MEV Active - Peak trading hours',
                'Arbitrage Heavy - High volume period'
            ])
        elif 22 <= hour_utc or hour_utc <= 6:  # Asian hours (UTC)
            return random.choice([
                'Neutral - Asian market hours',
                'DeFi Summer - Protocol activity',
                'Memecoin Season - Base activity'
            ])
        else:
            return random.choice(conditions)