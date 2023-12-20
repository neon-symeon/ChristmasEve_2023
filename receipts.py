# all the receipts are gathered here
# they are all set-up and ready,
# when finish preparing a meal, one could change 'zrobione' to True for an individual meal


from pprint import pprint
from datetime import date
import math
from source import sources
from glob import HOW_MANY_PEOPLE
from enumerations import WhoTakesResponsibility, Acquisition, FoodCategory, ProductionStage

print(f'How Many People = {HOW_MANY_PEOPLE}')

zakwas_barszcz = {
    'nazwa': 'zakwas buraczany',
    'kto': [WhoTakesResponsibility.Agnieszka],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {'source': sources['swieta_bez_pszenicy'],
               'strona': 172},
    'składniki': {
        'buraki - kg': 1.5,
        'czosnek- ząbki': 6,
        'liście laurowe - szt': 2,
        'ziele angielskie - kulki': 6,
        'pieprz ziarnisty - łyżeczka': .500,
        'sól - łyżeczka': 2,
        'woda letnia przegotowana - l': 2,
    },
    'na ile porcji': 12,
    'przepis':
        'buraki obierz i pokrój w kostkę. Obierz 4 ząbki czosnku i przekrój na pół. Dwa ząbki zostaw w'
        'skórce i lekko zmiażdż. Do słoja wrzuć wszystkie składniki. Zalej wszystko przegotowaną letnią'
        'wodą, jedna łyżeczka soli na 1 l. wody. Woda powinna sięgać przynajmniej 2 cm ponad buraki.'
        'Przykryj słój, postaw naczynie w ciepły miejscu na 4-8 dni. Po dwóch dniach zbierz zgromadzoną'
        'na wierzchu pianę. Im dłużej postoi, tym będzie bardziej kwaskowy.',
    'kategoria': FoodCategory.OTHERS,
    'kiedy': date(2023, 12, 16),
    'zrobione': True,
}

barszcz = {
    'nazwa': 'barszcz czerwony na zakwasie',
    'kto': [WhoTakesResponsibility.Szymon, WhoTakesResponsibility.Matylda],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {'source': sources['swieta_bez_pszenicy'],
               'strona': 147},
    'składniki': {
        'buraki ćwikłowe - kg': 1.5,
        'zakwas buraczany - l': .400,
        'marchewka - szt': 1,
        'pietruszka - szt': 1,
        'cebula - szt': 2,
        'seler - szt': 1 / 2,
        'czosnek - ząbki': 5,
        'grzyby suszone- szt': 4,
        'liście laurowe - szt': 4,
        'ziele angielskie - kulki': 10,
        'pieprz ziarnisty - łyżeczka': 1 / 2,
        'majeranek  - łyżeczka': 1,
        'lubczyk - szczypta': 1,
        'pieprz mielony - szczypta': 1,
        'sól - szczypta': 1,
    },
    'na ile porcji': 4,
    'przepis':
        'Warzywa obierz i do dużego garnka wrzuć wraz z czosnkiem i suszonymi grzybami oraz przyprawami.'
        'Zagotuj na średnim ogniu i gotuj przez godzinę. Zdejmij garnek z gazu, przecedź barszcz, dolej'
        'zakwas. Dopraw mielonym pierzem i solą. Nie wolno juz teraz zagotować, bo straci piękny kolor.'
        'Dla polepszenia smaku dodajemy roztarty czosnek.',
    'kategoria': FoodCategory.SALTY,
    'kiedy': date(2023, 12, 23),
    'zrobione': False,
}

uszka = {
    'nazwa': 'uszka tradycyjne',
    'kto': [WhoTakesResponsibility.Rafal, WhoTakesResponsibility.Monika],
    'jak': Acquisition.WE_GET_IT,
    'źródło': {'source': sources['babcia_tereska'],
               'strona': None},
    'składniki': {},
    'na ile porcji': None,
    'przepis': None,
    'kategoria': FoodCategory.SALTY,
}

nalesniki = {
    'nazwa': 'naleśniki bezglutenowe',
    'kto': [WhoTakesResponsibility.Agnieszka],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {'source': sources['aga'],
               'strona': None},
    'składniki': {
        'mąka ziemniaczana - kg': .250,
        'mąka ryżowa - kg': .250,
        'sól - szczypta': 1,
        'mleko - l': .500,
        'jajko - szt': 1,
        'masło klarowane - kg': .1},
    'na ile porcji': 12,
    'przepis':
        'W garnku roztrzepujemy jajko z solą. Dodajemy kubek mąki i wlewamy połowę mleka. Mieszamy na'
        'gładką masę. Dodajemy drugi kubek mąki i drugą porcję mleka. Ponownie mieszamy na gładką masę.<br>'
        'Rozgrzaną patelnię smarujemy masłem. Wlewamy niecałą chochelkę ciasta naleśnikowego na patelnię.'
        'Smażymy z obu stron odwracając na drugą stronę, gdy ciasto na brzegach patelni odkleja się.'
        'Przed każdym następnym wlaniem ciasta mieszamy je trzepaczką, aby pozbyć się grudek, które'
        'opadają na dno garnka.',
    'kategoria': FoodCategory.SALTY,
    'kiedy': date(2023, 12, 24),
    'zrobione': False,
}

