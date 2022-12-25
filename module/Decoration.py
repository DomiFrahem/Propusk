from typing import Any


class CleanUpdateData(object):
    def __init__(self, fun) -> None:
        self._fun = fun
        print(F"init with fuunction {fun.__name__}")

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(args)
        print(kwds)
        self._fun(*args, **kwds)


# def clean_and_update_data(*args, **kwds):
#     '''В классе где применяется этот декоратор, должны быть реализованны два метода: 
#         _clean_line_edit()
#         _load_data()
#         в противном случае будет ошибка
#     '''
#     def wrapper(func):
#         ret = func(*args)
#         # args[0]._clean_line_edit()
#         #    args[0]._load_data()

#         return ret
#     return wrapper
