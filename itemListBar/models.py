from django.db import models


class UserCardsModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    month = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    gender = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    house = models.IntegerField(default=0)
    apartment = models.IntegerField(default=0)
    purpose = models.CharField(max_length=30)
    money = models.IntegerField(default=0)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
