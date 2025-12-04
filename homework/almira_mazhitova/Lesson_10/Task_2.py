def repeat_me(func):
    def repeater(text, count):
        counter = 1
        while counter <= count:
            func(text)
            counter += 1

    return repeater


@repeat_me
def example(text):
    print(text)


example('print me', count=2)


def repeat_me_new(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat_me_new(count=5)
def example1(text):
    print(text)


example1('hello')
