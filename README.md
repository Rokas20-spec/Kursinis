# Kursinis

# Kursinio darbo ataskaita: Krovinių sandėlio modeliavimas

## 1. Įvadas

* **Kursinio darbo tikslas:** Šio darbo tikslas buvo sukurti Python programą. Ji turėjo parodyti, kaip veikia objektinis programavimas (OOP). Programoje sukūriau duomenų struktūrą, vadinamą `Stack`. Paskui pridėjau jai naujų galimybių, naudodamas Dekoratoriaus dizaino šabloną. Taip pat norėjau panaudoti visus keturis pagrindinius OOP principus: duomenų slėpimą (inkapsuliaciją), bendrų savybių išskyrimą (abstrakciją), galimybę vienoms klasėms perimti kitų savybes (paveldimumą) ir galimybę skirtingiems objektams veikti panašiai (polimorfizmą). Be to, pritaikiau kompozicijos ir agregacijos principus.
* **Darbo tema:** Darbo tema yra krovinių sandėlio modelis. Jame naudojau LIFO (paskutinis įdėtas, pirmas išimtas) principą. Šią temą pasirinkau, kad galėčiau praktiškai panaudoti OOP žinias ir sukurti programą, kuri imituotų realų pasaulio veiksmą.
* **Kas yra jūsų aplikacija?** Mano sukurta aplikacija yra programa, kuri modeliuoja krovinių sandėlį. Ji leidžia vartotojui valdyti sandėlį: priimti naujus krovinius, išduoti juos (pagal LIFO principą) ir pažiūrėti, koks krovinys yra viršuje. Be to, naudodamas Dekoratoriaus šabloną, padariau taip, kad programa galėtų sekti, kiek daugiausiai krovinių vienu metu buvo sandėlyje, ir atšaukti paskutinį priėmimo ar išdavimo veiksmą.
* **Kaip paleisti programą?** Norint paleisti programą, jūsų kompiuteryje turi būti įdiegta Python 3 programa. Išsaugokite kodo failą (galite pavadinti jį `sandėlys.py`). Atidarykite komandinę eilutę (arba terminalą), nueikite į tą vietą, kur išsaugojote failą, ir įrašykite komandą: `python sandėlys.py`. Programa pradės veikti ir parodys pagrindinius savo veiksmus ir rezultatus komandinėje eilutėje.
* **Kaip naudoti programą?** Kai programa veikia, komandinėje eilutėje matysite įvairius veiksmus su krovinių sandėliu: kaip jis atrodo pradžioje, kaip priimami kroviniai, kaip jie išduodami, koks krovinys yra viršuje, koks yra sandėlio dydis ir panašiai. Taip pat pamatysite, kaip veikia dekoratoriai – kaip stebimas didžiausias krovinių skaičius ir kaip galima atšaukti paskutinį veiksmą. Jei norite naudoti programos dalis savo kode, galite importuoti `Stack` klasę ir kurti jos objektus. Tada galite naudoti jos funkcijas (`push`, `pop`, `peek`, `is_empty`, `size`). Kad pridėtumėte dekoratorių funkcijas, turite apgaubti `Stack` objektą dekoratoriaus klasės objektu (pavyzdžiui, `max_dydžio_sandėlys = MaxKroviniųSkaičiausDekoratorius(Stack())`).

## 2. Analizė