krokiety = {
    'nazwa': 'krokiety z łososiem i szpinakiem',
    'kto': [WhoTakesResponsibility.Szymon, WhoTakesResponsibility.Matylda],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {'source': sources['swieta_bez_pszenicy'],
               'strona': 156},
    'składniki': {
        'naleśniki - szt': 12,
        'szpinak mrożony - paczka': 1,
        'filet z łososia - kg': .200,
        'cebula - szt': 1,
        'pęczek koperku  -szt': 1,
        'sól - szczypta': 1,
        'pieprz mielony- szczypta': 1,
        'cytryna - szt': 1,
        'masło klarowane - kg': .1, },
    'na ile porcji': 24,
    'przepis':
        'Cebulę obierz, drobno posiekaj i zezłoć na tłuszczu. Dodaj mrożony szpinak i podgrzewaj, aż zmięknie.'
        'OdkRyj pokrywkę i duś do czasu, aż nadmiar wody wyparuje.<br> Łososia cienko posiekaj.<br>'
        'Wymieszaj szpinak z łososiem oraz posiekany koperek. Dopraw pierzem, solą i sokiem z cytryny<br>'
        'Posmaruj połowę naleśnika farszem zwiń w rulon. Przekrój na pół, obtocz w roztrzepanym jajku i mące'
        'kukurydzianej. Podsmaż z obu stron i podawaj. Najlepiej smakuje świeżuchne, podane zaraz po przygotowaniu.',
    'kategoria': FoodCategory.SALTY,
    'kiedy': date(2023, 12, 24),
    'zrobione': False,
}

zakwas_zurek = {
    'nazwa': 'zakwas na żurek gryczany',
    'kto': [WhoTakesResponsibility.Agnieszka],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {'source': sources['swieta_bez_pszenicy'],
               'strona': 281},
    'składniki': {
        'pełnoziarnista mąka gryczana - kg': .120,
        'czosnek - ząbki': 6,
        'liście laurowe - szt': 4,
        'ziele angielskie - kulki': 10,
        'majeranek - łyżeczka': 1,
        'woda z kiszonych ogórków - łyżka': 3,
        'woda letnia przegotowana - litr': .800,
    },
    'na ile porcji': 6,
    'przepis':
        'Czosnek obierz ze skórki pokrój na połówki. Wymieszaj wszystkie składniki w słoiku. Przykryj'
        'papierem śniadaniowym i zabezpiecz gumką recepturką. Zostaw na 7 dni w ciepłym miejscu. Zakwas gotowy.',
    'kategoria': FoodCategory.OTHERS,
    'kiedy': date(2023, 12, 16),
    'zrobione': True,
}

zurek = {
    'nazwa': 'żurek na zakwasie',
    'kto': [WhoTakesResponsibility.Szymon],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {'source': sources['swieta_bez_pszenicy'],
               'strona': 287},
    'składniki': {
        'zakwas na żurek - szt': 1,
        'śmietana 18% - kubek': .3,
        'marchewka - szt': 1,
        'pietruszka - szt': 1,
        'cebula - szt': 1,
        'czosnek - ząbki': 3,
        'seler - szt': 1,
        'liście laurowe - szt': 4,
        'ziele angielskie - kulki': 6,
        'grzyby suszone- szt': 8,
        'pęczek pietruszki - szt': 1 / 2,
        'majeranek - łyżka': 1,
        'chrzan tarty - łyżeczka': 1,
        'jajko - szt': .5,
    },
    'na ile porcji': 5,
    'przepis':
        'Z warzyw ugotuj wywar. Przecedź i wlej spowrotem do garnka. Dodawaj stopniowo zakwas ciągle mieszając.'
        'W mikserze roztrzep jajko ze śmietaną. Wlej powoli do żuru ciągle mieszając. Dopraw solą i pieprzem oraz'
        'grzyby, chrzan tarty na Wielkanoc. Podgrzewaj nieustająco mieszając tak długo, aż na powierzchni żuru zaczną'
        'pojawiać się ruchy, co nazywamy, że barszcz "idzie". Tedy jest gotowy. Taki gorący podawać.',
    'kategoria': FoodCategory.SALTY,
    'kiedy': date(2023, 12, 23),
    'zrobione': False,
}

