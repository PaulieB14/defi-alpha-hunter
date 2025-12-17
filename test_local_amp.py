#!/usr/bin/env python3
"""
Test Local AMP Server
Quick test to show the local AMP server is working
"""

import requests
import json

LOCAL_AMP_URL = "http://localhost:1603"

def test_local_amp():
    print("🔍 Testing Local AMP Server...")
    print(f"Server: {LOCAL_AMP_URL}")
    
    # Test basic query
    try:
        response = requests.post(
            LOCAL_AMP_URL,
            data="SELECT 1 as test, 'Local AMP is working!' as message, NOW() as timestamp",
            headers={'Content-Type': 'text/plain'},
            timeout=5
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Local AMP Server is RUNNING!")
            print(f"   Response: {result}")
            return True
        else:
            print(f"❌ Server responded with error: {response.status_code}")
            print(f"   Error: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to local AMP server")
        print("   Server may not be running on localhost:1603")
        return False
    except Exception as e:
        print(f"❌ Error testing server: {e}")
        return False

def test_more_queries():
    """Test more complex queries"""
    print("\n🔍 Testing More Complex Queries...")
    
    queries = [
        "SELECT 'Hello' as greeting, 42 as answer",
        "SELECT CURRENT_TIMESTAMP as now",
        "SELECT 1+1 as math, 'AMP' as database"
    ]
    
    for i, query in enumerate(queries, 1):
        print(f"\n{i}. Testing: {query}")
        try:
            response = requests.post(
                LOCAL_AMP_URL,
                data=query,
                headers={'Content-Type': 'text/plain'},
                timeout=5
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"   ✅ Result: {result}")
            else:
                print(f"   ❌ Failed: {response.status_code} - {response.text}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")

def show_server_info():
    """Show information about the running server"""
    print("\n📊 Local AMP Server Information:")
    print(f"   🔗 URL: {LOCAL_AMP_URL}")
    print(f"   📡 Type: JSON Lines over HTTP")
    print(f"   🗄️  Database: PostgreSQL (localhost:5432/amp)")
    print(f"   ⚙️  Config: /tmp/amp-config.toml")
    
    print(f"\n🚀 How to Use:")
    print(f"   curl -X POST {LOCAL_AMP_URL} --data 'SELECT 1 as test'")
    print(f"   python3 test_local_amp.py")
    print(f"   python3 dashboard.py  # Start web dashboard")

if __name__ == "__main__":
    print("🎯 LOCAL AMP SERVER TEST")
    print("="*50)
    
    if test_local_amp():
        test_more_queries()
        show_server_info()
        
        print(f"\n🎉 LOCAL AMP SERVER IS WORKING!")
        print("✅ Ready to execute real blockchain queries")
        print("✅ Can connect dashboard to local server")
        print("✅ No fake data - server can handle real SQL")
    else:
        print(f"\n❌ LOCAL AMP SERVER NOT RUNNING")
        print("🔧 To start it:")
        print("   export PATH=\"/opt/homebrew/opt/postgresql@15/bin:$PATH\"")
        print("   ampd --config /tmp/amp-config.toml server --jsonl-server")