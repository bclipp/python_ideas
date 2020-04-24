import time


def do_something():
    print("This is a test")
    time.sleep(10)
    print("This is a test")
    time.sleep(10)
    print("This is a test")
    time.sleep(10)
    print("This is a test")
    time.sleep(10)
    print("This is a test")
    time.sleep(10)


class BreakManager():
    def take_break(self):
        time.sleep(10)


def do_something_refactor(break_manager):
    print("This is a test")
    break_manager.take_break()
    print("This is a test")
    break_manager.take_break()
    print("This is a test")
    break_manager.take_break()
    print("This is a test")
    break_manager.take_break()
    print("This is a test")
    break_manager.take_break()
