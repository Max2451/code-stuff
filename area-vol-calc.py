def clear():
    print(
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

class MathCalc:
    @staticmethod
    def area3D():
        rv = 0
        pi = 3.14
        tipe = input("Pon el tipo de figura\nTipos de figura disponibles:\n¬ Prisma\n¬ Cilindro\n\nElije la figura: ")
        type = tipe.lower()
        if type.startswith("prisma"):
            clear()
            faces = int(input("Pon las caras del prisma (sin contar las bases) "))
            base = float(input("Pon la longitud de la base: "))
            try:
                base2 = float(input("Pon la segunda longitud de la base (para los rectángulos) "))
            except:
                base2 = 0.0 + base
            height = float(input("Pon la altura: "))
            if base != base2 and faces % 2 == 0:
                rv = ((base * height) * (faces / 2)) + ((base2 * height) * (faces / 2)) + ((base * base2) * 2)
            elif faces == 3:
                rv = ((base * height) * faces) + (((base * base) / 2) * 2)
            else:
                rv = ((base * height) * faces) + ((base * base) * 2)
        elif type.startswith("cilindro"):
            clear()
            d = float(input("Pon el diámetro del cilindro: "))
            h = float(input("Pon la altura del cilindro: "))
            r = d / 2
            rv = ((2 * pi) * r) * (r + h)
        if str(rv).__contains__("."):
            n_rv = str(rv).split(".")
            print(f"Area = {n_rv[0]}.{n_rv[1][0:2]}")
        else:
            print(f"Area = {rv}")

    @staticmethod
    def vol3D():
        rv = 0
        pi = 3.14
        tipe = input("Pon el tipo de figura\nTipos de figura disponibles:\n¬ Prisma\n¬ Cilindro\n\nElije la figura: ")
        type = tipe.lower()
        if type.startswith("prisma"):
            clear()
            faces = int(input("Pon las caras del prisma (sin contar las bases) "))
            base = float(input("Pon la longitud de la base: "))
            try:
                base2 = float(input("Pon la segunda longitud de la base (para los rectángulos) "))
            except:
                base2 = 0.0 + base
            height = float(input("Pon la altura: "))
            if base != base2:
                rv = (base * base2) * height
            elif faces == 3:
                rv = ((base * height) / 2) * base2
            else:
                rv = (base * base) * height
        elif type.startswith("cilindro"):
            clear()
            faces = 2
            d = float(input("Pon el diametro del cilindro: "))
            r = d/2
            h = float(input("Pon la altura del cilindro: "))
            rv = pi * (r ** 2) * h
        
        if str(rv).__contains__("."):
            n_rv = str(rv).split(".")
            if len(str(n_rv[1])) > 2:
                print(f"Vol = {n_rv[0]}.{n_rv[1][0:2]} cm^3")
            else:
                print(f"Vol = {n_rv[0]}.{n_rv[1]} cm^3")
        else:
            print(f"Vol = {rv} cm^3")

loop = True
while loop:
    clear()
    func = input("Area3D or Vol3D : ")
    fu = func.lower()
    if fu.startswith("area3d") or fu.startswith("a3"):
        MathCalc.area3D()
    elif fu.startswith("vol3d") or fu.startswith("v3"):
        MathCalc.vol3D()
    elif fu in ["stop", "end", "break"]:
        loop = False
    else:
        print("Incorrect Method.")
    input()