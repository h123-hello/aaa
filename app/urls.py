from django.urls import path
from app import views
urlpatterns = [
    path("user/",views.UserAPIView.as_view()),
    # path('check/',views.RegisterView.as_view({"get":"check_user"})),
    path("emp/".views.EmployeeModelSerializer.as_view)
]