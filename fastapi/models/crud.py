from sqlalchemy.orm import Session, joinedload
from database import Product, Order, OrderItem
from schemas import ProductCreate, ProductUpdate, OrderCreate
from datetime import datetime

# Product CRUD
def get_products(db: Session):
    return db.query(Product).all()

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        for key, value in product.dict().items():
            setattr(db_product, key, value)
        db_product.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product

# Order CRUD
def get_orders(db: Session):
    return db.query(Order).options(joinedload(Order.items)).all()

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def create_order(db: Session, order: OrderCreate):
    # Create order without items first
    order_data = order.dict()
    items_data = order_data.pop('items')
    
    db_order = Order(**order_data)
    db.add(db_order)
    db.flush()  # Get the order ID
    
    # Create order items
    for item_data in items_data:
        db_item = OrderItem(**item_data, order_id=db_order.id)
        db.add(db_item)
    
    db.commit()
    db.refresh(db_order)
    return db_order