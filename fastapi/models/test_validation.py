import requests
import json

BASE_URL = "http://127.0.0.1:8003"

def test_validation_rules():
    print("=== Testing Validation Rules ===")
    
    # Test invalid product - empty name
    print("\n1. Testing invalid product - empty name")
    invalid_product = {
        "name": "",
        "description": "Test description",
        "price": "99.99"
    }
    response = requests.post(f"{BASE_URL}/products", json=invalid_product)
    print(f"Status: {response.status_code}")
    if response.status_code == 422:
        print("✅ Empty name validation - PASS")
        print(f"Error: {response.json()}")
    else:
        print("❌ Empty name validation - FAIL")
    
    # Test invalid product - negative price
    print("\n2. Testing invalid product - negative price")
    invalid_product = {
        "name": "Test Product",
        "description": "Test description",
        "price": "-10.00"
    }
    response = requests.post(f"{BASE_URL}/products", json=invalid_product)
    print(f"Status: {response.status_code}")
    if response.status_code == 422:
        print("✅ Negative price validation - PASS")
        print(f"Error: {response.json()}")
    else:
        print("❌ Negative price validation - FAIL")
    
    # Test invalid order - empty customer name
    print("\n3. Testing invalid order - empty customer name")
    invalid_order = {
        "customer_name": "",
        "customer_email": "test@example.com",
        "shipping_address": "123 Test St",
        "total_amount": "100.00",
        "items": [
            {
                "product_id": 1,
                "quantity": 1,
                "price_at_time": "100.00"
            }
        ]
    }
    response = requests.post(f"{BASE_URL}/orders", json=invalid_order)
    print(f"Status: {response.status_code}")
    if response.status_code == 422:
        print("✅ Empty customer name validation - PASS")
        print(f"Error: {response.json()}")
    else:
        print("❌ Empty customer name validation - FAIL")
    
    # Test invalid order - zero quantity
    print("\n4. Testing invalid order - zero quantity")
    invalid_order = {
        "customer_name": "Test Customer",
        "customer_email": "test@example.com",
        "shipping_address": "123 Test St",
        "total_amount": "100.00",
        "items": [
            {
                "product_id": 1,
                "quantity": 0,
                "price_at_time": "100.00"
            }
        ]
    }
    response = requests.post(f"{BASE_URL}/orders", json=invalid_order)
    print(f"Status: {response.status_code}")
    if response.status_code == 422:
        print("✅ Zero quantity validation - PASS")
        print(f"Error: {response.json()}")
    else:
        print("❌ Zero quantity validation - FAIL")
    
    # Test invalid order - non-existent product
    print("\n5. Testing invalid order - non-existent product")
    invalid_order = {
        "customer_name": "Test Customer",
        "customer_email": "test@example.com",
        "shipping_address": "123 Test St",
        "total_amount": "100.00",
        "items": [
            {
                "product_id": 999,
                "quantity": 1,
                "price_at_time": "100.00"
            }
        ]
    }
    response = requests.post(f"{BASE_URL}/orders", json=invalid_order)
    print(f"Status: {response.status_code}")
    if response.status_code == 400:
        print("✅ Non-existent product validation - PASS")
        print(f"Error: {response.json()}")
    else:
        print("❌ Non-existent product validation - FAIL")

def test_timestamps():
    print("\n=== Testing Timestamps ===")
    
    # Create a product and check timestamps
    print("\n1. Testing product timestamps")
    new_product = {
        "name": "Timestamp Test Product",
        "description": "Testing timestamp creation",
        "price": "50.00"
    }
    response = requests.post(f"{BASE_URL}/products", json=new_product)
    if response.status_code == 200:
        product = response.json()
        if product.get("created_at") and product.get("updated_at"):
            print("✅ Product timestamps - PASS")
            print(f"Created at: {product['created_at']}")
            print(f"Updated at: {product['updated_at']}")
        else:
            print("❌ Product timestamps - FAIL")
    
    # Create an order and check timestamp
    print("\n2. Testing order timestamps")
    new_order = {
        "customer_name": "Timestamp Test Customer",
        "customer_email": "timestamp@example.com",
        "shipping_address": "123 Timestamp St",
        "total_amount": "50.00",
        "items": [
            {
                "product_id": 1,
                "quantity": 1,
                "price_at_time": "50.00"
            }
        ]
    }
    response = requests.post(f"{BASE_URL}/orders", json=new_order)
    if response.status_code == 200:
        order = response.json()
        if order.get("order_date"):
            print("✅ Order timestamp - PASS")
            print(f"Order date: {order['order_date']}")
        else:
            print("❌ Order timestamp - FAIL")

if __name__ == "__main__":
    print("Starting Data Validation Tests...")
    print("Make sure your FastAPI server is running on http://127.0.0.1:8003")
    
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ Server is running")
            test_validation_rules()
            test_timestamps()
            print("\n=== Validation Test Summary ===")
            print("Data validation tests completed!")
        else:
            print("❌ Server is not responding correctly")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure it's running on http://127.0.0.1:8003")