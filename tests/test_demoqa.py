from demoqa_tests.pages.registration_page import RegistrationFormPage


# def test_demoqa_todo():
#     browser.open('/automation-practice-form')
#     browser.element('#firstName').type('Alexander')
#     browser.element('#lastName').type('Ischenko')
#     browser.element('#userEmail').type('ischeenko@gmail.com')
#     browser.element('[for="gender-radio-1"]').click()
#     browser.element('#userNumber').type('7978150151')
#     browser.element('#dateOfBirthInput').click()
#     browser.element('.react-datepicker__month-select option[value="0"]').click()
#     browser.element('.react-datepicker__year-select option[value="1994"').click()
#     browser.element('.react-datepicker__day.react-datepicker__day--013').click()
#     browser.element('#subjectsInput').type('English').press_enter()
#     browser.element('[for="hobbies-checkbox-1"]').perform(command.js.scroll_into_view).click()
#     browser.element('#uploadPicture').send_keys(os.path.abspath('images.jpeg'))
#     browser.element('#currentAddress').type('Saki')
#     browser.element("#react-select-3-input").type('NCR').press_enter()
#     browser.element('#react-select-4-input').type('Delhi').press_enter()
#     browser.element('#submit').click()
#     browser.element('.modal-content').element('table').all('tr').all('td').even.should(have.exact_texts(
#         "Alexander Ischenko",
#         "ischeenko@gmail.com",
#         "Male",
#         "7978150151",
#         "13 January,1994",
#         "English",
#         "Sports",
#         "images.jpeg",
#         "Saki",
#         "NCR Delhi",
#     )
#     )
def test_fill_registration_form():
    alex = User.Alex
    register_page = RegistrationFormPage()

    register_page.open()
    register_page.register(alex)
    register_page.should_registerted_user(alex)
