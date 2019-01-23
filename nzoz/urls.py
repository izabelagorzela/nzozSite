from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('poradniapsychologiczna/', views.poradnia_psychologiczna, name='poradnia_psychologiczna'),
    path('poradniapsychiatryczna/', views.poradnia_psychiatryczna, name='poradnia_psychiatryczna'),
    path('rejestracja/', views.rejestracja, name='rejestracja'),
    path('lokalizacja/', views.lokalizacja, name='lokalizacja'),

    path('poradniapsychologiczna/index', views.index, name='por_psycho_index'),
    path('poradniapsychologiczna/poradniapsychiatryczna', views.poradnia_psychiatryczna, name='por_psycho_por_psychiatryczna'),
    path('poradniapsychologiczna/rejestracja', views.rejestracja, name='por_psycho_rejestracja'),
    path('poradniapsychologiczna/lokalizacja', views.lokalizacja, name='por_psycho_lokalizacja'),

    path('poradniapsychiatryczna/index', views.index, name='por_psychia_index'),
    path('poradniapsychiatryczna/poradniapsychologiczna', views.poradnia_psychologiczna, name='por_psychia_por_psychologiczna'),
    path('poradniapsychiatryczna/rejestracja', views.rejestracja, name='por_psychia_rejestracja'),
    path('poradniapsychiatryczna/lokalizacja', views.lokalizacja, name='por_psychia_lokalizacja'),

    path('rejestracja/index', views.index, name='rejestracja_index'),
    path('rejestracja/poradniapsychologiczna', views.poradnia_psychologiczna, name='rejestracja_por_psychologiczna'),
    path('rejestracja/poradniapsychiatryczna', views.poradnia_psychiatryczna, name='rejestracja_por_psychiatryczna'),
    path('rejestracja/lokalizacja', views.lokalizacja, name='rejestracja_lokalizacja'),

    path('lokalizacja/index', views.index, name='lokalizacja_index'),
    path('lokalizacja/poradniapsychologiczna', views.poradnia_psychologiczna, name='lokalizacja_por_psychologiczna'),
    path('lokalizacja/poradniapsychiatryczna', views.poradnia_psychiatryczna, name='lokalizacja_por_psychiatryczna'),
    path('lokalizacja/rejestracja', views.lokalizacja, name='lokalizacja_rejestracja'),

]

