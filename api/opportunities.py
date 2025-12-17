from http.server import BaseHTTPRequestHandler
import json
import urllib.request
import urllib.error
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Get real blockchain data with fallbacks
            opportunities = self.get_real_opportunities()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = json.dumps(opportunities)
            self.wfile.write(response.encode())
        except Exception as e:
            # Return error with debug info
            self.send_response(200)  # Still return 200 to avoid frontend errors
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            error_opportunities = [{
                'type': 'API_CONNECTION_ERROR',
                'chain': 'System',
                'confidence': 0.0,
                'profit_potential': 0.0,
                'description': f'Unable to fetch live data: {str(e)}',
                'action': 'Retrying connection to blockchain APIs...',
                'timestamp': datetime.utcnow().isoformat() + 'Z',
                'data': {
                    'error_type': type(e).__name__,
                    'error_message': str(e),
                    'status': 'Attempting to reconnect'
                }
            }]
            
            response = json.dumps(error_opportunities)
            self.wfile.write(response.encode())
    
    def fetch_url(self, url, timeout=3):
        """Simple URL fetcher with timeout"""
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (compatible; DeFiAlphaHunter/1.0)')
            
            with urllib.request.urlopen(req, timeout=timeout) as response:
                if response.status == 200:
                    return json.loads(response.read().decode())
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")
        return None
    
    def get_real_opportunities(self):
        """Get real opportunities with multiple fallback strategies"""
        opportunities = []
        
        # Try to get real ETH price data
        eth_data = self.get_eth_price_data()
        if eth_data:
            opportunities.extend(self.create_eth_opportunities(eth_data))
        
        # Try to get DeFi data
        defi_opportunities = self.get_defi_opportunities()
        opportunities.extend(defi_opportunities)
        
        # If we have no real data, create status opportunity
        if not opportunities:
            opportunities = self.create_fallback_opportunities()
        
        return opportunities[:6]
    
    def get_eth_price_data(self):
        """Get ETH price with multiple API fallbacks"""
        # Try CoinGecko first
        coingecko_url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd&include_24hr_change=true'
        data = self.fetch_url(coingecko_url)
        
        if data and 'ethereum' in data:
            return {
                'price': data['ethereum']['usd'],
                'change_24h': data['ethereum'].get('usd_24h_change', 0),
                'source': 'CoinGecko'
            }
        
        # Fallback: Try CoinCap API
        coincap_url = 'https://api.coincap.io/v2/assets/ethereum'
        data = self.fetch_url(coincap_url)
        
        if data and 'data' in data:
            return {
                'price': float(data['data']['priceUsd']),
                'change_24h': float(data['data'].get('changePercent24Hr', 0)),
                'source': 'CoinCap'
            }
        
        return None
    
    def create_eth_opportunities(self, eth_data):
        """Create opportunities based on real ETH data"""
        opportunities = []
        
        price = eth_data['price']
        change_24h = eth_data['change_24h']
        source = eth_data['source']
        
        # Real volatility opportunity
        if abs(change_24h) > 1:  # >1% movement
            direction = 'up' if change_24h > 0 else 'down'
            opportunities.append({
                'type': 'ETH_PRICE_MOVEMENT',
                'chain': 'Ethereum',
                'confidence': min(0.9, abs(change_24h) / 10),
                'profit_potential': abs(change_24h) / 100 * 0.3,
                'description': f'ETH moved {direction} {abs(change_24h):.1f}% to ${price:,.0f} - momentum opportunity detected',
                'action': f'Trade ETH momentum - current price ${price:,.0f}',
                'timestamp': datetime.utcnow().isoformat() + 'Z',
                'data': {
                    'current_price': f'${price:,.0f}',
                    'price_change_24h': f'{change_24h:+.1f}%',
                    'data_source': f'{source} API (Live)',
                    'opportunity_type': 'Real Market Movement'
                }
            })
        
        # Price level opportunity
        if price > 4000:
            opportunities.append({
                'type': 'ETH_RESISTANCE_BREAK',
                'chain': 'Ethereum',
                'confidence': 0.75,
                'profit_potential': 0.05,
                'description': f'ETH above $4k resistance at ${price:,.0f} - breakout continuation possible',
                'action': 'Monitor for sustained break above $4,000 level',
                'timestamp': datetime.utcnow().isoformat() + 'Z',
                'data': {
                    'resistance_level': '$4,000',
                    'current_price': f'${price:,.0f}',
                    'data_source': f'{source} API (Live)'
                }
            })
        elif price < 3500:
            opportunities.append({
                'type': 'ETH_SUPPORT_TEST',
                'chain': 'Ethereum',
                'confidence': 0.68,
                'profit_potential': 0.08,
                'description': f'ETH testing support at ${price:,.0f} - potential bounce opportunity',
                'action': 'Watch for bounce from $3,500 support level',
                'timestamp': datetime.utcnow().isoformat() + 'Z',
                'data': {
                    'support_level': '$3,500',
                    'current_price': f'${price:,.0f}',
                    'data_source': f'{source} API (Live)'
                }
            })
        
        return opportunities
    
    def get_defi_opportunities(self):
        """Get DeFi opportunities from available APIs"""
        opportunities = []
        
        # Try to get DeFi TVL data
        tvl_data = self.get_defi_tvl_data()
        if tvl_data:
            opportunities.extend(self.create_defi_opportunities(tvl_data))
        
        return opportunities
    
    def get_defi_tvl_data(self):
        """Get DeFi TVL data from DeFiLlama"""
        # Try DeFiLlama protocols endpoint
        url = 'https://api.llama.fi/protocols'
        data = self.fetch_url(url, timeout=5)
        
        if data and isinstance(data, list):
            # Filter for major protocols
            major_protocols = []
            for protocol in data[:20]:  # Check first 20
                if isinstance(protocol, dict) and protocol.get('tvl', 0) > 100000000:  # >$100M
                    major_protocols.append(protocol)
            
            return major_protocols[:5] if major_protocols else None
        
        return None
    
    def create_defi_opportunities(self, protocols):
        """Create opportunities from real DeFi protocol data"""
        opportunities = []
        
        for protocol in protocols[:3]:  # Top 3 protocols
            name = protocol.get('name', 'Unknown')
            tvl = protocol.get('tvl', 0)
            change_1d = protocol.get('change_1d', 0)
            
            if abs(change_1d) > 5:  # >5% TVL change
                direction = 'increased' if change_1d > 0 else 'decreased'
                opportunities.append({
                    'type': 'DEFI_TVL_MOVEMENT',
                    'chain': 'Multiple',
                    'confidence': min(0.85, abs(change_1d) / 20),
                    'profit_potential': abs(change_1d) / 100 * 0.2,
                    'description': f'{name} TVL {direction} {abs(change_1d):.1f}% to ${tvl/1e9:.1f}B - protocol momentum shift',
                    'action': f'Monitor {name} for continued TVL movement',
                    'timestamp': datetime.utcnow().isoformat() + 'Z',
                    'data': {
                        'protocol': name,
                        'current_tvl': f'${tvl/1e9:.1f}B',
                        'tvl_change_1d': f'{change_1d:+.1f}%',
                        'data_source': 'DeFiLlama API (Live)'
                    }
                })
        
        return opportunities
    
    def create_fallback_opportunities(self):
        """Create opportunities when APIs are unavailable"""
        return [{
            'type': 'SYSTEM_STATUS',
            'chain': 'System',
            'confidence': 0.5,
            'profit_potential': 0.0,
            'description': 'Connecting to live blockchain data sources - real opportunities loading...',
            'action': 'Refresh in a few seconds for live market data',
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'data': {
                'status': 'Connecting to APIs',
                'attempted_sources': ['CoinGecko', 'CoinCap', 'DeFiLlama'],
                'next_attempt': 'Automatic refresh in 30 seconds'
            }
        }]