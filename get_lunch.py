from datetime import date, datetime
import requests
from bs4 import BeautifulSoup
from response_options import ResponseBuilder
import re

class LunchLady:

    def goGetLunch(self, when_lunch):

        # NAVIGATE TO WEBSITE FIND ELEMENTS FOR DATES AND MENU ITEMS
        res = requests.get('https://www.central51.net/o/central-school-district-51/dining?filter=5601')
        #res = requests.get('https://www.d52schools.com/o/wms/dining?filter=4492')
        res.raise_for_status()
        pageHtml = BeautifulSoup(res.text, features='html.parser')
        date_elements = pageHtml.select('.current-date-menu') # FINDING ELEMENTS BY CLASS
        menu_elements = pageHtml.select('.menu-list')

        # INITIALIZE LISTS TO HOLD STRINGS FROM WEB
        date_list = []
        menu_item_list = []
        menu_re = re.compile(r'\d\)')

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
            #print(date_list[i])
            i += 1

        if formatted_date not in date_list and when_lunch == 'today':
            past_lunch = ResponseBuilder().get_past_lunch_response()
            return past_lunch

        # THEN PASS INDEX TO GET CORRESPONDING MENU FOR THAT DAY
        j = 0
        if (when_lunch == 'tomorrow') and (formatted_date in date_list): #
            j = 1

        lunch_text = menu_elements[j].getText()

        # FORMAT STRING TO REMOVE LINE BREAKS AND REMOVE FIRST AND LAST COMMAS IN STRING
        pre_build_text = self.prep_response(lunch_text)

        # BUILD THE RESPONSE FOR ALEXA TO SPEAK
        response = ResponseBuilder()
        alexa_response = date_list[j] + response.get_pre_response() + str(
            pre_build_text.replace(
                         '\n', ', ')) + response.get_post_response()

        alexa_speaks = menu_re.sub('', alexa_response)

        return alexa_speaks

    def prep_response(self, lunch_text):
        """Strips out first and last commas puts . at end"""
        lunch_text.replace('\n', ', ')
        l = list(lunch_text)
        l[0] = ''
        e = len(l)
        l[e - 1] = '.'
        s = ''.join(l)
        return s

    def determine_when(self, t):
        if t == 'today':
            lunch_text = self.menu_elements[0].getText()
        if t == 'tomorrow':
            lunch_text = self.menu_elements[1].getText()
        return lunch_text

