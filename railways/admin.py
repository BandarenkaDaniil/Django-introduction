from django.contrib import admin

from .models import (
    Ride,
    Route,
    RouteItem,
    Station,
    Ticket,
    Train,
    Track,
)

admin.site.register(Ride)
admin.site.register(Route)
admin.site.register(RouteItem)
admin.site.register(Station)
admin.site.register(Ticket)
admin.site.register(Train)
admin.site.register(Track)
