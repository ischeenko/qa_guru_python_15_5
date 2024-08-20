from demoqa_tests.pages.registration_page import RegistrationFormPage
from demoqa_tests.data import user


def test_fill_registration_form():
    alex = user.user_data
    register_page = RegistrationFormPage()

    register_page.open()
    register_page.register(alex)
    register_page.should_register_user_with(alex)
