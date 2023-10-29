from .models import Trip
from django.forms import ModelForm, TextInput, EmailInput, DateTimeInput, NullBooleanSelect


class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['customer_name', 'customer_surname', 'customer_email', 'country_to_visit', 'trip_start_date',
                  'trip_finish_date', 'knows_where_to_go']

        widgets = {
            "customer_name": TextInput(attrs={
                'class': 'form-control',
                'id': 'customer_name',
                'placeholder': 'Имя'
            }),
            "customer_surname": TextInput(attrs={
                'class': 'form-control',
                'id': 'customer_surname',
                'placeholder': 'Фамилия'
            }),
            "country_to_visit": TextInput(attrs={
                'class': 'form-control',
                'id': 'country_to_visit',
                'placeholder': 'Страна визита'
            }),

            "customer_email": EmailInput(attrs={
                'class': 'form-control',
                'id': 'customer_email',
                'placeholder': 'Электронный адрес'
            }),
            "knows_where_to_go": NullBooleanSelect(),
            "trip_start_date": DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'placeholder': 'Дата начала поездки'
            }),
            "trip_finish_date": DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'placeholder': 'Дата конца поездки'
            }),
        }
