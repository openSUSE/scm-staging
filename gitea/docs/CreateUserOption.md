# CreateUserOption

CreateUserOption create user options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**full_name** | **str** |  | [optional] 
**login_name** | **str** |  | [optional] 
**must_change_password** | **bool** |  | [optional] 
**password** | **str** |  | 
**restricted** | **bool** |  | [optional] 
**send_notify** | **bool** |  | [optional] 
**source_id** | **int** |  | [optional] 
**username** | **str** |  | 
**visibility** | **str** |  | [optional] 

## Example

```python
from swagger_client.models.create_user_option import CreateUserOption

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserOption from a JSON string
create_user_option_instance = CreateUserOption.from_json(json)
# print the JSON string representation of the object
print CreateUserOption.to_json()

# convert the object into a dict
create_user_option_dict = create_user_option_instance.to_dict()
# create an instance of CreateUserOption from a dict
create_user_option_form_dict = create_user_option.from_dict(create_user_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