sznycelki = {
    'nazwa': 'kotlety rybne',
    'kto': [WhoTakesResponsibility.Szymon],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {'source': sources['swieta_bez_pszenicy'],
               'strona': 267},
    'składniki': {
        'filety rybne - kg': 1,
        'kasza jaglana - łyżka': 2,
        'natka pietruszki - szt': 1,
        'kurkuma - szczypta': 1,
        'tymianek - szczypta': 1,
        'czosnek niedźwiedzi - szczypta': 1,
        'mąka kukurydziana - szczypta': 16,
        'masło klarowane - kg': .1,
    },
    'na ile porcji': 16,
    'przepis':
        'Rozmrożoną bardzo dokładnie odciśnij z wody. Zmiel mięso w maszynie na na dużym oczku. Dodaj'
        'ugotowaną kaszę jaglaną, pietruszkę oraz przyprawy. Uformuj kotleciki i smaż po 3 min z każdej strony.',
    'kategoria': FoodCategory.SALTY,
    'kiedy': date(2023, 12, 24),
    'zrobione': False,
}

pierogi = {
    'nazwa': 'pierogi z kapustą i grzybami',
    'kto': [WhoTakesResponsibility.Szymon, WhoTakesResponsibility.Agnieszka, WhoTakesResponsibility.Matylda],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {'source': sources['swieta_bez_pszenicy'],
               'strona': [160, 369]},
    'składniki': {
        'pełnoziarnista mąka gryczana - kg': .34,
        'jajko - szt': 2,
        'olej rzepakowy - łyżka': 2,
        'kapusta kiszona - kg': .5,
        'grzyby suszone- paczka': 1,
        'cebula - szt': 2,
        'kminek - łyżeczka': 2,
        'liście laurowe - szt': 2,
        'pieprz mielony- szczypta': 1,
        'sól - szczypta': 1,
        'masło klarowane - kg': .010
    },
    'na ile porcji': 6,
    'przepis':
        'Ciasto: w rondelku zagotuj 300 ml wody z olejem. Kiedy woda zacznie się gotować wsyp do niej'
        'partiami 160 gr mąki mieszając energicznie łyżką, by mąka połączyła się z wodą. Masa szybko zgęstnieje.'
        'Ugniataj ciasto łyżką aż nie będzie śladu surowej mąki. Odstaw garnek z ognia aby masa przestygła.'
        'Na stolnice wysyp resztę mąki (180 gr), wbij dwa jajka i wymieszaj je z mąką. Dodaj zaparzoną mąkę i'
        'zagnieć ciasto. Podziel to na 4 części i każdą rozwałkuj na grubość 1 mm. Ciasto połóż na kawałku folii'
        'spożywczej aby się nie przyklejało. Z ciasta wykrój kółka za każdym razem zanurzając brzeg szklanki'
        'w mące. Robimy pierogi, gotujemy na wrzątku delikatnie. Wyciągamy i serwujemy.'
        'Farsz:  suszone grzyby namocz przez 3-4 h, ugotuj do miękkości, odsącz i drobno posiekaj. Cebule drobno'
        'posiekaj i zezłoć na tłuszczu. Kapustę ugotuj w niewielkiej ilości wody razem z przyprawami do miękkości'
        'odcisnąć i drobno posiekać. Do kapusty dodajemy cebulę z grzybami, doprawiamy pieprzem i solą. Farsz gotowy.',
    'kategoria': FoodCategory.SALTY,
    'kiedy': date(2023, 12, 23),
    'zrobione': False,
}

kapusta_z_grochem = {
    'nazwa': 'kapusta z grochem',
    'kto': [WhoTakesResponsibility.Szymon, WhoTakesResponsibility.Matylda],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {'source': sources['babcia_tereska'],
               'strona': None},
    'składniki': {
        'kapusta kiszona - kg': 3,
        'groch drobniutki perłowy- kg': 1,
        'grzyby suszone - paczka': 1,
        'cebula - szt': 3,
        'masło - kg': 0.1,
        'pieprz mielony- szczypta': 1,
        'ziele angielskie mielone - szczypta': 1,
        'kminek - szczypta': 1,
        'majeranek - szczypta': 1,
    },
    'na ile porcji': 30,
    'przepis':
        'kapustę gotujemy do miękkości 1 godzinę, groch moczymy przez noc, podwaja swoją objętość.',
    'kategoria': FoodCategory.SALTY,
    'kiedy': date(2023, 12, 23),
    'zrobione': False,
}

kompot = {
    'nazwa': 'kompot z suszu',
    'kto': [WhoTakesResponsibility.Szymon],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {'source': sources['babcia_tereska'],
               'strona': None},
    'składniki': {
        'śliwki suszone - kg': 1,
        'cukier - łyżka': 3,
    },
    'na ile porcji': 16,
    'przepis': 'zagotować, dosłodzić, podać',
    'kategoria': FoodCategory.OTHERS,
    'kiedy': date(2023, 12, 23),
    'zrobione': False,
}

