# ----------------------------------------------------------------------------------------------+
# run this file to get the receipts to follow split by day                                     |
# when you finish meal, you can go back to 'receipts.py' and change 'zrobione' to True.         |
# ----------------------------------------------------------------------------------------------+

from datetime import date, datetime
from timeline import create_timeline_as_dict
from receipts import przepisy, create_multiplications
from enumerations import Acquisition
import textwrap


# Set the day you want to see the cooking workflow
# date today
current_date = datetime.now().date()
# or any other date
any_date = date(2023, 12, 23)
# choose one and set it here
receipts_for_date = current_date  # any_date # current_date

# creates multiplications to fit the ingredients amounts to number of people attending Christmas Eve dinner.
create_multiplications()

# background preparation of lists and dicts
timeline_dict = create_timeline_as_dict()

# the main code goes here
line_width = 90
n = 0
for meal in przepisy:
    if meal['jak'] == Acquisition.WE_MAKE_IT and meal['kiedy'] == receipts_for_date:
        try:
            # numbered meals to prepare for the day (i.e. today)
            n += 1
            # simple lines to make it more User friendly
            print('-' * line_width)
            print(f"{n}. {meal['nazwa'].capitalize()}. Ilość porcji: {meal['na ile porcji'] * meal['mnoznik']}")
            print('- ' * (line_width//2))
            # ingredients with corrected amounts given below
            for i, v in meal['składniki'].items():
                print(f"{i}: {v} vs. {round(v * meal['mnoznik'], 3)}")
            print('- ' * (line_width // 2))
            # the cooking formula itself
            wrapped_text = textwrap.wrap(meal['przepis'], width=line_width)
            for line in wrapped_text:
                print(line)
        except KeyError:
            # if something went wrong leave me a simple message to find the bug
            print(f"keyError for {meal['nazwa']}")
