"""
URL configuration for test_irisa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.urls import path
from django.contrib import admin

import manager.views as manager_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('worker_list/', manager_view.WorkerListView.as_view(), name='worker_list'),  # URLとViewを組み合わせる！
    path('', manager_view.home, name='home'),
]

