from pages.registration_page import RegistrationFormPage


def test_sucess_registration_demoqa():
    registration_page = RegistrationFormPage()
    registration_page.open()
    registration_page.fill_first_name('Alexander')
    registration_page.fill_last_name('Ischenko')
    registration_page.fill_email('ischeenko@gmail.com')
    registration_page.choose_gender('Male')
    registration_page.fill_number('7978150151')
    registration_page.fill_date_of_birth('13', 'January', '1994')
    registration_page.choose_subject_and_hobby('English', 'Sports')
    registration_page.upload_file('resources/images.jpeg')
    registration_page.fill_address('Saki', 'NCR', 'Delhi')
    registration_page.should_registerted_user(
        "Alexander Ischenko",
        "ischeenko@gmail.com",
        "Male",
        "7978150151",
        "13 January,1994",
        "English",
        "Sports",
        "images.jpeg",
        "Saki",
        "NCR Delhi"
    )
