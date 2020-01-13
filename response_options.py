import random

class ResponseBuilder:
    
    school_name = 'Washington Central 51'

    pre_response = ['The ' + school_name + ' lunch ladies will be serving ',
                    'Lunch at ' + school_name + ' today is ',
                    'Your taste buds will be dancing for ',
                    'Get your fork and spoon, here comes lunch! ']

    post_response = [' That sounds absolutely delicious!',
                     ' If only I could eat food I would be all over that.',
                     ' Yum! Thank you Michelle Obama!',
                     ' That sounds really good.',
                     ' You humans get all the good stuff.']
                     
    end_session_response = ['Have a great day!',
                            'God Bless',
                            'Good Day!',
                            'So long, kind human.',
                            'Hasta la vista, baby!',
                            'Until next time.']
    def get_pre_response(self):
        string = str(random.choice(self.pre_response))
        return string

    def get_post_response(self):
        string = str(random.choice(self.post_response))
        return string
        
    def get_end_session_response(self):
        string = str(random.choice(self.end_session_response))
        return string
        
    def get_past_lunch_response(self):
        string = 'Looks like lunch has already been served today. If you want to know ' \
                 'tomorrow\'s lunch at ' + self.school_name + ' ask what\'s for lunch tomorrow.'
        return string
        
