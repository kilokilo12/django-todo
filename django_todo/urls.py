
from django.conf.urls import url
from django.contrib import admin
from todo.views import get_todo_list, create_an_item, edit_an_item, toggle_status

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_todo_list),
    url(r'^add$', create_an_item),
    url(r'^edit/(?P<id>\d+)$', edit_an_item),
    url(r'^toggle/(?P<id>\d+)$', toggle_status)
]
