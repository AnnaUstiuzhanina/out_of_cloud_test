from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import GameUser
from .classes import EspSystem
from django.conf import settings

class GameUsers(APIView):
    '''
    Непосредственно работа Бэкенда.
    '''

    def get(self, request, format=None):

        # 4. Бэкенд принимает почту
        email = request.data.get('email')

        if email:

            in_esp = True

            # 5. Бэкенд смотрит в свою базу, играла почта или нет
            obj, created = GameUser.objects.get_or_create(
                email=email,
            )

            #7. Если в базе игры почта есть
            if not created:
                # бэкенд инкрементит в базе кол. игр
                obj.game_count += 1
                obj.save()

            # 6. Если в базе игры почты нет:
            else:
                # Бэкенд проверяет в ESP системе есть такая почта или нет
                # Если почты нет, создает ее в ESP системе
                # Бэкенд записывает в свою базу факт игры
                esp = EspSystem(settings.ESP_URL, settings.ESP_KEY)
                in_esp = esp.process_email(email)

            # 8. Бэкенд возвращает на фронт результат:
            return Response({
                "in_esp": in_esp,
                "in_db": not created,
                "game_count": obj.game_count,
            })

        # 404 в случае некорректных данных почты в полученном json
        else:
            return Response('Email field is required', status=status.HTTP_400_BAD_REQUEST) 

