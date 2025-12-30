import requests
import json
from decimal import Decimal

BASE_URL = "http://127.0.0.1:8003"

def test_products_endpoints():
    print("=== Testing Products Endpoints ===")
    
    # Test GET /products
    print("\n1. Testing GET /products")
    response = requests.get(f"{BASE_URL}/products")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        products = response.json()
        print(f"Found {len(products)} products")
        print("PASS: GET /products")
    else:
        print("FAIL: GET /products")
    
    # Test POST /products
    print("\n2. Testing POST /products")
    new_product = {
        "name": "Test Product",
        "description": "A test product for API verification",
        "price": "99.99"
    }
    response = requests.post(f"{BASE_URL}/products", json=new_product)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        created_product = response.json()
        product_id = created_product["id"]
        print(f"Created product with ID: {product_id}")
        print("PASS: POST /products")
        
        # Test GET /products/{product_id}
        print(f"\n3. Testing GET /products/{product_id}")
        response = requests.get(f"{BASE_URL}/products/{product_id}")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print("PASS: GET /products/{product_id}")
        else:
            print("FAIL: GET /products/{product_id}")
        
        # Test PUT /products/{product_id}
        print(f"\n4. Testing PUT /products/{product_id}")
        updated_product = {
            "name": "Updated Test Product",
            "description": "An updated test product",
            "price": "149.99"
        }
        response = requests.put(f"{BASE_URL}/products/{product_id}", json=updated_product)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            updated = response.json()
            print(f"Updated product name: {updated.get('name')}")
            print("PASS: PUT /products/{product_id}")
        else:
            print("FAIL: PUT /products/{product_id}")
            print(f"Error: {response.text}")
    else:
        print("FAIL: POST /products")

def test_orders_endpoints():
    print("\n=== Testing Orders Endpoints ===")
    
    # Test GET /orders
    print("\n1. Testing GET /orders")
    response = requests.get(f"{BASE_URL}/orders")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        orders = response.json()
        print(f"Found {len(orders)} orders")
        print("PASS: GET /orders")
    else:
        print("FAIL: GET /orders")
    
    # Test POST /orders
    print("\n2. Testing POST /orders")
    new_order = {
        "customer_name": "Test Customer",
        "customer_email": "test@example.com",
        "shipping_address": "123 Test St, Test City, TC 12345",
        "total_amount": "129.98",
        "items": [
            {
                "product_id": 1,
                "quantity": 2,
                "price_at_time": "64.99"
            }
        ]
    }
    response = requests.post(f"{BASE_URL}/orders", json=new_order)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        created_order = response.json()
        order_id = created_order["id"]
        print(f"Created order with ID: {order_id}")
        print("PASS: POST /orders")
        
        # Test GET /orders/{order_id}
        print(f"\n3. Testing GET /orders/{order_id}")
        response = requests.get(f"{BASE_URL}/orders/{order_id}")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print("PASS: GET /orders/{order_id}")
        else:
            print("FAIL: GET /orders/{order_id}")
    else:
        print("FAIL: POST /orders")
        print(f"Error: {response.text}")

def test_error_cases():
    print("\n=== Testing Error Cases ===")
    
    # Test non-existent product
    print("\n1. Testing GET /products/999 (non-existent)")
    response = requests.get(f"{BASE_URL}/products/999")
    print(f"Status: {response.status_code}")
    if response.status_code == 404:
        print("PASS: Product not found error")
    else:
        print("FAIL: Product not found error")
    
    # Test non-existent order
    print("\n2. Testing GET /orders/999 (non-existent)")
    response = requests.get(f"{BASE_URL}/orders/999")
    print(f"Status: {response.status_code}")
    if response.status_code == 404:
        print("PASS: Order not found error")
    else:
        print("FAIL: Order not found error")

if __name__ == "__main__":
    print("Starting API Verification Tests...")
    print("Make sure your FastAPI server is running on http://127.0.0.1:8003")
    
    try:
        # Test server is running
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("PASS: Server is running")
            
            test_products_endpoints()
            test_orders_endpoints()
            test_error_cases()
            
            print("\n=== Test Summary ===")
            print("API verification completed!")
        else:
            print("FAIL: Server is not responding correctly")
    except requests.exceptions.ConnectionError:
        print("FAIL: Cannot connect to server. Make sure it's running on http://127.0.0.1:8003")