skaits = {}

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        limenis = rinda.split()[2]

        if: limenis in skaits: 
            skaits[limenis] += 1
        else: skaits [limenis] = 1

print("Limenu kopsavilkums")

for limenis in sorted(skaits,key =skaits.get, reverse=True):
    print (limenis,skaits[limenis]) 
