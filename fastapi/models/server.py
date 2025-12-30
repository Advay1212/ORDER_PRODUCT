from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import os

from db_config import get_db, create_tables
from schemas import Product, ProductCreate, ProductUpdate, Order, OrderCreate
import crud

app = FastAPI(title="Products & Orders API")

# Create database tables
create_tables()

# CORS middleware configured for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://order-product-frontend.onrender.com" # Your live frontend URL
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Products & Orders API with Database"}

# Product endpoints
@app.post("/products", response_model=Product)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@app.get("/products", response_model=List[Product])
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "Product not found", "message": f"Product with ID {product_id} does not exist."}
        )
    return db_product

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud.update_product(db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "Product not found", "message": f"Product with ID {product_id} does not exist."}
        )
    return db_product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.delete_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "Product not found", "message": f"Product with ID {product_id} does not exist."}
        )
    return {"message": "Product deleted successfully"}

# Order endpoints
@app.post("/orders", response_model=Order)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    # Validate that all products exist
    for item in order.items:
        db_product = crud.get_product(db, product_id=item.product_id)
        if db_product is None:
            raise HTTPException(
                status_code=400,
                detail={"error": "Invalid product", "message": f"Product with ID {item.product_id} does not exist."}
            )
    return crud.create_order(db=db, order=order)

@app.get("/orders", response_model=List[Order])
def get_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)

@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "Order not found", "message": f"Order with ID {order_id} does not exist."}
        )
    return db_order

if __name__ == "__main__":
    import uvicorn
    # Use the PORT environment variable provided by Render, defaulting to 8003 for local development
    port = int(os.environ.get("PORT", 8003))
    # Host changed to 0.0.0.0 to accept external traffic on Render
    uvicorn.run(app, host="0.0.0.0", port=port)