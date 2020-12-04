from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TotalPizzaAPIView, PizzaDetail, ArticleViewSet,SearchListView

router = DefaultRouter()
router.register('user',ArticleViewSet,basename='order')

urlpatterns = [
    path('',include(router.urls)),
    path('detail/<int:id>/', PizzaDetail.as_view()),
    path('search/', SearchListView.as_view()),
]
