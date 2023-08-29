import uuid
from utils import (
    create_business_user_item, 
    read_business_user_item, 
    update_business_user_item, 
    delete_business_user_item
)

business_user_item = {
    'email': {'S': 'john@gmail.com'},
    'is_superuser': {'BOOL': False},
    'first_name': {'S': 'John'},
    'last_name': {'S': 'Doe'},
    'is_active': {'BOOL': True},
    'date_joined': {'S': '2023-08-22'},
    'company_name': {'S': 'ABC Corp'},
    'broker_service': {'S': 'XYZ Broker'},
    'broker_api_key': {'S': f'{uuid.uuid4()}'}
}

item_created = create_business_user_item(business_user_item)
print("Item created :: ", item_created)

get_item = read_business_user_item('john@gmail.com')
print("Item read :: ", get_item)

update_expression = "SET is_active = :new_active_value"
expression_values = {":new_active_value": {'BOOL': False}}
item_updated = update_business_user_item('john@gmail.com', update_expression, expression_values)
print("Item updated :: ", item_updated)

item_deleted = delete_business_user_item('john@email.com')
print("Item deleted :: ", item_deleted)

# check if item deleted
get_item = read_business_user_item('john@gmail.com')
print("Item read after delete:: ", get_item)

# again create the above data to be used by customer
item_created = create_business_user_item(business_user_item)
print("Item created again:: ", item_created)