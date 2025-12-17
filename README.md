# 🚀 DeFi Alpha Hunter

**Real-time profit opportunity scanner for Ethereum & Base using live blockchain data**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![AMP Powered](https://img.shields.io/badge/Powered%20by-AMP-purple.svg)](https://amp.thegraph.com/)

## 🎯 What This Does

This system analyzes **real blockchain data** from 33+ datasets to find profitable DeFi opportunities using [AMP (The Graph's blockchain database)](https://github.com/edgeandnode/amp).

### 🔥 Real Data Sources

- **33 Real Blockchain Datasets** from AMP Playground
- **Ethereum Mainnet** - Raw transactions, Uniswap V3, Aave V2, Compound
- **Base Mainnet** - Uniswap V3, Aerodrome, Aave V3, Bridge Analytics
- **NO FAKE DATA** - Only actual blockchain transactions and events

### 💰 Opportunity Types

- **🌉 Cross-Chain Arbitrage** - Real price differences between Ethereum & Base
- **🐋 Whale Tracking** - Actual large wallet movements (>1000 ETH)
- **⚡ Liquidation Detection** - Real Aave/Compound liquidation events
- **🔵 Base Ecosystem** - Token launches, bridge activity, DeFi growth

## 🚀 Quick Start

### Option 1: Web Playground (Immediate Access)

1. Go to [AMP Playground](https://playground.amp.thegraph.com/playground)
2. Select a dataset (e.g., `edgeandnode/ethereum_mainnet`)
3. Run real queries:

```sql
-- Find whale transactions (>1000 ETH)
SELECT from_address, to_address, value, block_timestamp, transaction_hash
FROM "edgeandnode/ethereum_mainnet@latest".transactions
WHERE value > 1000000000000000000000
  AND block_timestamp > NOW() - INTERVAL '1 hour'
ORDER BY value DESC LIMIT 10;
```

### Option 2: Run Local Demo

```bash
# Install dependencies
pip install requests python-dateutil

# Run real data demo
python real_data_demo.py

# Run web dashboard
python dashboard.py
# Open http://localhost:8080
```

## 📊 Real Query Examples

### 🐋 Whale Tracking
```sql
-- Track large ETH transfers
SELECT from_address, to_address, value, transaction_hash
FROM "edgeandnode/ethereum_mainnet@latest".transactions
WHERE value > 1000000000000000000000  -- > 1000 ETH
ORDER BY value DESC;
```

### ⚡ Liquidation Events
```sql
-- Get Aave liquidations
SELECT user, liquidator, debt_to_cover, transaction_hash
FROM "fernando/aave_v3_base@latest".event__liquidation_call
WHERE block_timestamp > NOW() - INTERVAL '24 hours'
ORDER BY debt_to_cover DESC;
```

### 🌉 Cross-Chain Arbitrage
```sql
-- Compare Uniswap prices ETH vs Base
-- ETH Uniswap swaps
SELECT pool_address, sqrt_price_x96, block_timestamp
FROM "edgeandnode/uniswap_v3_ethereum@latest".event__swap
WHERE block_timestamp > NOW() - INTERVAL '1 hour';

-- Base Uniswap swaps
SELECT pool_address, sqrt_price_x96, block_timestamp  
FROM "edgeandnode/uniswap_v3_base@latest".event__swap
WHERE block_timestamp > NOW() - INTERVAL '1 hour';
```

## 🔧 Local AMP Setup

To run queries locally with your own AMP instance:

```bash
# Install AMP
curl --proto '=https' --tlsv1.2 -sSf https://ampup.sh/install | sh

# Start PostgreSQL
brew install postgresql@15
brew services start postgresql@15
createdb amp

# Configure AMP
echo 'metadata_db_url = "postgresql://$(whoami)@localhost:5432/amp"' > amp-config.toml
echo 'data_dir = "/tmp/amp-data"' >> amp-config.toml

# Start AMP server
ampd --config amp-config.toml server --jsonl-server

# Test connection
curl -X POST http://localhost:1603 --data 'SELECT 1 as test'
```

## 🌐 Web Dashboard

Interactive dashboard showing:
- 📊 Real-time opportunities from actual blockchain data
- 📈 Confidence scores based on real transaction patterns
- 🎯 Chain-specific breakdowns (ETH vs Base)
- ⚡ Actionable trading signals with real tx hashes

## 📎 Real Data Sources

All data comes from [AMP Playground](https://playground.amp.thegraph.com/) with 33+ real datasets:

### Ethereum Mainnet
- `edgeandnode/ethereum_mainnet` - Raw blockchain data
- `edgeandnode/uniswap_v3_ethereum` - Real Uniswap V3 swaps
- `edgeandnode/aave_v2_ethereum` - Lending/liquidation events
- `edgeandnode/compound_v2_ethereum` - Money market data

### Base Mainnet  
- `edgeandnode/base_mainnet` - Raw Base blockchain data
- `edgeandnode/uniswap_v3_base` - Base Uniswap V3 activity
- `fernando/aave_v3_base` - Base lending protocol
- `edgeandnode/aerodrome_base` - Base's central DEX

## ⚠️ No Fake Data Policy

This project uses **ONLY real blockchain data**:
- ✅ Actual transaction hashes you can verify on Etherscan
- ✅ Real wallet addresses with verifiable history  
- ✅ Live price data from actual DEX swaps
- ✅ Genuine liquidation events with real profit potential
- ❌ No simulations, mock data, or fake examples

## 📈 Trading Integration

The system can integrate with:
- **1inch API** - For optimal swap routing
- **Uniswap V3 SDK** - Direct DEX integration  
- **Telegram/Discord** - Alert notifications
- **TradingView** - Chart integration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your improvements (must use real data only)
4. Submit a pull request

Ideas for contributions:
- Additional chain support (Polygon, Arbitrum)
- More sophisticated analysis algorithms
- Better UI/UX for dashboard
- Mobile app version
- Trading bot integration

## 📄 License

MIT License - see [LICENSE](LICENSE) file

## 🙏 Acknowledgments

- [The Graph](https://thegraph.com/) for AMP blockchain data infrastructure
- [Edge & Node](https://github.com/edgeandnode/amp) for the AMP database
- [Uniswap](https://uniswap.org/) for DEX protocols
- [Aave](https://aave.com/) for lending protocol data
- [Base](https://base.org/) for Layer 2 infrastructure

---

**⭐ Star this repo if you found it useful!**

**🐦 Follow [@PaulBarba12](https://twitter.com/PaulBarba12) for more DeFi alpha**