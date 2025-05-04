class Stack:
    """
    Implementuoja Last-In, First-Out (LIFO) duomenų struktūrą (dėklą), skirtą
    kroviniams sandėliuoti.
    """
    def __init__(self):
        """
        Inicijuoja tuščią dėklą (sandėlį).
        """
        self._items = []

    def is_empty(self):
        """
        Patikrina, ar sandėlis yra tuščias (neturi krovinių).
        Grąžina True, jei tuščias, False priešingu atveju.
        """
        return not self._items

    def push(self, item):
        """
        Prideda krovinį (item) į sandėlio viršų.
        """
        self._items.append(item)

    def pop(self):
        """
        Pašalina ir grąžina viršutinį krovinį iš sandėlio.
        Kelia IndexError, jei sandėlis yra tuščias.
        """
        if self.is_empty():
            raise IndexError("išimti iš tuščio sandėlio")
        return self._items.pop()

    def peek(self):
        """
        Grąžina viršutinį krovinį sandėlyje, jo nepašalindamas.
        Kelia IndexError, jei sandėlis yra tuščias.
        """
        if self.is_empty():
            raise IndexError("peržiūrėti tuščią sandėlį")
        return self._items[-1]

    def size(self):
        """
        Grąžina dabartinį krovinių skaičių sandėlyje.
        """
        return len(self._items)

    def __len__(self):
        """
        Leidžia naudoti built-in funkciją len() su Stack objektu.
        """
        return self.size()

    def __str__(self):
        """
        Grąžina gražų sandėlio atvaizdavimą eilutėje, rodantį krovinius nuo viršaus.
        """
        return f"Sandėlis (viršus -> apačia): {[str(item) for item in reversed(self._items)]}"

    def __repr__(self):
        """
        Grąžina oficialų Stack objekto atvaizdavimą.
        """
        return f"Stack(items={self._items})"