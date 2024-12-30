from typing import Any, Callable


def log(filename: str = "") -> Callable[[str], Any]:
    """Декоратор логирования функции на ошибку или нет, создаёт файл если указать имя файла"""

    def decorator_log(func: Any) -> Callable[[Any], Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
            except Exception as error_type:
                if filename != "":
                    with open(f"{filename}.txt", "w") as file_log:
                        file_log.write(f"{func.__name__} error: {str(error_type)}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {str(error_type)}. Inputs: {args}, {kwargs}")
            else:
                if filename != "":
                    with open(f"{filename}.txt", "w") as file_log:
                        file_log.write(f"{func.__name__} ok")
                    return result
                else:
                    print(f"{func.__name__} ok")
                    return result

        return wrapper

    return decorator_log
