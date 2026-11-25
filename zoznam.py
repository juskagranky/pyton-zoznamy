"""suciastky = ["rezistor", "kondenzator", "dioda","tranzistor", "rele"]
print(type(suciastky))
print(suciastky)
print(suciastky[0])
print(suciastky[1:4])
print(len(suciastky) -1)
suciastky.append("poistka")
print(suciastky)
suciastky.insert(1, "poistka")
print(suciastky)
suciastky.extend(["spinac","poistka"])
print(suciastky)
suciastky.remove("poistka")
print(suciastky)
odobrane = suciastky.pop()
print(odobrane)
print(suciastky)
novylist = []
novylist.append(suciastky.pop())
print(novylist)"""
"""merania = [4,5,8,22,3,11]
vysoke = []
for i in merania [:]:
    if i > 10:
        vysoke.append(i)
        merania.remove(i)

print("ostali:", merania)
print("vysoke:", vysoke)"""
sklad = ["rezistor", "kondenzator", "dioda", "tranzistor", "rele"]
rasto = []
print("Pocet suciastok:", len(sklad))
print("Prva:", sklad[0])
print("Posledná:", sklad[-1])
sklad.append("poistka")
sklad.insert(0, "cievka")
sklad.remove("dioda")
sklad[0], sklad[-1] = sklad[-1], sklad[0]
rasto.append(sklad.pop())

for i, s in enumerate(sklad, start=1):
    print(f"{i}. {s}")


print("Na oprave:", rasto)


nazov = input("Zadaj suciastku: ")
if nazov in sklad:
    sklad.remove(nazov)
    print("Vydane.")
else:
    print("Na sklade nie je.")