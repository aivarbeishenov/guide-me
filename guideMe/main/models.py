import datetime

from django.db import models


class Trip(models.Model):
    created_date = models.DateTimeField('Дата создаения заявки', default=datetime.date.today)
    customer_name = models.CharField('Имя клиента', max_length=50, null=None)
    customer_surname = models.CharField('Фамилия клиента', max_length=50, null=None)
    customer_email = models.EmailField('Электронная почта', null=None)
    knows_where_to_go = models.BooleanField('Знает куда лететь', default=True)
    country_to_visit = models.CharField('Страна визита', max_length=50, null=None)
    trip_start_date = models.DateTimeField('Дата начала поездки')
    trip_finish_date = models.DateTimeField('Дата завершения поездки')


    def __str__(self):
        return self.customer_name
