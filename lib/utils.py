def flatten_list(irregular_list):
    return [element for item in irregular_list for element in flatten_list(item)] if type(irregular_list) is list else [irregular_list]
