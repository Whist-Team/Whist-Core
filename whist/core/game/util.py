def enforce_str_on_dict(dictionary: dict, keys: set[str]) -> dict:
    for key in keys:
        if key in dictionary:
            dictionary[key] = str(dictionary[key]) if dictionary[key] else None
    return dictionary
