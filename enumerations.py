# backend stuff, nothing to change for an end-user

from enum import Enum, auto


class Acquisition(Enum):
    WE_MAKE_IT = auto()
    WE_BUY_IT = auto()
    WE_GET_IT = auto()


class FoodCategory(Enum):
    SALTY = auto()
    SWEET = auto()
    OTHERS = auto()


class WhoTakesResponsibility(Enum):
    Szymon = auto()
    Agnieszka = auto()
    Matylda = auto()
    Weronika = auto()
    Rafal = auto()
    Monika = auto()


class ProductionStage(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    RESOLVED = auto()
    CLOSED = auto()


products_categories = {
    'bataty': 'warzywa',
    'bezglutenowy cukier cynamonowy': 'wypieki',
    'boczek wędzony': 'wędliny',
    'buraki': 'warzywa',
    'buraki ćwikłowe': 'warzywa',
    'cebula': 'warzywa',
    'chrzan tarty': 'przetwory',
    'cukinia': 'warzywa',
    'cukier': 'wypieki',
    'cukier puder': 'wypieki',
    'cytryna': 'owoce',
    'czosnek': 'warzywa',
    'czosnek niedźwiedzi': 'przyprawy',
    'dżem truskawkowy': 'przetwory',
    'ekstrakt z wanilii': 'wypieki',
    'filet z łososia': 'ryby',
    'filety rybne': 'ryby',
    'filety śledziowe': 'ryby',
    'gałka muszkatołowa': 'przyprawy',
    'golonka': 'mięso',
    'groch drobniutki perłowy': 'warzywa',
    'groszek mrożony': 'mrożonki',
    'grzyby suszone': 'warzywa',
    'jabłko': 'owoce',
    'jajko': 'jajko',
    'kakao': 'wypieki',
    'kapusta kiszona': 'kiszonki',
    'karkówka': 'mięso',
    'kiełbasa wiejska*': 'wędliny',
    'buraki kiszone': 'kiszonki',
    'kminek': 'przyprawy',
    'majeranek': 'przyprawy',
    'kurkuma': 'przyprawy',
    'liście laurowe': 'przyprawy',
    'lubczyk': 'przyprawy',
    'majonez': 'przetwory',
    'marchewka': 'warzywa',
    'masło': 'tłuszcze',
    'masło klarowane': 'tłuszcze',
    'miód': 'wypieki',
    'szynka': 'mięso',
    'mleko': 'nabiał',
    'mleko pełne w proszku': 'nabiał',
    'musztarda': 'przetwory',
    'mąka gryczana': 'wypieki',
    'mąka kukurydziana': 'wypieki',
    'mąka ryżowa': 'wypieki',
    'mąka ziemniaczana': 'wypieki',
    'naleśniki': 'żywność gotowa',
    'natka pietruszki': 'warzywa',
    'ogórki długie': 'warzywa',
    'ogórki kiszone': 'kiszonki',
    'olej rzepakowy': 'tłuszcze',
    'oliwa z oliwek': 'tłuszcze',
    'opłatki bezglutenowe*': 'inne',
    'papryka': 'przyprawy',
    'pełnoziarnista mąka gryczana': 'wypieki',
    'pieprz mielony': 'przyprawy',
    'pieprz ziarnisty': 'przyprawy',
    'filet z indyka': 'mięso',
    'pietruszka': 'warzywa',
    'podgardle': 'mięso',
    'przyprawa do pierników': 'przyprawy',
    'pęczek koperku': 'warzywa',
    'pęczek pietruszki': 'warzywa',
    'płatki migdałowe': 'wypieki',
    'rozmaryn': 'przyprawy',
    'rukola': 'warzywa',
    'roszponka': 'warzywa',
    'mix sałat': 'warzywa',
    'seler': 'warzywa',
    'smalec': 'tłuszcze',
    'soda oczyszczona': 'wypieki',
    'śliwki suszone': 'owoce',
    'szpinak mrożony': 'mrożonki',
    'sól': 'przyprawy',
    'sól peklująca': 'przyprawy',
    'słonina': 'tłuszcze',
    'truskawki mrożone': 'mrożonki',
    'twaróg sernikowy': 'nabiał',
    'tymianek': 'przyprawy',
    'kasza jaglana': 'zboża',
    'woda': 'inne',
    'woda letnia przegotowana': 'inne',
    'woda z kiszonych ogórków': 'kiszonki',
    'wątroba kurza': 'mięso',
    'zakwas buraczany': 'inne',
    'zakwas na żurek': 'inne',
    'ziele angielskie': 'przyprawy',
    'ziele angielskie mielone': 'przyprawy',
    'ziemniaki': 'warzywa',
    'zioła prowansalskie': 'przyprawy',
    'śmietana 12%': 'nabiał',
    'śmietana 18%': 'nabiał',
    'śmietana 36%': 'nabiał',
}

dont_buy = {'woda',
            'woda letnia przegotowana',
            'zakwas buraczany',
            'zakwas na żurek',
            'buraki kiszone',
            'naleśniki',
            'woda z kiszonych ogórków',
            }