karp = {
    'nazwa': 'karp smażony',
    'kto': [WhoTakesResponsibility.Monika],
    'jak': Acquisition.WE_GET_IT,
    'źródło': {'source': sources['zbyszek'],
               'strona': None},
    'składniki': {},
    'na ile porcji': 12,
    'przepis': '',
    'kategoria': FoodCategory.SALTY,
}

placek_niebo = {
    'nazwa': 'placek Niebo',
    'kto': [WhoTakesResponsibility.Weronika],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {'source': sources['swieta_bez_pszenicy'],
               'strona': 239},
    'składniki': {
        'mąka gryczana - kg': .140,
        'mąka ryżowa - kg': .100,
        'mąka kukurydziana - kg': .060,
        'cukier - kg': .280,
        'masło - kg': .600,
        'jajko - szt': 3,
        'jabłko - kg': .75,
        'cytryna - szt': 1,
        'płatki migdałowe - kg': .250,
        'mleko - l': .250,
        'cukier puder - kg': .120,
        'kakao - łyżka': 2,
        'woda - łyżeczka': 7},
    'na ile porcji': 12,
    'przepis':
        'CIASTO: wszystkie składniki ciasta  (3 mąki, 80g cukru, 200 g masła, 3 żółtka) wymieszaj i zagnieć'
        'ciasto. Podziel na pół i uformuj dwa placki o wymiarach mniej więcej 35 x 20 cm. Podpiecz'
        'w piekarniku nagrzanym do 180 st Celsjusza przez 15 min. do lekkiego zrumienienia. MASA JABŁKOWA:'
        'Jabłka obierz i zetrzyj na dużych oczkach. Podduś z cukrem (200g) i 2 łyżeczkami soku z cytryny w'
        'garnku z dużym dnem, aż zmiękną i większość płynu odparuje (jednak jabłka powinny zostać wilgotne.'
        'Ciepłą masę jabłkową wyłóż na pierwszy upieczony placek i przykryj drugim plackiem. MASA'
        'MIGDAŁOWA: migdały zmiel w maszynce i zalej gorącym mlekiem (250 ml). Ostudź a następnie utrzyj'
        'z masłem oraz cukrem pudrem. Wyłóż masę migdałową na drugi placekPolewa: w małym garnku umieść'
        '50 gr masła, 5 łyżek cukru, 2 czubate łyżki kakao i 7 łyżeczek wody i podgrzej na małym ogniu.'
        'Zdejmij gdy całość zacznie się gotować i ładnie się rozprowadź przestudź nieco i wciąż lekko płyną'
        'polej masę migdałową. Ciast przechowuj w lodówce',
    'kategoria': FoodCategory.OTHERS,
    'kiedy': date(2023, 12, 22),
    'zrobione': False,
}

pierniki = {
    'nazwa': 'pierniczki matyldziowe',
    'kto': [WhoTakesResponsibility.Agnieszka, WhoTakesResponsibility.Matylda],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {'source': sources['swieta_bez_pszenicy'],
               'strona': None},
    'składniki': {
        'mąka ryżowa - kg': .113,
        'mąka ziemniaczana - kg': .113,
        'mąka kukurydziana - kg': .114,
        'przyprawa do pierników - łyżka': 1,
        'bezglutenowy cukier cynamonowy - łyżeczka': 1,
        'kakao - łyżka': 1,
        'cukier - kg': .050,
        'soda oczyszczona - łyżeczka': 1,
        'dżem truskawkowy - kg': .100,
        'miód - łyżka': 3,
        'ziemniaki - kg': .100,
        'masło - kg': .060,
        'jajko - szt': 1,
    },
    'na ile porcji': 48,
    'przepis':
        'Mieszamy suche składniki. Dodajemy pozostałe surowce, mieszamy ręcznie lub mikserem na jednolitą masę'
        'wstawiamy do lodówki na 1-2 godz. Na stolnicę posypaną dodatkową mąką ziemniaczaną wykładamy ciasto'
        'i rozwałkowujemy małymi porcjami. Piekarnik na 180 st. foremkami wycinamy pierniczki i układamy niezbyt'
        'gęsto na blasze. Pieczemy 10-15 min. Wsadzamy do puszki ze skórki z pomarańczy. Gdy ostygną możemy udekorować'
        'lukrem lub czekoladą. Przechowujemy w metalowej puszce, będą długo świeże, miękkie i aromatyczne.',
    'kategoria': FoodCategory.OTHERS,
    'kiedy': date(2023, 12, 20),
    'zrobione': False,
}