* **Programos atitikimas funkcijoms:**

    * **Stack klasė:** Programa turi `Stack` klasę. Ji veikia pagal LIFO (paskutinis įdėtas, pirmas išimtas) principą. Ji turi funkcijas `push()` (įdeda elementą į viršų), `pop()` (pašalina ir grąžina viršutinį elementą) ir `peek()` (grąžina viršutinį elementą, bet jo nepašalina).

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

        * **Inkapsuliacija:** `Stack` klasės vidiniai duomenys (`_items`) yra paslėpti. Juos galima pasiekti tik per klasės funkcijas. Tai padeda apsaugoti duomenis nuo netinkamo naudojimo.
        * **Abstrakcija:** `SandėlioDekoratorius` yra kaip bendras planas visiems dekoratoriams. Jis apibrėžia, kokias pagrindines funkcijas turės dekoratoriai, bet nepasako, kaip konkrečiai jie veiks. Tai leidžia kurti įvairius dekoratorius, kurie prideda skirtingų galimybių sandėliui.

          ```python
          from abc import ABC, abstractmethod

          class SandėlioDekoratorius(ABC):
              def __init__(self, sandėlys):
                  self._sandėlys = sandėlys

              @abstractmethod
              def is_empty(self):
                  pass
              # ... kitos bendros funkcijos ...
          ```

        * **Paveldimumas:** Konkrečios dekoratorių klasės (`MaxKroviniųSkaičiausDekoratorius`, `AtšaukiamasSandėlioDekoratorius`) paveldi savybes iš `SandėlioDekoratorius`. Jos perima bendrą planą ir prideda savo specifinį veikimą.

          ```python
          class MaxKroviniųSkaičiausDekoratorius(SandėlioDekoratorius):
              # ... kaip veikia maksimalaus krovinių skaičiaus stebėjimas ...

          class AtšaukiamasSandėlioDekoratorius(SandėlioDekoratorius):
              # ... kaip veikia atšaukimo galimybė ...
          ```

        * **Polimorfizmas:** Funkcija `apdoroti_sandėlio_objektą` gali dirbti su įvairiais sandėlio objektais (tiek su paprastu `Stack`, tiek su dekoruotais sandėliais). Ji gali vienodai naudoti jų funkcijas (`push`, `pop`), nes jie visi turi bendras pagrindines savybes.

          ```python
          class Krovinys: # Pavyzdys, jei naudojate Krovinio klasę
              def __init__(self, pavadinimas):
                  self.pavadinimas = pavadinimas

          def apdoroti_sandėlio_objektą(sandėlio_obj):
              sandėlio_obj.push(Krovinys("Universalus krovinys"))
              # ... kiti veiksmai ...
          ```

    * **Decorator šablonas:** Programa naudoja Dekoratoriaus dizaino šabloną. Tai leidžia dinamiškai pridėti naujų funkcijų prie `Stack` objektų (pavyzdžiui, stebėti didžiausią dydį, leisti atšaukti veiksmus) nekeičiant pačios `Stack` klasės kodo.

      ```python
      max_dydžio_sandėlys = MaxKroviniųSkaičiausDekoratorius(Stack())
      atšaukiamas_sandėlys = AtšaukiamasSandėlioDekoratorius(Stack())
      ```

    * **Kompozicija ir agregacija:**

        * **Kompozicija:** Dekoratoriai (`MaxKroviniųSkaičiausDekoratorius`, `AtšaukiamasSandėlioDekoratorius`) turi viduje `Stack` objektą ir yra nuo jo priklausomi.
        * **Agregacija:** `Stack` klasė turi `Krovinys` objektus. `Stack` "turi" krovinius, bet `Krovinys` objektai gali egzistuoti ir be `Stack`.

## 3. Rezultatai ir apibendrinimas

* Sukurta programa sėkmingai modeliuoja krovinių sandėlį pagal LIFO principą, naudodama `Stack` duomenų struktūrą.
* Programos struktūra ir veikimas gerai parodo visus keturis objektinio programavimo principus (inkapsuliaciją, abstrakciją, paveldimumą ir polimorfizmą).
* Pritaikytas Dekoratoriaus dizaino šablonas leido lengvai pridėti naujų galimybių `Stack` klasei, tokių kaip maksimalaus dydžio stebėjimas ir atšaukimo galimybė, nekeičiant pagrindinio klasės kodo.
* **Iššūkiai:** Vienas sunkumas buvo gerai suplanuoti, kaip veiks dekoratoriai ir kaip jie derės su pagrindine `Stack` klase bei vienas su kitu (nors šiame darbe dekoratoriai naudojami atskirai).
* **Išvados:** Šis darbas pasiekė savo tikslus. Sukūriau veikiantį krovinių sandėlio modelį, kuris parodo svarbius objektinio programavimo principus ir Dekoratoriaus šablono privalumus. Sukurta programa yra geras pavyzdys, kaip kurti duomenų struktūras ir plėsti jų galimybes naudojant OOP metodus.
* **Būsimos programos galimybės:** Programą būtų galima toliau tobulinti. Pavyzdžiui, būtų galima tiesiogiai `Stack` klasėje arba per atskirą dekoratorių nustatyti maksimalų sandėlio dydį. Taip pat būtų galima sukurti kitus dekoratorius, pavyzdžiui, skirtus registruoti krovinius (kas ir kada įdėjo/išėmė), nustatyti prioritetus (nors tai prieštarautų LIFO principui, bet galėtų būti kaip papildoma funkcija) arba leisti atšaukti kelis paskutinius veiksmus. Be to, būtų galima sukurti patogesnį valdymą per grafinę arba tekstinę vartotojo sąsają. Galiausiai, būtų galima pridėti galimybę išsaugoti ir vėl įkelti sandėlio būseną iš failo.
