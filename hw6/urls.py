from rest_framework.routers import DefaultRouter

from hw6 import views

router = DefaultRouter()
router.register("products", views.ProductViewSet)
router.register("stocks", views.StockViewSet)

urlpatterns = router.urls
