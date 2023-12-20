# ----------------------------------------------------------------------------------------------+
# run this file to get the action plan for making the Christmas Eve sound, beautiful and tasty  |
# when you finish meal, you can go back to 'receipts.py' and change 'zrobione' to True.         |
# ----------------------------------------------------------------------------------------------+

from pprint import pprint
from receipts import przepisy
from enumerations import Acquisition


#
def create_timeline() -> list:
    _timeline_table = []
    for przepis in przepisy:
        if przepis['jak'] == Acquisition.WE_MAKE_IT:
            _name = przepis['nazwa']
            _date = None
            _done = przepis['zrobione']
            try:
                _date = przepis['kiedy'][0] if isinstance(przepis['kiedy'], list) else przepis['kiedy']
            except KeyError:
                print('brak klucza: ', _name)
            _timeline_table.append([_name, _date, _done])

    _timeline_table = sorted(_timeline_table, key=lambda x: x[1])

    return _timeline_table


def create_timeline_as_dict() -> dict:
    timeline_list = create_timeline()
    _timeline_as_dict = dict()
    for item in timeline_list:
        _unit = (item[0], item[2])
        try:
            _timeline_as_dict[item[1]].append(_unit)
        except KeyError:
            _timeline_as_dict[item[1]] = [_unit]
    return _timeline_as_dict


if __name__ == "__main__":
    pprint(create_timeline_as_dict())
