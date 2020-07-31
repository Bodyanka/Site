from django.urls import path
from . import views

app_name = 'sharingsite'

urlpatterns = [

    # /upload/
    path('', views.FileUpload.as_view(), name='upload'),

    # /download/?file_link=*link*
    path('media/', views.FileDownload.as_view(), name='download'),

    # /link/*pk*
    path('link/<int:pk>', views.Link.as_view(), name='link'),

]
