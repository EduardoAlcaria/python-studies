from challenge111p.datapkg import money
from challenge111p.coinpkg import summary

r = money.readmoney("Type a price $")
summary(r, 35, 32)