

def remove_duplicates(data):
    """
    Remove duplicates from the data.
    """

    return set(data)


lst=['a', 'b', 'c', 'a', 'b', 'c']

print(remove_duplicates(lst))
print(len(remove_duplicates(lst)))
