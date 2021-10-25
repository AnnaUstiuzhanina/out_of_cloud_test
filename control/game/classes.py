from . models import EspSystemUser

class EspSystem:
    '''
    Имитация ESP-системы.
    '''

    def __init__(self, url: str, key: str):
        self.url = url
        self.key = key

    def check_email(self, email: str) -> bool:
        '''
        Проверка наличия почты пользователя в БД ESP.
        '''
        email_exists = EspSystemUser.objects.filter(email=email)

        if email_exists:
            return True

        return False

    def create_email(self, email: str) -> bool:
        '''
        Добавление почты пользователя в БД ESP.
        '''
        new_email = EspSystemUser.objects.create(email=email)
        new_email.save()

        return True

    def process_email(self, email: str) -> bool:
        '''
        Обработка адреса почты пользователя в ESP-системе.
        '''
        in_esp = self.check_email(email)

        if in_esp:
            return True

        else:
            self.create_email(email)
            return False
