import random


class ResponseBuilder:

    pre_response = ['The lunch ladies will be serving ',
                    'Lunch at Washington Central school today is ',
                    'Your taste buds will be dancing for ',
                    'Get your fork and spoon, here comes lunch! ']

    post_response = [' That sounds absolutely delicious!',
                     ' Wow, if only I had a mouth I would be all over that.',
                     ' Yum! Thank you Michelle Obama!',
                     ' That sounds, uh, really, ummmm, good?']

    def get_pre_response(self):
        string = str(random.choice(self.pre_response))
        return string

    def get_post_response(self):
        string = str(random.choice(self.post_response))
        return string

    def get_past_lunch_response(self):
        string = 'Lunch has already been served today. If you want to know ' \
                 'tomorrow\'s lunch ask what\'s for lunch tomorrow'
        return string