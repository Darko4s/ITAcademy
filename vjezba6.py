#spoji stringove u listama da pise:
# Plavo:Nebo
# Bijelo:Auto
# Zelen:Grm
# Zuto:Sunce
# Crn:Asfalt

boje = ["Plavo", "Bijelo","Zelen", "Zuto", "Crn"]
ostalo = ["Nebo", "Auto", "Grm", "Sunce", "Asfalt"]

#1. nacin
for i in range(len(boje)):
    print("{}:{} \n".format(boje[i],ostalo[i]), end="")

#2. nacin
for i in range(len(boje)):
    print(f"{boje[i]}:{ostalo[i]}\n", end="")


