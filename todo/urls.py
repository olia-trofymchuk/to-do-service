from django.urls import path

from todo.views import (
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskListView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    change_task_status,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task_create"),
    path(
        "tasks/update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"
    ),
    path(
        "tasks/delete/<int:pk>/", TaskDeleteView.as_view(), name="task_delete"
    ),
    path(
        "tasks/change_task_status/<int:pk>/",
        change_task_status,
        name="change_status",
    ),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/create/", TagCreateView.as_view(), name="tag_create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag_update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag_delete"),
]

app_name = "todo"
