from krovinys import Krovinys

class SandėlioValdytojas:
    def __init__(self, sandėlys):
        self._sandėlys = sandėlys

    def pridėti_krovinį(self, krovinys, file=None):
        self._sandėlys.push(krovinys)
        pranešimas = f"Valdytojas: į sandėlį pridėtas {krovinys}\n"
        if file:
            file.write(pranešimas)
        else:
            print(pranešimas.strip())

    def išduoti_krovinį(self, file=None):
        if not self._sandėlys.is_empty():
            krovinys = self._sandėlys.pop()
            pranešimas = f"Valdytojas: iš sandėlio išduotas {krovinys}\n"
            if file:
                file.write(pranešimas)
            else:
                print(pranešimas.strip())
            return krovinys
        else:
            pranešimas = "Valdytojas: sandėlis tuščias.\n"
            if file:
                file.write(pranešimas)
            else:
                print(pranešimas.strip())
            return None