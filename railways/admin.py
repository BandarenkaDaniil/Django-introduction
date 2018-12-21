from django.contrib import admin

# from .models import Train
from .models import Station
from .models import Track
from .models import Route
from .models import RouteItem

# admin.site.register(Train)
admin.site.register(Station)
admin.site.register(Track)
admin.site.register(Route)
admin.site.register(RouteItem)