czekolada = {
    'nazwa': 'czekolada domowa',
    'kto': [WhoTakesResponsibility.Szymon],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {'source': sources['swieta_bez_pszenicy'],
               'strona': None},
    'składniki': {
        'mleko pełne w proszku - szt': 1,
        'masło - kg': .200,
        'kakao - łyżka': 2,
        'cukier - kg': .200,
        'mleko - l': .200,
    },
    'na ile porcji': 12,
    'przepis':
        'Do pół szklanki mleka wsyp kakao i mieszaj aż nie będzie grudek. W garnku rozpuszczamy (mieszamy wszystko'
        'podczas rozpuszczania) masło z cukrem i dolewamy mlekiem z kakaem (z naszej szklanki). Następnie powoli,'
        'cały czas mieszając dodajemy mleko w proszku. Uzyskaną "czekoladę" przekładamy do foremki wyłożonej'
        'papierem do pieczenia (np. "keksówki") i po wystudzeniu wstawiamy na noc do lodówki.',
    'kategoria': FoodCategory.SWEET,
    'kiedy': date(2023, 12, 22),
    'zrobione': False,
}

sernik = {
    'nazwa': 'sernik idealny',
    'kto': [WhoTakesResponsibility.Agnieszka, WhoTakesResponsibility.Matylda],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {},
    'składniki': {
        'twaróg sernikowy - kg': 1,
        'cukier - kg': .200,
        'mąka ziemniaczana - łyżka': 3,
        'jajko - szt': 5,
        'śmietana 36% - l': .125,
        'ekstrakt z wanilii - łyżeczka': 3,
        'śmietana 12% - l': .250,
        'cukier - łyżka': 3,
        'truskawki mrożone - opakowanie': 1,
    },
    'na ile porcji': 12,
    'przepis':
        'Składniki wyjmujemy wcześniej z lodówki. Dno tortownicy z odpinaną obręczą o średnicy 21-22 cm wyłożyć'
        'papierem do pieczenia. Zapnij obręcz wypuszczając papier na zewnątrz. boki tortownicy posmarować masłem.'
        'Piekarnik nagrzać do tmp 175 stopni góra-dół. Do misy miksera włożyć ser, cukier i makę. Miksować na średnich'
        'obrotach aż masa będzie gładka i jednolita, przez około 2 min dodając po jednym jajku, miksując przez około'
        '30 sek po każdym dodanym jajku. Dodać śmietankę i wanilię i miksować dalej do połączenia składników, przez'
        'około pół minuty. masę wlać do przygotowanej formy, wstawić do środkowej części piekarnika i piec przez 15'
        'minut. Następnie zmniejszyć temperaturę do 120 stopni i piec przez kolejne półtorej godziny. Sernik wyjąć'
        'z piekarnika i rozprowadzić na nim kwaśną śmietanę wymieszana  z cukrem. Wstaw z powrotem do piekarnika na'
        'kolejne 15 minut. Gotowy sernik wyjąć na kratkę i ostudzić. przed podaniem udekorować owocami.',
    'kategoria': FoodCategory.SWEET,
    'kiedy': date(2023, 12, 23),
    'zrobione': False,
}

pasztet = {
    'nazwa': 'pasztet wieprzowo-drobiowy',
    'kto': [WhoTakesResponsibility.Szymon, WhoTakesResponsibility.Matylda],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {'source': sources['nomart'],
               'strona': None},
    'składniki': {
        'golonka - kg': 1.3,
        'wątroba kurza - kg': .5,
        'podgardle - kg': .4,
        'karkówka - kg': .3,
        'cebula - szt': 2,
        'jajko - szt': 3,
        'słonina  - kg': .2,
        'smalec - łyżka': 1,
        'liście laurowe - szt': 3,
        'ziele angielskie - kulki': 5,
        'grzyby suszone  - szt': 5,
        'sól - łyżeczka': 3,
        'pieprz mielony- łyżeczka': 2,
        'gałka muszkatołowa - łyżeczka': .5},
    'na ile porcji': 4,
    'przepis':
        'Mięsa kroimy na mniejsze kawałki, dodajemy cebule, liście laurowe, grzyby, ziele angielskie obgotować na małym'
        'ogniu 30 min. Po tym czasie dodać do garnka z gorącymi mięsami wątróbkę i gotować przez 5 min. Wyłączyć i'
        'odstawić do przestygnięcia na noc. Wydobyć całą zawartość garnka i mielimy na oczkach grubych. Dodajemy'
        'przyprawy: sól, pieprz i gałkę. Po wymieszaniu mielimy jeszcze dwa razy, na średnim i na końcu małym oczku.'
        'Dodajemy jajka, mieszamy. Foremki nacieramy smalcem i napełniamy. Na wierzch kładziemy paski słoniny. Piec'
        'w piekarniku z termoobiegiem na 200 stopni przez 60 min. Sprawdzamy upieczenie testem suchej zapałki.',
    'kategoria': FoodCategory.SALTY,
    'kiedy': date(2023, 12, 22),
    'zrobione': False,
}

