colors = {"green": '\033[7;32m',
          "color_reset": '\033[m'}
def line(msg):
    l = len(msg) + 4
    print(colors['green'])
    print("~" * l)
    print(f"  {msg}  ")
    print("~" * l)
    print(colors['color_reset'])
def syshelp(command):
    help(command)
line("PyHELP system helper, Type EXIT to end")
while True:
    h = str(input("Function or library : "))
    if h.upper() == "EXIT":
        break
    else:
        syshelp(h)