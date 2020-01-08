from datetime import date, datetime
import requests
from bs4 import BeautifulSoup
from response_options import ResponseBuilder

class LunchLady:

    def goGetLunch(self):

        # NAVIGATE TO WEBSITE FIND ELEMENTS FOR DATES AND MENU ITEMS
        res = requests.get('https://www.central51.net/o/central-school-district-51/dining?filter=5601')
        res.raise_for_status()
        pageHtml = BeautifulSoup(res.text, features='html.parser')
        date_elements = pageHtml.select('.current-date-menu') # FINDING ELEMENTS BY CLASS
        menu_elements = pageHtml.select('.menu-list')

        # INITIALIZE LISTS TO HOLD STRINGS FROM WEB
        date_list = []
        menu_item_list = []

        # GET TODAY'S DATE AND FORMAT TO:<'THURSDAY, Jan 30 '> <---NOTE SPACE @ END
        today = datetime.now()
        week_day = today.strftime('%A, ')
        monthDay = today.strftime('%b %d ')
        formatted_date = week_day.upper() + monthDay # POTENTIAL BUG, PUT IN A SPACE

        # LOOP THROUGH THE BEAUTIFULSOUP ELEMENTS AND APPEND TEXT
        # OF EACH TO STRINGS TO THE APPROPRIATE LIST
        i = 0
        while i < len(date_elements):
            date_list.append(date_elements[i].getText())
            menu_item_list.append(menu_elements[i].getText())
            i += 1

        # PASS TODAY'S DATE INTO THE date_list TO FIND A MATCH AND GET THE INDEX VALUE
        j = date_list.index(formatted_date) # formatted_date GOES HERE WHEN NOT DEBUGGING

        # THEN PASS INDEX TO GET CORRESPONDING MENU FOR THAT DAY
        lunch_text = menu_elements[j].getText()

        # FORMAT STRING TO REMOVE LINE BREAKS AND REMOVE FIRST AND LAST COMMAS IN STRING
        lunch_text.replace('\n', ', ')
        l = list(lunch_text)
        l[0] = ''
        e = len(l)
        l[e - 1] = '.'
        s = ''.join(l)

        # BUILD THE RESPONSE FOR ALEXA TO SPEAK
        response = ResponseBuilder()
        alexa_response = response.get_pre_response() + str(s.replace('\n', ', ')) \
                         + response.get_post_response()

        #print(alexa_response)

        return alexa_response
