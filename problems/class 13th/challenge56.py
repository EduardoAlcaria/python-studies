old_name = ""
fem_lees = 0
old_man = 0
group_age = 0
for c in range(1, 5):
    print(f"----- {c} person -----")
    name = str(input("Name: ")).strip()
    age = int(input("Age: ")) 
    group_age += age 
    gen = str(input("Gender [M/F]: ")).lower().strip() 
    if gen == "f" and age < 20: 
        fem_lees += 1
    if c == 1: 
        old_man = age
        old_name = name
    else:
        if age > old_man and gen == "m": 
            old_man = age
            old_name = name
    
print(f"the avarege group age is {group_age/4}")
print(f"the older man has {old_man} years old and his name is {old_name.capitalize()}")
print(f"there are {fem_lees} womans with age bellow 20 years old")
