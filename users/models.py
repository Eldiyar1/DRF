import random
from django.contrib.auth.models import User
from django.db import models


class Confirm_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.code

    @staticmethod
    def generate_random_code():
        code = random.randint(111111, 999999)
        return str(code)
