# DeFi Alpha Hunter

A blockchain data analysis tool for finding arbitrage opportunities, whale movements, and liquidation events across Ethereum and Base networks.

## Overview

This project uses [AMP (The Graph's blockchain database)](https://github.com/edgeandnode/amp) to analyze real blockchain data from multiple sources including Uniswap, Aave, and other DeFi protocols.

## Features

- **Cross-chain arbitrage detection** between Ethereum and Base
- **Whale transaction tracking** for large wallet movements
- **Liquidation event monitoring** from lending protocols
- **Web dashboard** with real-time updates
- **Real blockchain data** - no simulated or fake data

## Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL
- AMP (blockchain database)

### Installation

1. **Install AMP:**
```bash
curl --proto '=https' --tlsv1.2 -sSf https://ampup.sh/install | sh
```

2. **Setup PostgreSQL:**
```bash
brew install postgresql@15
brew services start postgresql@15
createdb amp
```

3. **Install Python dependencies:**
```bash
pip install requests python-dateutil
```

### Running the Application

1. **Start AMP server:**
```bash
# Create config file
echo 'metadata_db_url = "postgresql://$(whoami)@localhost:5432/amp"' > amp-config.toml
echo 'data_dir = "/tmp/amp-data"' >> amp-config.toml

# Start server
ampd --config amp-config.toml server --jsonl-server
```

2. **Run the web dashboard:**
```bash
python dashboard.py
```

3. **Open in browser:**
```
http://localhost:8080
```

## Data Sources

The application connects to real blockchain datasets including:

- Ethereum mainnet transactions
- Uniswap V3 swap data (Ethereum and Base)
- Aave lending protocol events
- Base network activity

All data comes from actual blockchain transactions - no simulated data is used.

## API Usage

The local AMP server accepts SQL queries via HTTP POST:

```bash
curl -X POST http://localhost:1603 \
  --data 'SELECT 1 as test' \
  --header 'Content-Type: text/plain'
```

## Configuration

Edit `amp-config.toml` to customize:
- Database connection
- Data directory
- Server ports

## Development

To run the real data demo:
```bash
python real_data_demo.py
```

To test the local server:
```bash
python test_local_amp.py
```

## License

MIT License - see LICENSE file for details.

## Acknowledgments

- [The Graph](https://thegraph.com/) for AMP blockchain data infrastructure
- [Edge & Node](https://github.com/edgeandnode/amp) for the AMP database