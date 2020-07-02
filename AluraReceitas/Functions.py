from typing import Union, Dict
from django.contrib.auth.models import User


class Authenticate(object):

    def user_authenticate(self, user: str, password: Union[str, int],
                          password2: Union[str, int]) -> Union[Dict[str, Union[str, int]], bool]:
        if not User.objects.filter(email__contains=user).exists():
            if all((user.strip(), password.strip(), password2.strip())):
                if password == password2:
                    user_inf: Dict[str, Union[str, int]] = {'user': user, 'password': password}
                    return user_inf
        return False

