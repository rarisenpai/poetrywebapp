from django.urls import path

from . import views
urlpatterns = [
  path('poems',views.PoemsListView.as_view(), name="poems.list"),
  path('poems/<int:pk>',views.PoemsDetailView.as_view(), name="poems.detail"),
  path('poems/new',views.PoemsCreateView.as_view(),name="poems.new"),
  path('poems/<int:pk>/edit',views.PoemsUpdateView.as_view(),name="poems.update"),
  path('poems/<int:pk>/delete',views.PoemsDeleteView.as_view(),name="poems.delete")
]