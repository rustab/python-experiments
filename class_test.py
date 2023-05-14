import sys
import io


class printHello:
    def __init__(this, woami: str) -> None:
        this.woami = woami

    def sayHello(this):
        print("Hello there")
        print(this.woami)

if __name__ == "__main__":
    myObject = printHello("I am who I am")
    myObject.sayHello()

    print("Standard stdout: Hello")
    temp_stdout = io.StringIO()
    sys.stdout = temp_stdout
    print("Hello I am in a in-memory buffer.")
    
    sys.stdout = sys.__stdout__
    print(temp_stdout.getvalue())
