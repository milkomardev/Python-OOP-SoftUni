class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, value) -> None:
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = value
        
    @property
    def password(self) -> str:
        return self.__password
    
    @password.setter
    def password(self, value) -> None:
        is_valid_length = len(value) >= 8
        is_upper_case_presented = len([c for c in value if c.isupper()]) > 0
        is_digit_presented = len([c for c in value if c.isdigit()]) > 0

        if is_digit_presented and is_upper_case_presented and is_valid_length:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)