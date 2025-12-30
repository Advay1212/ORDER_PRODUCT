from sqlalchemy.orm import Session
from db_config import SessionLocal
from database import Order, OrderItem, OrderStatus
from decimal import Decimal

def add_sample_orders():
    db = SessionLocal()
    
    # Check if orders already exist
    if db.query(Order).count() > 0:
        print(f"Orders already exist: {db.query(Order).count()} orders found")
        db.close()
        return
    
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
        ),
        Order(
            customer_name="Bob Johnson",
            customer_email="bob@example.com",
            shipping_address="789 Pine Rd, Elsewhere, EW 13579",
            total_amount=Decimal("479.97"),
            status=OrderStatus.PENDING
        )
    ]
    
    for order in orders:
        db.add(order)
    
    db.commit()
    db.flush()
    
    # Create order items
    order_items = [
        # Order 1 items (John Doe)
        OrderItem(order_id=1, product_id=1, quantity=1, price_at_time=Decimal("999.99")),
        OrderItem(order_id=1, product_id=2, quantity=1, price_at_time=Decimal("29.99")),
        # Order 2 items (Jane Smith)
        OrderItem(order_id=2, product_id=3, quantity=1, price_at_time=Decimal("149.99")),
        OrderItem(order_id=2, product_id=2, quantity=1, price_at_time=Decimal("29.99")),
        # Order 3 items (Bob Johnson)
        OrderItem(order_id=3, product_id=4, quantity=1, price_at_time=Decimal("399.99")),
        OrderItem(order_id=3, product_id=5, quantity=1, price_at_time=Decimal("79.99"))
    ]
    
    for item in order_items:
        db.add(item)
    
    db.commit()
    print(f"Added {len(orders)} sample orders with order items")
    db.close()

if __name__ == "__main__":
    add_sample_orders()