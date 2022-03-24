from django.urls import path

from group.views import (
    create_group_view,
    join_group_view,
    group_view,
    leave_group_view,
)

app_name = 'group'

urlpatterns = [
    path('', group_view, name="group_info"),
    path('join_group/', join_group_view, name="join_group"),
    path('leave_group/', leave_group_view, name="leave_group"),
]