from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('families', views.FamilyViewSet, 'families')

urlpatterns = router.urls
