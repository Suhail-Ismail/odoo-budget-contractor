def choices_tuple(choices, is_sorted=True):
    choices = [(i.lower(), i.upper()) for i in choices]

    if is_sorted:
        return sorted(choices, key = lambda tup: tup[0])

    return choices