from abc import ABC, abstractmethod
from stack import Stack


class SandėlioDekoratorius(ABC):
    """
    Abstrakti bazinė klasė, skirta dekoruoti Stack objektus (sandėlius) ir pridėti
    papildomų savybių ar elgsenos.
    """
    def __init__(self, sandėlys):
        """
        Inicijuoja dekoratorių su Stack objektu (sandėliu).
        """
        self._sandėlys = sandėlys

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def push(self, krovinys):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

# Konkretus dekoratorius, stebintis maksimalų kada nors sandėlyje buvusių krovinių skaičių
class MaxKroviniųSkaičiausDekoratorius(SandėlioDekoratorius):
    """
    Dekoratorius, kuris prideda galimybę stebėti didžiausią kada nors pasiektą
    krovinių skaičių sandėlyje.
    """
    def __init__(self, sandėlys):
        super().__init__(sandėlys)
        self._max_dydis = 0

    def push(self, krovinys):
        self._sandėlys.push(krovinys)
        self._max_dydis = max(self._max_dydis, self._sandėlys.size())

    def pop(self):
        return self._sandėlys.pop()

    def peek(self):
        return self._sandėlys.peek()

    def is_empty(self):
        return self._sandėlys.is_empty()

    def size(self):
        return self._sandėlys.size()

    def get_max_dydis(self):
        """
        Grąžina maksimalų kada nors sandėlyje buvusių krovinių skaičių.
        """
        return self._max_dydis

    def __len__(self):
        return len(self._sandėlys)

    def __str__(self):
        return f"{str(self._sandėlys)} (Maksimalus krovinių skaičius: {self._max_dydis})"

    def __repr__(self):
        return f"MaxKroviniųSkaičiausDekoratorius(sandėlys={repr(self._sandėlys)})"

# Konkretus dekoratorius, leidžiantis atšaukti paskutinį krovinio priėmimą ar išdavimą
class AtšaukiamasSandėlioDekoratorius(SandėlioDekoratorius):
    """
    Dekoratorius, kuris suteikia galimybę atšaukti paskutinę 'push' arba 'pop' operaciją sandėlyje.
    """
    def __init__(self, sandėlys):
        super().__init__(sandėlys)
        self._istorija = []

    def push(self, krovinys):
        self._sandėlys.push(krovinys)
        self._istorija.append(('push', krovinys))

    def pop(self):
        try:
            krovinys = self._sandėlys.pop()
            self._istorija.append(('pop', krovinys))
            return krovinys
        except IndexError:
            raise

    def atšaukti(self):
        """
        Atšaukia paskutinę 'push' arba 'pop' operaciją.
        """
        if self._istorija:
            operacija, duomenys = self._istorija.pop()
            if operacija == 'push':
                if not self._sandėlys.is_empty():
                    self._sandėlys.pop()
            elif operacija == 'pop':
                self._sandėlys.push(duomenys)

    def peek(self):
        return self._sandėlys.peek()

    def is_empty(self):
        return self._sandėlys.is_empty()

    def size(self):
        return self._sandėlys.size()

    def __len__(self):
        return len(self._sandėlys)

    def __str__(self):
        return f"{str(self._sandėlys)} (Galima atšaukti paskutinį veiksmą)"

    def __repr__(self):
        return f"AtšaukiamasSandėlioDekoratorius(sandėlys={repr(self._sandėlys)})"