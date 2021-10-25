from django.db import models

# Create your models here.


class GameUser(models.Model):
    '''
    Модель пользователя сайта.
    '''
    email = models.EmailField(
        'Почта',
        max_length=255,
        primary_key=True,
    )

    game_count = models.PositiveSmallIntegerField(
        'Количество игр',
        default=1,
    )


class EspSystemUser(models.Model):
    '''
    Имитация базы данных ESP-системы.
    '''

    email = models.EmailField(
        'Почта',
        max_length=255,
        primary_key=True,
    )