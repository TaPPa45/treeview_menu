from django.contrib import admin
from django.urls import path
from treeview_menu.views import MenuPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MenuPageView.as_view(), name='home'),
    path('about', MenuPageView.as_view(), name='about'),
    path('page/<slug:slug>/', MenuPageView.as_view(), name='dynamic_page'),
]