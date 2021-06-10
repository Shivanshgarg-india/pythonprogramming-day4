#  make_printer() function, which creates and returns a function. The nested printer() function is the closure.

def make_printer(msg):

    msg = "hi there"

    def printer():
        print(msg)

    return printer


myprinter = make_printer("Hello there")
myprinter()
myprinter()
myprinter()