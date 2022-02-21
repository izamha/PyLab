import datetime as dt


class Member:
    """ The Member class attributes and methods are for everyone """
    expiry_days = 365

    # Initialize a member object
    def __init__(self, firstname, lastname):
        # Attributes (instance variables) for everyone
        self.firstname = firstname
        self.lastname = lastname

        # Calculate expiry date from today's date
        self.expiry_date = dt.date.today() + dt.timedelta(days=self.expiry_days)
        # Default secret_code
        self.secret_code = ''

    def showexpiry(self):
        return f"{self.firstname} {self.lastname} expires on {self.expiry_date}"


# Subclass for the Admin
class Admin(Member):
    expiry_days = 365.2422 * 100

    def __init__(self, firstname, lastname, secret_code):
        super().__init__(firstname, lastname)
        self.secret_code = secret_code


# Subclass for the User
class User(Member):
    pass
