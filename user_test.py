import unittest
from user import User


class User_Test(unittest.TestCase):
    def setUp(self):
        self.fixture = self._Fixture()

    def test_create_user_with_no_field(self):
        self.fixture.given_create_user_fields_with_no_fileds()
        self.fixture.when_create_operation_is_called_with_no_field()
        self.fixture.then_status_should_be_this(False)

    def test_create_user_with_valid_required_fields(self):
        self.fixture.given_create_user_fields("Talha Ayub", "talha.ayub@qbatch.com", "abcd@1234")
        self.fixture.when_create_operation_is_called()
        self.fixture.then_status_should_be_this(True)

    def test_create_user_with_required_and_optional_fields(self):
        self.fixture.given_create_user_fields("Talha Ayub", "talha.ayub@qbatch.com", "abcd@1234", 24, "Canal road")
        self.fixture.when_create_operation_is_called()
        self.fixture.then_status_should_be_this(True)

    def test_create_user_with_invalid_username_field(self):
        self.fixture.given_create_user_fields("Talha@_@Ayub", "talha.ayub@qbatch.com", "abcd@1234", 24, "Canal road")
        self.fixture.when_create_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    def test_create_user_with_invalid_email_field(self):
        self.fixture.given_create_user_fields("Talha Ayub", "talha.ayub", "abcd@1234", 24, "Canal road")
        self.fixture.when_create_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    def test_create_user_with_invalid_password_field(self):
        self.fixture.given_create_user_fields("Talha Ayub", "talha.ayub@qbatch.com", "Talha Ayub", 24, "Canal road")
        self.fixture.when_create_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    def test_create_user_with_invalid_age_field(self):
        self.fixture.given_create_user_fields("Talha Ayub", "talha.ayub@qbatch.com", "Talha Ayub", "24", "Canal road")
        self.fixture.when_create_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    def test_create_user_with_already_existing_email_field(self):
        self.fixture.given_create_user_fields("Talha Ayub", "talha.ayub@qbatch.com", "abcd@1234", 24, "Canal road")
        self.fixture.when_create_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    def test_read_user_with_valid_email(self):
        self.fixture.given_read_user_field("talha.ayub@qbatch.com")
        self.fixture.when_read_operation_is_called()
        self.fixture.then_status_should_be_this(True)

    def test_read_user_with_invalid_email(self):
        self.fixture.given_read_user_field("talha.ayub")
        self.fixture.when_read_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    def test_read_user_with_empty_email_field(self):
        self.fixture.given_read_user_field("")
        self.fixture.when_read_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    def test_update_username_with_valid_email(self):
        self.fixture.given_update_user_field("Ali Usman", "talha.ayub@qbatch.com")
        self.fixture.when_update_username_operation_is_called()
        self.fixture.then_status_should_be_this(True)

    def test_update_username_with_invalid_email(self):
        self.fixture.given_update_user_field("Ali Usman", "talha.ayub")
        self.fixture.when_update_username_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    def test_update_username_with_empty_email_field(self):
        self.fixture.given_update_user_field("Ali Usman", "")
        self.fixture.when_update_username_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    def test_update_password_with_valid_email(self):
        self.fixture.given_update_user_field("1234@abcd", "talha.ayub@qbatch.com")
        self.fixture.when_update_password_operation_is_called()
        self.fixture.then_status_should_be_this(True)

    def test_update_password_with_invalid_password_and_valid_email(self):
        self.fixture.given_update_user_field("Talha Ayub", "talha.ayub@qbatch.com")
        self.fixture.when_update_password_operation_is_called()
        self.fixture.then_status_should_be_this(True)

    def test_update_password_with_wrong_email(self):
        self.fixture.given_update_user_field("1234@abcd", "talha.ayub")
        self.fixture.when_update_password_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    def test_update_password_with_empty_email_field(self):
        self.fixture.given_update_user_field("1234@abcd", "")
        self.fixture.when_update_password_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    def test_update_age_with_valid_email(self):
        self.fixture.given_update_user_field(24, "talha.ayub@qbatch.com")
        self.fixture.when_update_password_operation_is_called()
        self.fixture.then_status_should_be_this(True)

    def test_update_age_with_invalid_age_and_valid_email(self):
        self.fixture.given_update_user_field("24", "talha.ayub@qbatch.com")
        self.fixture.when_update_password_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    def test_update_age_with_wrong_email(self):
        self.fixture.given_update_user_field(24, "talha.ayub")
        self.fixture.when_update_password_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    def test_update_age_with_empty_email_field(self):
        self.fixture.given_update_user_field(24, "")
        self.fixture.when_update_password_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    def test_update_addresss_with_valid_email(self):
        self.fixture.given_update_user_field("Peoples Colony", "talha.ayub@qbatch.com")
        self.fixture.when_update_address_operation_is_called()
        self.fixture.then_status_should_be_this(True)

    def test_update_addresss_with_wrong_email(self):
        self.fixture.given_update_user_field("Peoples Colony", "talha.ayub")
        self.fixture.when_update_address_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    def test_update_addresss_with_empty_email_field(self):
        self.fixture.given_update_user_field("Peoples Colony", "")
        self.fixture.when_update_address_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    def test_delete_username_with_valid_email(self):
        self.fixture.given_delete_user_field("talha.ayub@qbatch.com")
        self.fixture.when_delete_user_operation_is_called()
        self.fixture.then_status_should_be_this(True)

    def test_delete_username_with_invalid_email(self):
        self.fixture.given_delete_user_field("talha.ayub")
        self.fixture.when_delete_user_operation_is_called()
        self.fixture.then_status_should_be_this(False)

    class _Fixture(unittest.TestCase):
        def __init__(self):
            self.user = User()

        def given_create_user_fields_with_no_fileds(self):
            pass

        def when_create_operation_is_called_with_no_field(self):
            pass

        def given_create_user_fields(self, username, email, password, *agrs):
            self.username = username
            self.email = email
            self.password = password
            self.agrs = agrs

        def given_read_user_field(self, email):
            self.email = email

        def given_update_user_field(self, update_field, email):
            self.update_field = update_field
            self.email = email

        def given_delete_user_field(self, email):
            self.email = email

        def when_create_operation_is_called(self):
            self.status = self.user.create_user(
                self.username, self.email, self.password, self.agrs)

        def when_read_operation_is_called(self):
            self.status = self.user.read_user(self.email)

        def when_update_username_operation_is_called(self):
            self.status = self.user.update_username(
                self.update_field, self.email)

        def when_update_password_operation_is_called(self):
            self.status = self.user.update_email(self.update_field, self.email)

        def when_update_age_operation_is_called(self):
            self.status = self.user.update_age(self.update_field, self.email)

        def when_update_address_operation_is_called(self):
            self.status = self.user.update_address(
                self.update_field, self.email)

        def when_delete_user_operation_is_called(self):
            self.status = self.user.delete_user(self.email)

        def then_status_should_be_this(self, expected_status):
            self.assertTrue(self.status, expected_status)


if __name__ == "__main__":
    unittest.main()
