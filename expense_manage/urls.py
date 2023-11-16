from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from base.views import *


admin.site.site_header = 'Inductus | Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',loginview,name = "login"),
    path('logout/',logoutview,name="logout"),
    path('',EmployeeView,name = "employees"),
    path('employee/<str:pk>/',EmployeeProfileView,name = "employee"),
    path('employee/<str:pk>/atp/',AdvancedTravelPlanView,name='atp'),
    path('employee/<str:pk>/tp',ActualTravelPlan,name ="tp"),
    path('employee/<str:pk1>/tp/<str:pk2>/',ViewAtp,name = "viewatp"),
    
]

handler404 = "base.views.error404"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
