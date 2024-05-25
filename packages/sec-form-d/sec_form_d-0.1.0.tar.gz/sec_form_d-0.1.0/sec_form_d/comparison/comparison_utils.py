from typing import Union

def is_empty_dictionary(obj: Union[str, dict, list, bool]) -> bool:
    """
    Recursive function to test if a dictionary is empty. Fields
    also included as blank is the boolean value False.

    Args:
        obj (str | dict | list | bool): A dictionary, list, str or boolean object.

    Returns:
        bool: A boolean indicating whether the dictionary is empty.
    """
    if isinstance(obj, dict):
        return all(
            is_empty_dictionary(obj=field) for _, field in obj.items()
        )
    elif isinstance(obj, list):
        return all(
            is_empty_dictionary(obj=field) for field in obj
        )
    else:
        return not obj