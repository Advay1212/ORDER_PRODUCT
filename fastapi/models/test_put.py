import requests
import json

BASE_URL = "http://127.0.0.1:8003"

def test_put_endpoint():
    print("=== Testing PUT Endpoint ===")
    
    # First, get existing products
    print("1. Getting existing products...")
    response = requests.get(f"{BASE_URL}/products")
    if response.status_code == 200:
        products = response.json()
        if products:
            product_id = products[0]["id"]
            print(f"Found product ID: {product_id}")
            print(f"Current product: {products[0]}")
            
            # Test PUT update
            print(f"\n2. Testing PUT /products/{product_id}")
            update_data = {
                "name": "Updated Product Name",
                "description": "Updated description",
                "price": "199.99"
            }
            
            response = requests.put(f"{BASE_URL}/products/{product_id}", json=update_data)
            print(f"PUT Status: {response.status_code}")
            print(f"PUT Response: {response.text}")
            
            if response.status_code == 200:
                print("✅ PUT request successful")
                updated_product = response.json()
                print(f"Updated product: {updated_product}")
            else:
                print("❌ PUT request failed")
        else:
            print("No products found")
    else:
        print(f"Failed to get products: {response.status_code}")

if __name__ == "__main__":
    test_put_endpoint()