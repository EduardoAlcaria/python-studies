s = str(input("Type a sentence: ")).strip().upper()
splited = s.split()
tog = ''.join(splited)
invert = ''
for c in range(len(tog) - 1, -1, -1):
    invert += tog[c]
if invert == tog:
    print("Its a palindromo")
else:
    print("its not a palindromo")