def finish_me(func):
    def wrapper(*args):
        returned_func = func(*args)
        print('finished')
        return returned_func

    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')
