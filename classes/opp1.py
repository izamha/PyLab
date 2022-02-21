import datetime as dt


class Member:
    """ Create a new member. """
    free_days = 365

    def __init__(self, uname, fname):
        # Define attributes and give them values
        self.username = uname
        self.fullname = fname
        # Default date_joined to today's date
        self.date_joined = dt.date.today()
        # Set is active to True initially.
        self.is_active = True

    @classmethod
    def setfreedays(cls, days):
        cls.free_days = days

    # Methods for each instance created (instance method)
    # A method to return a formatted string with showing date joined
    def show_date_joined(self):
        return f"{self.fullname} joined on {self.date_joined:%m %d %y}"

    @staticmethod
    def currenttime():
        now = dt.datetime.now()
        return f'{now:%I:%M %p}'


# Class definition ends at last indented line
# Try out the new static method

print(Member.currenttime())
