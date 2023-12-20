# Projekt rozwija się i postanowiłem zbierać informacje o wydatkach, tym razem wykorzystując
# namedtuple. Dla łatwiejszej obsługi wprowadzam klasę, która gromadzi wydatki w formie prostej listy
# oraz zapewnia podstawowe zestawienia.

from collections import namedtuple, defaultdict

Zakup = namedtuple('Zakup',
                   'product quantity price market category',
                   defaults=(None, None))


class Wydatki:
    """
    Gromadzi wydatki związane ze świętami oraz zapewnia proste statystyki.
    """
    def __init__(self):
        self.wydatki = []

    def __len__(self):
        return len(self.wydatki)

    def __getitem__(self, w):
        return self.wydatki[w]

    def __add__(self, wydatek):
        if isinstance(wydatek, Zakup):
            self.wydatki.append(wydatek)
            return self
        else:
            raise TypeError('Możesz dodawać wyłącznie `Zakup` do listy wydatków.')

    def razem(self):
        return round(sum(i[2] for i in self.wydatki), 2)

    def razem_po_kategorii(self):
        # calculates sums per category
        kategorie = defaultdict(float)
        for w in self.wydatki:
            kategorie[w[-1]] += w[2]
        # sorts descending by amounts spent per category
        kategorie = sorted(kategorie.items(), key=lambda i: i[1], reverse=True)
        # prepares a string for more readable spending representation
        kategorie_as_string = '\nWydatki w podziale na kategorie:\n-------------------------------\n'
        for k, w in kategorie:
            if len(k) < 6:
                kategorie_as_string += f'{k}:\t\t{round(w, 2)}\n'
            else:
                kategorie_as_string += f'{k}:\t{round(w, 2)}\n'
        # returns the result (needs to be printed out)
        return kategorie_as_string


if __name__ == "__main__":

    wydatki = Wydatki()
    wydatki += Zakup('włoszczyzna', 4, 15.95, 'Biedronka', 'warzywa')
    wydatki += Zakup('miód wielokwiatowy', 2, 25.98, 'Biedronka', 'wypieki')
    wydatki += Zakup('makowiec', .600, 15.99, 'Biedronka', 'wypieki')
    wydatki += Zakup('mąka kukurydziana', 1, 8.99, 'Carrefour', 'wypieki')
    wydatki += Zakup('mąka ryżowa', 1, 9.99, 'Carrefour', 'wypieki')
    wydatki += Zakup('cukier Dr.Oetker', 1, 3.79, 'Carrefour', 'wypieki')
    wydatki += Zakup('lubczyk kamis', 1, 1.89, 'Carrefour', 'przyprawy')
    wydatki += Zakup('kmin rzymski', 1, 2.05, 'Carrefour', 'przyprawy')
    wydatki += Zakup('zioła prowansalskie prymat', 1, 1.49, 'Carrefour', 'przyprawy')
    wydatki += Zakup('majeranek otarty', 1, 1.49, 'Carrefour', 'przyprawy')
    wydatki += Zakup('gałka muszkatołowa', 1, 1.49, 'Carrefour', 'przyprawy')
    wydatki += Zakup('pieprz prymat 20g', 1, 1.49, 'Carrefour', 'przyprawy')
    wydatki += Zakup('pieprz prymat 15g', 1, 1.49, 'Carrefour', 'przyprawy')
    wydatki += Zakup('kurkuma prymat 15g', 1, 1.49, 'Carrefour', 'przyprawy')
    wydatki += Zakup('gorczyca prymat', 1, 1.49, 'Carrefour', 'przyprawy')
    wydatki += Zakup('kminek prymat', 1, 1.49, 'Carrefour', 'przyprawy')
    wydatki += Zakup('goździk kotanyi', 1, 2.79, 'Carrefour', 'przyprawy')
    wydatki += Zakup('czosnek niedźwiedzi kotanyi', 1, 2.79, 'Carrefour', 'przyprawy')
    wydatki += Zakup('szpinak mrożony liście', 2, 10.46, 'Biedronka', 'przyprawy')
    wydatki += Zakup('szpinak mroźna kraina', 1, 3.19, 'Biedronka', 'przyprawy')
    wydatki += Zakup('boczek do peklowania', .983, 12.77, 'Biedronka', 'mięso')
    wydatki += Zakup('truskawka mrożona', 1, 5.99, 'Biedronka', 'mrożonki')
    wydatki += Zakup('filety rybne mintaj', .485*2, 25.41, 'Biedronka', 'ryby')
    wydatki += Zakup('masło klarowane', 1.000, 31.58, 'Biedronka', 'tłuszcze')
    wydatki += Zakup('przyprawa imbir kamis', 1.000, 1.99, 'Biedronka', 'przyprawy')

    # wydatki += Zakup('', 1, 0, '')

    print(f'pozycji: {len(wydatki)}, łączne wydatki: {wydatki.razem()}')

    print(wydatki.razem_po_kategorii())
