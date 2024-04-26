from abc import ABC, abstractmethod

# Abstract base class for a login form
class LoginForm(ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def authenticate(self):
        pass

# Concrete implementation of a login form using username and password
class UsernamePasswordForm(LoginForm):
    def validate(self):
        # Validate the username and password
        if len(self.username) < 3 or len(self.password) < 8:
            return False
        return True

    def authenticate(self):
        # Authenticate the user using the username and password
        # Replace this with your actual authentication logic
        if self.username == "admin" and self.password == "password":
            return True
        return False

# Concrete implementation of a login form using email and password
class EmailPasswordForm(LoginForm):
    def validate(self):
        # Validate the email and password
        if not self.username.endswith("@example.com") or len(self.password) < 8:
            return False
        return True

    def authenticate(self):
        # Authenticate the user using the email and password
        # Replace this with your actual authentication logic
        if self.username == "user@example.com" and self.password == "password":
            return True
        return False

# Create a dynamic login form based on user input
def create_login_form(username, password, form_type):
    if form_type == "username_password":
        return UsernamePasswordForm(username, password)
    elif form_type == "email_password":
        return EmailPasswordForm(username, password)
    else:
        raise ValueError("Invalid form type")

# Example usage
username = "admin"
password = "password"
form_type = "username_password"

login_form = create_login_form(username, password, form_type)

if login_form.validate():
    if login_form.authenticate():
        print("Login successful!")
    else:
        print("Invalid credentials")
else:
    print("Invalid input")