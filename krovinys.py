class Krovinys:
    """
    Reprezentuoja vieną krovinį sandėlyje. Kiekvienas krovinys turi pavadinimą.
    """
    def __init__(self, pavadinimas):
        """
        Inicijuoja Krovinys objektą su nurodytu pavadinimu.
        """
        self.pavadinimas = pavadinimas

    def __str__(self):
        """
        Grąžina gražų krovinio atvaizdavimą, kai naudojama funkcija str().
        """
        return f"Krovinys: {self.pavadinimas}"

    def __repr__(self):
        """
        Grąžina oficialų krovinio atvaizdavimą, tinkamą atvaizdavimui ir testavimui.
        """
        return f"Krovinys(pavadinimas='{self.pavadinimas}')"