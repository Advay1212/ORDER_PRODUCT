from pydantic import BaseModel, validator, EmailStr
from decimal import Decimal
from datetime import datetime
from typing import Optional, List
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"

# Product Schemas
class ProductBase(BaseModel):
    name: str
    description: str
    price: Decimal
    
    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip()
    
    @validator('description')
    def description_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Description cannot be empty')
        return v.strip()
    
    @validator('price')
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Price must be greater than 0')
        return v

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Order Item Schemas
class OrderItemBase(BaseModel):
    product_id: int
    quantity: int
    price_at_time: Decimal
    
    @validator('quantity')
    def quantity_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Quantity must be greater than 0')
        return v
    
    @validator('price_at_time')
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Price must be greater than 0')
        return v

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: int
    
    class Config:
        from_attributes = True

# Order Schemas
class OrderBase(BaseModel):
    customer_name: str
    customer_email: EmailStr
    shipping_address: str
    total_amount: Decimal
    items: List[OrderItemCreate]
    
    @validator('customer_name')
    def customer_name_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Customer name cannot be empty')
        return v.strip()
    
    @validator('shipping_address')
    def shipping_address_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Shipping address cannot be empty')
        return v.strip()
    
    @validator('total_amount')
    def total_amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Total amount must be greater than 0')
        return v
    
    @validator('items')
    def items_must_not_be_empty(cls, v):
        if not v or len(v) == 0:
            raise ValueError('Order must have at least one item')
        return v

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    order_date: datetime
    status: OrderStatus
    items: List[OrderItem]
    
    class Config:
        from_attributes = True