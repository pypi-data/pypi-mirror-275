def check_nested_dict(nested_dict:dict, keys_list:list)->bool:
    """
    Helper function to recursively search for keys in a nested dictionary.
    
    Args:
        nested_dict (dict): The dictionary to search.
        keys_list (list): The list of keys to check for.
    
    Returns:
        bool: True if all keys are found, False otherwise.
    """
    for keys in keys_list:
        temp_dict = nested_dict
        for key in keys:
            if key in temp_dict:
                temp_dict = temp_dict[key]
            else:
                break
        else:
            return True
    return False