sledziowa = {
    'nazwa': 'sałatka śledziowa',
    'kto': [WhoTakesResponsibility.Szymon, WhoTakesResponsibility.Matylda],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {'source': sources['others'],
               'strona': None},
    'składniki': {
        'filety śledziowe - kg': .500,
        'jajko - szt': 5,
        'jabłko - szt': 2,
        'cebula - szt': 1,
        'majonez - łyżki': 3,
        'musztarda - łyżeczka': 2,
        'sól - szczypta': 1,
        'pieprz mielony- szczypta': 1,
        'groszek mrożony - paczka': .5,
    },
    'na ile porcji': 6,
    'przepis':
        'filety śledziowe moczymy przez ok. 12 godzin w wodzie, co kilka godzin zmieniając wodę. Następnie'
        'kroimy w cienkie paski, podobnie jak ugotowane jabłka, obrane jabłka. Cebulę kroimy w b. drobną'
        'kostkę. Dodajemy majonez i musztardę, by na końcu doprawić solą i pieprzem do smaku.',
    'kategoria': FoodCategory.SALTY,
    'kiedy': date(2023, 12, 23),
    'zrobione': False,
}

majonez = {
    'nazwa': 'majonez domowy',
    'kto': [WhoTakesResponsibility.Szymon, WhoTakesResponsibility.Matylda],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {},
    'składniki': {
        'jajko- szt': 1,
        'olej rzepakowy - l': .3,
        'musztarda - łyżeczka': 1,
        'miód - łyżeczka': 1,
        'sól - szczypta': 1,
        'pieprz mielony- szczypta': 1,
        'cytryna - szt': 1,
    },
    'na ile porcji': 12,
    'przepis':
        'jajko sparzone i pozostałe składniki wlać i wsypać do cylindrycznego naczynia. Wprowadzić blender'
        'ręczny na samo dno i !nie przerywając pracy blendera! unosić powoli końcówkę miksującą z dna do samej góry'
        'naczynia, następnie zjedżdzamy do dna, by ponownie wyjechać na samą górę i po raz ostatni zjechać końcówką'
        'miksującą na samo dno. po tym kilkukrotnym, NIEPRZERWANYM miksowaniu składników powinniśmy otrzymać jednlity.'
        'sztywny i smakowity majonez domowy. Jeśli jest zbyt luźny mozna dodać nieco oleju i jeszcze raz zamieszać'
        'dół - góra - dół. Smacznego!',
    'kategoria': FoodCategory.SALTY,
    'kiedy': date(2023, 12, 23),
    'zrobione': False,
}

jarzynowa = {
    'nazwa': 'sałatka jarzynowa',
    'kto': [WhoTakesResponsibility.Szymon, WhoTakesResponsibility.Matylda,
            WhoTakesResponsibility.Agnieszka, WhoTakesResponsibility.Weronika],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {},
    'składniki': {
        'marchewka - kg': 1,
        'pietruszka - kg': .7,
        'seler - kg': .5,
        'ogórki kiszone - szt': 5,
        'jajko - szt': 5,
        'jabłko - szt': 3,
        'groszek mrożony - paczka': 1,
        'sól - szczypta': 1,
        'pieprz mielony - szczypta': 1,
        'śmietana 12% - kubek': .5,
        'majonez - szt': 1,
    },
    'na ile porcji': 24,
    'przepis': 'Surowe warzywa gotujemy w skórkach do miękkości (ok 1h). Jajka gotujemy na twardo. Groszek mrożony'
    'jedynie podgotowujemy, szybko dochodzi. Wszystkie warzywa kroimy na drobną kostkę, dodajemy majonez i śmietanę'
    'przyprawiamy do smaku solą i pieprzem, Gotowe.',
    'kategoria': FoodCategory.SALTY,
    'kiedy': date(2023, 12, 23),
    'zrobione': False,
}

szynka = {
    'nazwa': 'szynka domowa peklowana pieczona',
    'kto': [WhoTakesResponsibility.Szymon, WhoTakesResponsibility.Matylda],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {},
    'składniki': {
        'szynka - kg': 1,
        'sól peklująca - kg': .050,
        'cukier - kg': .010,
    },
    'na ile porcji': 12,
    'przepis':
        'W przegotowanej wodzie rozpuszczamy sół peklującą i cukier. Proporcje: "25 g soli peklowej rozpuszczonej'
        'w 100 ml wody dostarcza do nastrzyknięcia około 1 kg mięsa. "Peklowanie metodą zalewową: rozpuścić sól peklową'
        'w wodzie (50 g na 1 litr wody). Mięso powinno być całkowicie zanurzone w zalewie przez około 7 dni. Peklowane'
        'mięso należy przechowywać w temp. ok. 8 stopni" (source: https://www.galeo.pl/produkty/opis/sol-peklowa). '
        'Po tym czasie wiążemy szyneczkę i do piekarnika na 1.5-2h w temp. ok 130-150 st. W środku mięso powinno'
        'osiągnąć temp. 72 st, aby było gotowe.',
    'kategoria': FoodCategory.SALTY,
    'kiedy': [date(2023, 12, 18), date(2023, 12, 23)],
    'zrobione': True,
    'stan': ProductionStage.IN_PROGRESS,  # eksperymentalnie, jako alternatywa do 'zrobione'
}

