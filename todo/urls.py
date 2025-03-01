from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet) # Api will be available at /api/todos/

# from .views import todo_list
urlpatterns = [
    path('api/', include(router.urls)),
    # path('api/todos/', todo_list),
]
    