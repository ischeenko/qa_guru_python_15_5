from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    date_of_birth: str
    subject: str
    hobby: str
    file: str
    address: str
    state: str
    city: str

