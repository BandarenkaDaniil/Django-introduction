from django.contrib import admin

from .models import Ride
from .models import Route
from .models import RouteItem
from .models import Station
from .models import Train
from .models import Track


admin.site.register(Ride)
admin.site.register(Route)
admin.site.register(RouteItem)
admin.site.register(Station)
admin.site.register(Train)
admin.site.register(Track)

