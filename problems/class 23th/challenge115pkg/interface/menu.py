purple = '\033[1;35m'
red = '\033[1;31m'
yellow = '\033[1;33m'
color_reset = "\033[m"
def line(msg):
    print("-" * 45)
    print(f"{msg.center(45)}")
    print("-" * 45)

def menu(options):
    line("MAIN MENU")
    c = 1
    for item in options:
        print(f"{yellow}{c}{color_reset} - {purple}{item}{color_reset}")
        c += 1
    print("-"*45)
    while True:
        try:
            op = int(input(f"{yellow}your option > {color_reset}"))
            if op > 3:
                print(f"{red}option out of range, pleace select a valid one{color_reset}")
            if op == 3:
                exit(f"{yellow}good bye{color_reset}")
            for c in range(1, 4):
                if op == c:
                    return op
        except(TypeError, ValueError):
            print(f"{red}invalid value, try again{color_reset}")
            continue
        except KeyboardInterrupt:
            exit(f"\n{yellow}good bye{color_reset}")