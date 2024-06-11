
from django.contrib import admin
from django.urls import path,include
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin-access/', admin.site.urls),
    path('',include('company.urls')),
    path('',include('Users.urls')),
    path('',include('core.urls')),
    path('logistics/',include('logistics.urls')),
    path('myadmin/',include('myadmin.urls')),
    path('accounts/',include('django.contrib.auth.urls')),

]


if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


handler404 = 'core.views.error_404_handler'
handler500 = 'core.views.error_500_handler'
handler403 = 'core.views.error_403_handler'