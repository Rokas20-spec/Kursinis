from krovinys import Krovinys
from stack import Stack
from dekoratorius import MaxKroviniųSkaičiausDekoratorius, AtšaukiamasSandėlioDekoratorius
from valdytojas import SandėlioValdytojas
def apdoroti_sandėlio_objektą(sandėlio_obj, file):
    file.write(f"\nApdorojamas sandėlys: {sandėlio_obj}\n")
    naujas_krovinys = Krovinys("Universalus krovinys")
    sandėlio_obj.push(naujas_krovinys)
    file.write(f"Įdėtas: {naujas_krovinys}, Sandėlys: {sandėlio_obj}\n")
    if not sandėlio_obj.is_empty():
        viršutinis = sandėlio_obj.peek()
        file.write(f"Viršutinis krovinys: {viršutinis}\n")
        sandėlio_obj.pop()
        file.write(f"Išimtas viršutinis krovinys, sandėlys: {sandėlio_obj}\n")

with open("rezultatai.txt", "w", encoding="utf-8") as f:
    f.write("--- Paprastas sandėlys ---\n")
    s = Stack()
    s.push(Krovinys("Televizorius"))
    s.push(Krovinys("Šaldytuvas"))
    f.write(str(s) + "\n")

    f.write("\n--- Sandėlys su maksimaliu dydžiu ---\n")
    max_s = MaxKroviniųSkaičiausDekoratorius(Stack())
    max_s.push(Krovinys("Stalas"))
    max_s.push(Krovinys("Kėdė"))
    max_s.pop()
    f.write(str(max_s) + "\n")
    f.write(f"Maksimalus dydis: {max_s.get_max_dydis()}\n")

    f.write("\n--- Atšaukiamas sandėlys ---\n")
    ats = AtšaukiamasSandėlioDekoratorius(Stack())
    ats.push(Krovinys("K1"))
    ats.pop()
    ats.atšaukti()
    f.write(str(ats) + "\n")

    f.write("\n--- Polimorfizmas ---\n")
    apdoroti_sandėlio_objektą(s, f)
    apdoroti_sandėlio_objektą(max_s, f)
    apdoroti_sandėlio_objektą(ats, f)

    f.write("\n--- Valdytojas ---\n")
    valdytojas = SandėlioValdytojas(s)
    valdytojas.pridėti_krovinį(Krovinys("Dokumentai"), f)
    valdytojas.išduoti_krovinį(f)