from utils import (
    create_customer_item,
    read_customer_item,
    update_customer_item,
    delete_customer_item
)

customer_item = {
    'business_user_email': {'S': 'john@email.com'},
    'customer_name': {'S': 'Alice'},
    'date_joined': {'S': '2023-08-22'},
    'customer_broker_id': {'S': 'BROKER123'},
    'investment_style': {'S': 'Conservative'},
    'investment_strategy': {'S': 'Long-term'},
    'trading_ability': {'BOOL': True}
}

item_created = create_customer_item(customer_item)
print("Item created :: ", item_created)

get_item = read_customer_item('john@email.com', '2023-08-22')
print("Item read :: ", get_item)

# Update example
update_expression = "SET customer_name = :new_name_value"
expression_values = {":new_name_value": {'S': 'Alicia'}}
item_updated = update_customer_item('john@email.com', '2023-08-22', update_expression, expression_values)
print("Item updated :: ", item_updated)

item_deleted = delete_customer_item('john@email.com', '2023-08-22')
print("Item deleted :: ", item_deleted)