from django.urls import path
from myslug import ResumeDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume/', ResumeDetailView.as_view() ,name='resume'),
    
]
    


