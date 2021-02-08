from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('about', views.about, name= 'about'),
 path('profile', views.profile, name= 'profile'),
 path('accounts/signup', views.signup, name= 'signup'),
 path('login', views.login, name= 'login'),
 path('memory_new', views.memory_new, name= 'memory_new'),
 path('memory_delete/<int:memory_id>/', views.memory_delete, name= 'memory_delete'),
 path('memory_edit/<int:memory_id>/', views.memory_edit, name= 'memory_edit'),
path('memory_show/<int:memory_id>/', views.memory_show, name= 'memory_show'),
]

#  path('memory_delete/<int:memory_id>/', views.memory_delete, name= 'memory_delete')
#  path('memories_new/', views.make_memory, name='memories_new'),
#  path('memories_edit/<int:memory_id>/', views.memories_post, name='memories_edit'),
#  path('memories_delete/<int:memory_id>/', views.delete_post, name= 'memories_delete')