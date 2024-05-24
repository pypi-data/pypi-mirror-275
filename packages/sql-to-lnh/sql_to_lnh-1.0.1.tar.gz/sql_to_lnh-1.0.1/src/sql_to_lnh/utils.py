def format_str(s: str, indent=4, end="\n") -> str:
    """
    Formats a string by adding indentation and an end character.

    Args:
        s: The string to format.
        indent: The number of spaces to indent the string.
        end: The character to add to the end of the string.

    Returns:
        The formatted string.
    """
    return f"{' ' * indent}{s}{end}"


def find_index(data, condition):
    """
    Finds the index of the first element in a list that meets a given condition.

    Args:
        data: The list to search.
        condition: A function that takes an element from the list and returns True if it meets the requirement.

    Returns:
        The index of the first element that meets the condition, or -1 if no such element is found.
    """

    for i, element in enumerate(data):
        if condition(element):
            return i
    return -1


def get_subset_between(dictionaries, start_condition, end_condition):
    """
    Extracts a subset of dictionaries from a list that fall between two given conditions.

    Args:
        dictionaries: The list of dictionaries to search.
        start_condition: A dictionary representing the starting condition for the subset.
        end_condition: A dictionary representing the ending condition for the subset.

    Returns:
        A list of dictionaries that fall between the start and end conditions.
    """
    subset = []
    is_subset_started = False

    for d in dictionaries:
        if not is_subset_started and all(d[key] == start_condition[key] for key in start_condition):
            # Start adding dictionaries to the subset
            is_subset_started = True

        if is_subset_started:
            subset.append(d)

        if is_subset_started and all(d[key] == end_condition[key] for key in end_condition):
            # Stop adding dictionaries to the subset
            break
    return subset


def has_key_value_pair(list_of_dicts, key, value):
    """
    Checks if a list of dictionaries contains a dictionary with a specific key-value pair.

    Args:
        list_of_dicts: The list of dictionaries to search.
        key: The key to search for.
        value: The value to search for.

    Returns:
        True if a dictionary with the specified key-value pair is found, False otherwise.
    """
    for my_dict in list_of_dicts:
        if key in my_dict and my_dict[key] == value:
            return True
    return False
