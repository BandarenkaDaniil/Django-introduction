from django.contrib import admin

from .models import Train
from .models import Ride
from .models import Station

admin.site.register(Train)
admin.site.register(Ride)
admin.site.register(Station)

