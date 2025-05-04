# Kursinis

# Kursinio darbo ataskaita: Krovinių sandėlio modeliavimas

## 1. Įvadas

* **Kursinio darbo tikslas:** Šio kursinio darbo tikslas buvo sukurti Python programą, kuri parodytų duomenų struktūrą (`Stack`) tema. Darbo metu taip pat buvo siekiama įgyvendinti visus keturis pagrindinius OOP principus: inkapsuliaciją, abstrakciją, paveldimumą ir polimorfizmą, bei pritaikyti kompozicijos ir agregacijos principus.
* **Darbo tema:** Darbo tema yra krovinių sandėlio modeliavimas, kuriame naudojama LIFO (paskutinis įėjo, pirmas išėjo) principo duomenų struktūra. 
* **Mano programa** Mano sukurta programa yra krovinių sandėlio modeliavimo programa. Ji leidžia vartotojui valdyti krovinių sandėlį, priimti naujus krovinius, išduoti juos ir peržiūrėti viršutinį krovinį. 
* **Kaip paleisti programą?** Norint paleisti programą, reikia turėti įdiegtą Python 3, taip pat reikia išsaugoti pateiktą kodo failą (pvz., pavadinimu `sandėlys.py`). Ir tai atlikus paleisti programą.
* **Kaip naudoti programą?** Paleidus programą, konsolėje bus rodomi įvairūs veiksmai su krovinių sandėliu: pradinė būsena, krovinių priėmimas, išdavimas, viršutinio krovinio peržiūra, sandėlio dydis ir kt. Taip pat bus pademonstruotas dekoratorių veikimas – maksimalaus krovinių skaičiaus stebėjimas ir galimybė atšaukti paskutinį veiksmą. 

## 2. Analizė

* **Programos atitikimas funkciniams reikalavimams:**

    * **Stack klasė:** Programa pavaizduoja `Stack` klasę, kuri atitinka (paskutinis įėjo, pirmas išėjo) duomenų struktūros principą. Ji turi metodus `push()` (prideda elementą į viršų), `pop()` (pašalina ir grąžina viršutinį elementą) ir `peek()` (grąžina viršutinį elementą jo nepašalindama).

      ```python
      class Stack:
          def __init__(self):
              self._items = []

          def push(self, item):
              self._items.append(item)

          def pop(self):
              if not self.is_empty():
                  return self._items.pop()
              raise IndexError("išimti iš tuščio sandėlio")

          def peek(self):
              if not self.is_empty():
                  return self._items[-1]
              raise IndexError("peržiūrėti tuščią sandėlį")

          def is_empty(self):
              return not self._items

          def size(self):
              return len(self._items)
      ```

    * **OOP principai:**

        * **Inkapsuliacija:** `Stack` klasės vidinė būsena (`_items`) yra paslėpta ir prieinama tik per klasės metodus, užtikrinant duomenų vientisumą.
        * **Abstrakcija:** `SandėlioDekoratorius` yra abstrakti bazinė klasė, kuri apibrėžia bendrą dekoratorių sąsają, tačiau nekeičia konkretaus veikimo. 

          ```python
          from abc import ABC, abstractmethod

          class SandėlioDekoratorius(ABC):
              def __init__(self, sandėlys):
                  self._sandėlys = sandėlys

              @abstractmethod
              def is_empty(self):
                  pass
              # ... kiti abstraktūs metodai ...
          ```

        * **Paveldimumas:** Konkrečios dekoratorių klasės (`MaxKroviniųSkaičiausDekoratorius`, `AtšaukiamasSandėlioDekoratorius`) paveldi iš `SandėlioDekoratorius`, perimdamos bendrą sąsają ir pavaizduodamos specifinį funkcionalumą.

          ```python
          class MaxKroviniųSkaičiausDekoratorius(SandėlioDekoratorius):
              # ... implementacija ...

          class AtšaukiamasSandėlioDekoratorius(SandėlioDekoratorius):
              # ... implementacija ...
          ```

        * **Polimorfizmas:** Funkcija `apdoroti_sandėlio_objektą` gali priimti įvairių tipų sandėlio objektus (tiek paprastą `Stack`, tiek dekoruotus sandėlius) ir vienodai su jais veikti (pvz., `push`, `pop`), nes jie visi turi bendrą sąsają.

          ```python
          class Krovinys: # Tik pavyzdys, jei naudojate Krovinio klasę
              def __init__(self, pavadinimas):
                  self.pavadinimas = pavadinimas

          def apdoroti_sandėlio_objektą(sandėlio_obj):
              sandėlio_obj.push(Krovinys("Universalus krovinys"))
              # ...
          ```

    * **Decorator šablonas:** Programa naudoja Dekoratoriaus dizaino šabloną, leidžiantį dinamiškai pridėti naują veikimą prie `Stack` objektų (pvz., maksimalaus dydžio stebėjimą, atšaukimo galimybę) nekeičiant pačios `Stack` klasės.

      ```python
      max_dydžio_sandėlys = MaxKroviniųSkaičiausDekoratorius(Stack())
      atšaukiamas_sandėlys = AtšaukiamasSandėlioDekoratorius(Stack())
      ```

    * **Kompozicija ir agregacija:**

        * **Kompozicija:** Dekoratoriai (`MaxKroviniųSkaičiausDekoratorius`, `AtšaukiamasSandėlioDekoratorius`) "turi" vidinį `Stack` objektą ir yra nuo jo priklausomi.
        * **Agregacija:** `Stack` klasė apibendrina `Krovinys` objektus. `Stack` "turi" krovinius, tačiau `Krovinys` objektai gali egzistuoti ir be `Stack`.

## 3. Rezultatai ir apibendrinimas

* Sukurta programa sėkmingai pavaizduoja `Stack` duomenų struktūrą.
* Buvo sėkmingai pademonstruoti visi keturi objektinio programavimo principai (inkapsuliacija, abstrakcija, paveldimumas ir polimorfizmas) per programos struktūrą ir veikimą.
* Pritaikytas Dekoratoriaus dizaino šablonas leido praplėsti `Stack` klasės funkcionalumą nekeičiant pagrindinės klasės kodo.
* **Išvados:** Šis darbas atliktas sėkmingai. Buvo sukurta krovinių sandėlio programa, kuri parodo svarbius objektinio programavimo principus. Programa yra geras pavyzdys, demonstruojantis duomenų struktūros kūrimą.
* **Būsimos programos plėtros galimybės:** Programą galima tobulinti įvairiais būdais. Pavyzdžiui, pridėti sandėlio dydžio ribojimą, krovinių registravimą. Taip pat būtų patogu padaryti galimybę išsaugoti ir atidaryti sandėlio duomenis.

