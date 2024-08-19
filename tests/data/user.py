from dataclasses import dataclass
from selene import browser, have, command
import os

@dataclass
class User:
    name: str
    surname: str
    email: str
    gender: str
    date_of_birth: str
    subject: str
    hobby: str
    file: str
    address: str
    state: str
    city: str

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def choose_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def fill_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, date_of_birth):
        day, month, year = date_of_birth.split(' ')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').select_option(month)
        browser.element('.react-datepicker__year-select').select_option(year)
        day_selector = f'.react-datepicker__day--0{int(day)}:not(.react-datepicker__day--outside-month)'
        browser.element(day_selector).click()

    def choose_subject_and_hobby(self, subject, hobby):
        browser.element('#subjectsInput').type(subject).press_enter()
        browser.all('.custom-checkbox').element_by(have.exact_text(hobby)).perform(command.js.scroll_into_view).click()

    def upload_file(self, value):
        browser.element('#uploadPicture').send_keys(os.path.abspath(value))

    def fill_address(self, address, state, city):
        browser.element('#currentAddress').type(address)
        browser.element("#react-select-3-input").type(state).press_enter()
        browser.element('#react-select-4-input').type(city).press_enter()
        browser.element('#submit').click()

    def should_registerted_user(self, full_name, mail, gender, number, date_of_birth, subject, hobby, file, address, state_and_city):
        browser.element('.modal-content').element('table').all('tr').all('td').even.should(have.exact_texts(
            full_name, mail, gender, number, date_of_birth, subject, hobby, file, address, state_and_city
        ))

    def fill_registration_form(self):
        self.fill_first_name(self.name)
        self.fill_last_name(self.surname)
        self.fill_email(self.email)
        self.choose_gender(self.gender)
        self.fill_date_of_birth(self.date_of_birth)
        self.choose_subject_and_hobby(self.subject, self.hobby)
        self.upload_file(self.file)
        self.fill_address(self.address, self.state, self.city)

    def assert_result_registration(self):
        full_name = f"{self.name} {self.surname}"
        state_and_city = f"{self.state} {self.city}"
        self.should_registerted_user(
            full_name,
            self.email,
            self.gender,
            '7978150151',
            self.date_of_birth,
            self.subject,
            self.hobby,
            self.file.split('/')[-1],
            self.address,
            state_and_city
        )



user_data = User(
    name='Alexander',
    surname='Ischenko',
    email='ischeenko@gmail.com',
    gender='Male',
    date_of_birth='13 January 1994',
    subject='English',
    hobby='Sports',
    file='resources/images.jpeg',
    address='Saki',
    state='NCR',
    city='Delhi'
)

# Заполнение формы и проверка результатов
user_data.open()
user_data.fill_registration_form()
user_data.assert_result_registration()

