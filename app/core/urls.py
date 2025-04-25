from django.contrib import admin
from django.urls import path
from app.treeview_menu.views import MenuPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Примеры страниц с меню
    path('', MenuPageView.as_view(), name='home'),
    path('jh', MenuPageView.as_view(), name='about'),
    path('page/<slug:slug>/', MenuPageView.as_view(), name='dynamic_page'),
]