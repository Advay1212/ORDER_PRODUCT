from sqlalchemy.orm import Session
from db_config import SessionLocal, create_tables
from database import Product, Order, OrderItem, OrderStatus
from decimal import Decimal

def seed_database():
    create_tables()
    
    db = SessionLocal()
    
    # Check if products already exist
    if db.query(Product).count() > 0:
        print("Database already seeded")
        db.close()
        return
    
    # Create sample products
    products = [
        Product(
            name="Laptop",
            description="High-performance laptop for work and gaming",
            price=Decimal("999.99")
        ),
        Product(
            name="Wireless Mouse",
            description="Ergonomic wireless mouse with long battery life",
            price=Decimal("29.99")
        ),
        Product(
            name="Mechanical Keyboard",
            description="RGB mechanical keyboard with blue switches",
            price=Decimal("149.99")
        ),
        Product(
            name="Monitor",
            description="27-inch 4K monitor with HDR support",
            price=Decimal("399.99")
        ),
        Product(
            name="Webcam",
            description="HD webcam for video calls and streaming",
            price=Decimal("79.99")
        )
    ]
    
    for product in products:
        db.add(product)
    
    db.commit()
    db.flush()
    
    # Create sample orders
    orders = [
        Order(
            customer_name="John Doe",
            customer_email="john@example.com",
            shipping_address="123 Main St, Anytown, AT 12345",
            total_amount=Decimal("1029.98"),
            status=OrderStatus.DELIVERED
        ),
        Order(
            customer_name="Jane Smith",
            customer_email="jane@example.com",
            shipping_address="456 Oak Ave, Somewhere, SW 67890",
            total_amount=Decimal("179.98"),
            status=OrderStatus.SHIPPED
        )
    ]
    
    for order in orders:
        db.add(order)
    
    db.commit()
    db.flush()
    
    # Create order items
    order_items = [
        # Order 1 items
        OrderItem(order_id=1, product_id=1, quantity=1, price_at_time=Decimal("999.99")),
        OrderItem(order_id=1, product_id=2, quantity=1, price_at_time=Decimal("29.99")),
        # Order 2 items
        OrderItem(order_id=2, product_id=3, quantity=1, price_at_time=Decimal("149.99")),
        OrderItem(order_id=2, product_id=2, quantity=1, price_at_time=Decimal("29.99"))
    ]
    
    for item in order_items:
        db.add(item)
    
    db.commit()
    print(f"Seeded database with {len(products)} products and {len(orders)} orders")
    db.close()

if __name__ == "__main__":
    seed_database()