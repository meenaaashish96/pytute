#debugger

def debug(func):
    def wraper(*args, **kwargs):
        argsval = ', '.join(x for x in args)
        keyval = ', '.join(k+":"+v for k,v in kwargs.items())
        print(f"Arguments in {func.__name__} is {argsval} {keyval}")
        func(*args, **kwargs)
        print("function wrapeed")
    return wraper

@debug
def printhello(name, greet="hello"):
    print(f"{name} {greet}")

printhello("Aniket", greet="Hi")
