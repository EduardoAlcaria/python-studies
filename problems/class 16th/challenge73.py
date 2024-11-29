teams = (
    "Botafogo", "Palmeiras", "Internacional", "Fortaleza", "Flamengo", 
    "São Paulo", "Cruzeiro", "Bahia", "Corinthians", "Atlético-MG", 
    "Vasco", "Vitória", "Juventude", "Grêmio", "Athletico-PR", 
    "Fluminense", "Criciúma", "Bragantino", "Cuiabá", "Atlético-GO"
)
sor = sorted(teams)
print("-="*30)
for t in teams:
    print(f"{t}, ", end="")
print(f"\n{"-="*30}")
for t in range(0, 5):
    print(f"{teams[t]} ", end="")
print(f"\n{"-="*30}")
for t in range(4, 0, -1):
    print(f"{teams[-t]} ", end="")
print(f"\n{"-="*30}")
for t in range(0, len(teams)):
    print(f"{sor[t]} ",end="")
print(f"\n{"-="*30}")
print(f"the team Internacional is in {teams.index("Internacional") + 1}th position")
print(f"{"-="*30}")
