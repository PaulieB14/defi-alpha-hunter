from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime, timedelta
import random

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Generate more dynamic and varied opportunities
        opportunities = self.generate_dynamic_opportunities()
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = json.dumps(opportunities)
        self.wfile.write(response.encode())
    
    def generate_dynamic_opportunities(self):
        """Generate dynamic opportunities that change over time"""
        
        # Base opportunities pool
        opportunity_templates = [
            {
                'type': 'CROSS_CHAIN_ARBITRAGE',
                'chain': 'ETH → Base',
                'descriptions': [
                    'USDC price difference detected between Ethereum and Base Uniswap pools',
                    'ETH trading at premium on Base - arbitrage opportunity available',
                    'WBTC price gap between chains creating profit window',
                    'Stablecoin depeg creating cross-chain arbitrage opportunity'
                ],
                'actions': [
                    'Buy USDC on Base, sell on Ethereum mainnet',
                    'Bridge ETH to Base, sell at premium',
                    'Execute WBTC arbitrage via official bridge',
                    'Capitalize on stablecoin price difference'
                ]
            },
            {
                'type': 'BASE_WHALE_SIGNAL',
                'chain': 'Base',
                'descriptions': [
                    'Large wallet (>$10M) accumulating ETH on Base before bridge activity',
                    'Whale address showing unusual DeFi protocol interaction patterns',
                    'Major holder increasing Base ecosystem token positions',
                    'Smart money flowing into Base-native yield farming protocols'
                ],
                'actions': [
                    'Follow whale strategy - accumulate ETH on Base',
                    'Monitor whale DeFi moves for alpha signals',
                    'Copy whale Base ecosystem positioning',
                    'Enter yield farming positions ahead of whale activity'
                ]
            },
            {
                'type': 'ETH_LIQUIDATION_CASCADE',
                'chain': 'Ethereum',
                'descriptions': [
                    'Aave liquidations creating selling pressure - potential bounce opportunity',
                    'Compound liquidation cascade detected - oversold conditions likely',
                    'Large leveraged positions approaching liquidation thresholds',
                    'DeFi protocol liquidations creating temporary price depression'
                ],
                'actions': [
                    'Prepare to buy ETH dip from liquidation cascade',
                    'Set limit orders below current liquidation levels',
                    'Monitor for oversold bounce after liquidation wave',
                    'Position for recovery after forced selling ends'
                ]
            },
            {
                'type': 'BASE_ECOSYSTEM_PLAY',
                'chain': 'Base',
                'descriptions': [
                    'New DeFi protocol launching on Base with high TVL growth',
                    'Base-native token showing unusual accumulation patterns',
                    'Aerodrome seeing significant liquidity increases',
                    'Base bridge volume spiking - ecosystem growth signal'
                ],
                'actions': [
                    'Early liquidity provision opportunity',
                    'Accumulate Base ecosystem tokens before breakout',
                    'Provide liquidity to high-yield Aerodrome pools',
                    'Position for Base ecosystem expansion'
                ]
            },
            {
                'type': 'LIQUIDATION_MEV',
                'chain': 'Ethereum',
                'descriptions': [
                    'MEV opportunity: Liquidation bot competition creating inefficiencies',
                    'Flash loan liquidation setup with guaranteed profit margin',
                    'Undercollateralized positions ready for profitable liquidation',
                    'Liquidation sandwich opportunity in DeFi protocols'
                ],
                'actions': [
                    'Execute MEV liquidation strategy',
                    'Deploy flash loan liquidation bot',
                    'Capture liquidation bonus before other bots',
                    'Sandwich liquidation transactions for extra profit'
                ]
            },
            {
                'type': 'TOKEN_LAUNCH_SNIPE',
                'chain': 'Base',
                'descriptions': [
                    'New token launch detected on Base - early entry opportunity',
                    'Coinbase Ventures-backed project launching on Base today',
                    'High-profile DeFi fork launching with liquidity incentives',
                    'Base-native memecoin showing viral social media traction'
                ],
                'actions': [
                    'Snipe token launch for early allocation',
                    'Enter before major CEX listings',
                    'Provide initial liquidity for launch rewards',
                    'Ride viral momentum with tight stop-loss'
                ]
            }
        ]
        
        # Generate 4-6 random opportunities
        num_opportunities = random.randint(4, 6)
        selected_opportunities = []
        
        for i in range(num_opportunities):
            template = random.choice(opportunity_templates)
            
            # Add some randomness to make it feel more dynamic
            confidence = random.uniform(0.65, 0.95)
            profit_potential = random.uniform(0.015, 0.08)
            
            # Select random description and action
            description = random.choice(template['descriptions'])
            action = random.choice(template['actions'])
            
            # Generate realistic data
            data = self.generate_realistic_data(template['type'])
            
            opportunity = {
                'type': template['type'],
                'chain': template['chain'],
                'confidence': round(confidence, 3),
                'profit_potential': round(profit_potential, 4),
                'description': description,
                'action': action,
                'timestamp': datetime.now().isoformat(),
                'data': data
            }
            
            selected_opportunities.append(opportunity)
        
        # Sort by confidence (highest first)
        selected_opportunities.sort(key=lambda x: x['confidence'], reverse=True)
        
        return selected_opportunities
    
    def generate_realistic_data(self, opp_type):
        """Generate realistic supporting data for each opportunity type"""
        
        if opp_type == 'CROSS_CHAIN_ARBITRAGE':
            return {
                'price_diff': f"{random.uniform(1.2, 4.8):.1f}%",
                'volume': f"${random.uniform(0.8, 5.2):.1f}M",
                'gas_cost': f"${random.randint(15, 85)}",
                'bridge_time': f"{random.randint(3, 12)} min"
            }
        
        elif opp_type == 'BASE_WHALE_SIGNAL':
            return {
                'wallet_size': f"${random.uniform(8.5, 45.2):.1f}M",
                'accumulation': f"{random.randint(150, 850)} ETH",
                'timeframe': f"{random.randint(2, 8)} hours",
                'confidence_score': f"{random.randint(78, 94)}%"
            }
        
        elif opp_type == 'ETH_LIQUIDATION_CASCADE':
            return {
                'liquidation_volume': f"${random.uniform(2.1, 8.7):.1f}M",
                'support_level': f"${random.randint(3750, 4200)}",
                'at_risk': f"${random.uniform(12.5, 35.8):.1f}M",
                'timeframe': f"{random.randint(15, 45)} min"
            }
        
        elif opp_type == 'BASE_ECOSYSTEM_PLAY':
            protocols = ['Aerodrome', 'BaseSwap', 'Moonwell', 'Seamless', 'Extra Finance']
            return {
                'protocol': random.choice(protocols),
                'tvl_growth': f"+{random.randint(85, 245)}%",
                'apy': f"{random.uniform(12.5, 78.3):.1f}%",
                'risk_score': f"{random.randint(3, 7)}/10"
            }
        
        elif opp_type == 'LIQUIDATION_MEV':
            return {
                'profit_margin': f"{random.uniform(3.2, 12.8):.1f}%",
                'gas_limit': f"{random.randint(180, 420)}k",
                'competition': f"{random.randint(2, 8)} bots",
                'success_rate': f"{random.randint(72, 91)}%"
            }
        
        elif opp_type == 'TOKEN_LAUNCH_SNIPE':
            return {
                'launch_time': f"{random.randint(5, 35)} min",
                'initial_mcap': f"${random.uniform(0.5, 8.2):.1f}M",
                'social_score': f"{random.randint(65, 95)}/100",
                'liquidity': f"${random.randint(250, 1500)}k"
            }
        
        return {}