try:
    a = int(input("a: "))
    b = int(input("b: "))
    r = a/b
except (ValueError, TypeError):
    print("we had a problem with the values")
except ZeroDivisionError:
    print("it not possible to split a number by 0")
except KeyboardInterrupt:
    print("the user choose to exit")
except Exception as error:
    print(f"the error was {error}")
else:
    print(r)
finally:
    print("always come back")