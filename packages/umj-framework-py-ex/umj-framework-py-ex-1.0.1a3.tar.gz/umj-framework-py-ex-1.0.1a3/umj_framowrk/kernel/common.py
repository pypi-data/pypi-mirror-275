

def get_object_type(obj):
    ret = None

    # recursion err((
    # def contains_dict(obj, depth=0):
    #     try:
    #         if depth >= 3:
    #             return False
    #         depth += 1
    #         match obj:
    #             case dict():
    #                 return True
    #             case list():
    #                 return any(contains_dict(item, depth) for item in obj)
    #         return False
    #     except RecursionError:
    #         print('RECURSION' , obj)

    match obj:
        case obj if callable(obj):
            ret = 'func'
        case dict():
            ret = 'window'
        case list():
            if all(type(item) in [str, int, dict] for item in obj):
                ret = 'view'
            elif all(type(item) in [str, list] or callable(item) for item in obj):
                ret = 'scenario'
        case str():
            ret = 'action'
    return ret
