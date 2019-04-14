from django.urls import path
from .views import ListMenuSections, MenuDetailView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('menusection', ListMenuSections.as_view())
  , path('menusection/<int:pk>', MenuDetailView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)


