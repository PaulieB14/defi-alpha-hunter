"""
Configuration for DeFi Alpha Hunter
"""

# Whale addresses to track (add your own discoveries)
WHALE_ADDRESSES = [
    "0x8eb8a3b98659cce290402893d0123abb75e3ab28",  # Example profitable wallet
    "0x47ac0fb4f2d84898e4d9e7b4dab3c24507a6d503",  # Another whale
    "0x3cd751e6b0078be393132286c442345e5dc49699",  # Coinbase institutional
    "0x40ec5B33f54e0E8A33A975908C5BA1c14e5BbbDf",  # Base ecosystem whale
]

# Minimum thresholds for opportunities
MIN_ARBITRAGE_BPS = 8  # Minimum 0.08% profit for arbitrage
MIN_WHALE_AMOUNT = 1000000  # Minimum $1M for whale tracking
MIN_LIQUIDATION_AMOUNT = 500000  # Minimum $500K liquidation

# Gas price thresholds (gwei)
LOW_GAS_THRESHOLD = 20  # Below this = profitable for complex trades
HIGH_GAS_THRESHOLD = 80  # Above this = users migrate to L2

# API endpoints (optional - uses AMP playground by default)
ETH_RPC_URL = None  # Add your own for faster data
BASE_RPC_URL = None

# Trading integration (optional)
UNISWAP_API_KEY = None
ONEINCH_API_KEY = None

# Notification settings
TELEGRAM_BOT_TOKEN = None
TELEGRAM_CHAT_ID = None
DISCORD_WEBHOOK_URL = None