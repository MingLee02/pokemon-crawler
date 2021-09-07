from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from pokemon import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '',
        views.HomeView.as_view(),
        name='home'
    ),
    path(
        'pokemon-list/<int:version_id>',
        views.PokemonListView.as_view(),
        name='pokemon-list'
    ),
    path("pokemon/<int:pk>", views.PokemonDetailView.as_view(), name="pokemon_details"),
]


if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)