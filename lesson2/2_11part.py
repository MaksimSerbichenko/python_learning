def check_instance(obj, cls):
    return check_subclass(type(obj), cls)


def check_subclass(child, base):
    if child == base:
        return True

    for direct_base in child.__basses__:
        if base == direct_base:
            return True
        return check_subclass(direct_base, base)
    
    return False