indyk = {
    'nazwa': 'indyk faszerowany szpinakiem w plastrach boczku',
    'kto': [WhoTakesResponsibility.Szymon, WhoTakesResponsibility.Matylda],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {},
    'składniki': {
        'filet z indyka - kg': 3,
        'szpinak mrożony - paczka': 2,
        'sól - szczypta': 1,
        'pieprz mielony- szczypta': 1,
        'zioła prowansalskie - szczypta': 4,
        'masło klarowane - kg': 0.100,
        'czosnek - ząbki': 4,
        'boczek wędzony - plastry': 12,
    },
    'na ile porcji': 12,
    'przepis':
        'Posolony szpinak redukujemy na maśle klarowanym. Na końcu dodajemy przeciśnięty przez praskę czosnek. Mięso'
        'delikatnie rozbijamy, żeby uformować regularny prostokąt. Z obu stron przyprawiamy. Na mięso nakładamy szpinak'
        'pozostawiając 1/3 mięsa pustą (podczas zwijania ta część będzie na końcu i zapobiegnie wydostawaniu się'
        'szpinaku na zewnątrz rolady. Zwinięte rolady obkładamy plastrami boczku, a następnie krępujemy sznurkiem'
        'wędliniarskim. Wrzucamy do piekarnika na 180 stopni na 90 min i gotowe.',
    'kategoria': FoodCategory.SALTY,
    'kiedy': date(2023, 12, 26),
    'zrobione': False,
}

pieczone_warzywa = {
    'nazwa': 'pieczone ziemniaki, bataty i cukinie w rozmarynie',
    'kto': [WhoTakesResponsibility.Szymon, WhoTakesResponsibility.Matylda],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {},
    'składniki': {
        'ziemniaki - szt': 12,
        'bataty - szt': 4,
        'cukinia - szt': 4,
        'papryka - szt': 2,
        'rozmaryn - doniczka': 1,
        'sól - szczypta': 1,
        'pieprz mielony- szczypta': 1,
    },
    'na ile porcji': 12,
    'przepis':
        'warzywa obieramy, kroimy w ćwiartki lub plasterki, układamy na blasze, przyprawiamy i pieczemy'
        '30 min. w piekarniku z termoobiegiem na 200 st.',
    'kategoria': FoodCategory.SALTY,
    'kiedy': date(2023, 12, 26),
    'zrobione': False,
}

mizeria = {
    'nazwa': 'mizeria',
    'kto': [WhoTakesResponsibility.Szymon, WhoTakesResponsibility.Matylda],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {},
    'składniki': {
        'ogórki długie - szt': 3,
        'cebula - szt': 1,
        'śmietana 12% - kubek': 1,
        'sól - szczypta': 1,
        'pieprz mielony- szczypta': 1,
        'cytryna - szt': 1,
        'miód - łyżka': 1,
    },
    'na ile porcji': 12,
    'przepis':
        'ogórki i cebulę obrać i pokroić w cienkie plasterki. miód zmieszać z sokiem z cytryny i śmietaną'
        'przyprawić solą i pieprzem. pomieszać i podać',
    'kategoria': FoodCategory.SALTY,
    'kiedy': date(2023, 12, 26),
    'zrobione': False,
}

salata = {
    'nazwa': 'sałata włoska w dressingu',
    'kto': [WhoTakesResponsibility.Szymon, WhoTakesResponsibility.Matylda],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {},
    'składniki': {
        'mix sałat - paczka': 1,
        'miód - łyżka': 1,
        'cytryna - szt': 1,
        'musztarda - łyżeczka': 1,
        'oliwa z oliwek - l': .100,
        'sól - szczypta': 1,
        'pieprz mielony - szczypta': 1,
    },
    'na ile porcji': 8,
    'przepis': 'miód, cytrynę musztardę pomieszać w shakerze z oliwą, solą i pieprzem. polać liście i przemieszać',
    'kategoria': FoodCategory.SALTY,
    'kiedy': date(2023, 12, 26),
    'zrobione': False,
}

