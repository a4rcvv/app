from rest_framework import routers
from .views import PostViewset

router = routers.SimpleRouter()
router.register("", PostViewset)
urlpatterns = router.urls
