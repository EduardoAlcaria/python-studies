gen = ""
while gen != "m" and gen != "f":
    gen = str(input("Type your gender [m/f]: ")).lower()
    if gen != "m" and gen != "f":
        print("Unknown gender, try again")
print("Valid gender")