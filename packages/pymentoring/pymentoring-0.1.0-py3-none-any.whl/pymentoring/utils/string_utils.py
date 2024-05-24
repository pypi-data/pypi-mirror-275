def assert_valid_str(arg) -> str:
    return assert_valid_type(arg, str)


def assert_valid_type(arg, type_info):
    if arg is None or not isinstance(arg, type_info):
        raise TypeError("Argument expected to be valid " + type_info.__name__)
    else:
        return arg