cwikla = {
    'nazwa': 'ćwikła na bazie kiszonych buraków',
    'kto': [WhoTakesResponsibility.Szymon, WhoTakesResponsibility.Matylda],
    'jak': Acquisition.WE_MAKE_IT,
    'źródło': {},
    'składniki': {
        'buraki kiszone - kg': 1,
        'musztarda - łyżeczka': 1,
        'chrzan tarty - łyżeczka': 2,
        'cytryna - szt': .5,
        'miód - łyżka': 1,
        'sól - szczypta': 1,
    },
    'na ile porcji': 12,
    'przepis':
        'buraki zetrzeć na najdrobniejszym oczku, pomieszać z dodatkami, serwować',
    'kategoria': FoodCategory.SALTY,
    'kiedy': date(2023, 12, 23),
    'zrobione': False,
}

kielbasa = {
    'nazwa': 'kiełbasa wiejska',
    'jak': Acquisition.WE_BUY_IT,
    'kto': [WhoTakesResponsibility.Szymon],
    'źródło': 'masarnia Kołdras',
    'jednostka': 'kg',
    'ile': 2,
    'kategoria': FoodCategory.SALTY,
}

oplatki = {
    'nazwa': 'opłatki bezglutenowe',
    'kto': [WhoTakesResponsibility.Matylda],
    'jak': Acquisition.WE_BUY_IT,
    'źródło': 'do_ustalenia',
    'jednostka': 'opakowanie',
    'ile': 2,
    'kategoria': FoodCategory.OTHERS,
}

makowiec = {
    'nazwa': 'makowiec',
    'kto': [WhoTakesResponsibility.Szymon],
    'jak': Acquisition.WE_BUY_IT,
    'źródło': 'cukiernia',
    'jednostka': 'kg',
    'ile': 2,
    'kategoria': FoodCategory.SWEET,
}

przepisy = [barszcz, cwikla, czekolada, indyk, jarzynowa, kapusta_z_grochem, karp, kielbasa,
            kompot, krokiety, majonez, makowiec, mizeria, nalesniki, oplatki, pasztet,
            pieczone_warzywa, pierniki, pierogi, placek_niebo, salata, sernik,
            sledziowa, sznycelki, szynka, uszka, zakwas_barszcz, zakwas_zurek, zurek]

dodatkowe = {
    'choinka': {
        'kiedy': date(2023, 12, 18),
        'gdzie': 'Castorama',
        'zrobione': date(2023, 12, 19),
    },
    'alkohole': {
        'kiedy': date(2023,  12,  21),
        'gdzie': ['Auchan', 'Lidl', 'Biedronka'],
        'zrobione': False,
    },
    'prezenty': {
        'kiedy': (date(2023, 12, 19), date(2023, 12, 21)),
        'gdzie': 'Bonarka',
        'zrobione': False,
    },
    'życzenia': {
        'kiedy': (date(2023, 12, 23), date(2023, 12, 24)),
        'zrobione': False,
    },
}


def create_multiplications():
    """
    adds a new key 'mnoznik' (multiplication) to receipts in order to calculate the right
    ingredients' (key: składniki) volumes to buy.
    """
    # uses global variable originally defined in 'glob.py' file.
    global HOW_MANY_PEOPLE
    print(f'How Many People from within create_multiplications = {HOW_MANY_PEOPLE}')
    # checks if all quantities are given as integer numbers, for smooth multiplications
    cond = all(isinstance(przepis['na ile porcji'], int)
               for przepis in przepisy
               if przepis['jak'] == Acquisition.WE_MAKE_IT)
    # finds closest ceil integer multiplications and adds to 'przepis' dict
    if cond:
        for przepis in przepisy:
            if przepis['jak'] == Acquisition.WE_MAKE_IT:
                multiplication = math.ceil(HOW_MANY_PEOPLE / math.ceil(przepis['na ile porcji']))
                przepis['mnoznik'] = multiplication
        return True
    # implicitly returns None if cond not met, which should evoke Exception further on


def gat_receipt_list() -> list:
    """
    in its intention, lists all receipts given in this file, should omit other objects that are not
    receipts and created either automatically or explicitly in this file.
    """
    global_scope_ = globals().copy()
    receipts_picked = []
    for name_ in global_scope_:
        if name_ not in ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__',
                         '__builtins__', '__file__', '__cached__', 'sources', 'pprint', 'przepisy',
                         'create_multiplications', 'HOW_MANY_PEOPLE', 'math', 'date',
                         'gat_receipt_list', 'WhoTakesResponsibility', 'Acquisition', 'FoodCategory']:
            receipts_picked.append(name_)

    return sorted(receipts_picked)


if __name__ == "__main__":
    #
    receipts_form_global_scope = gat_receipt_list()
    print(receipts_form_global_scope)
    pprint(receipts_form_global_scope)
    print(len(receipts_form_global_scope))
