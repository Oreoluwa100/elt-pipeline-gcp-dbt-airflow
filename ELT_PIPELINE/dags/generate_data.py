"""
This script contains a function to simulate order data which mimics real orders
for the ELT pipeline development.
Each order includes a unique order ID, random customer ID, product ID, quantity, price
and timestamp from yesterday.
"""

import json 
import random
from datetime import datetime, timedelta, time
import uuid

def generate_order():
    order_id = str(uuid.uuid4()) # Generate UUID for unique order identifier
    customer_id = random.randint(1000, 9999) # Random customer ID
    product_id = random.choice(['A101', 'B202', 'C303', 'D404']) # Random product code
    quantity = random.randint(1, 10) # Random order quantity between 1 - 10
    price = round(random.uniform(10.0, 100.0),2) # Random price between 10.0 - 100.0

    # Generate order date from a random timestamp yesterday
    order_date = (datetime.combine((datetime.now().date() - timedelta(days = 1)), 
                                   time(random.randint(0,23), random.randint(0,59), random.randint(0,59)
                                    ))).strftime("%Y-%m-%d %H:%M:%S")
    return {
        "order_id": order_id,
        "customer_id": customer_id,
        "product_id": product_id,
        "quantity": quantity,
        "price": price,
        "order_date": order_date
    }