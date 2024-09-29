from django.urls import path
from todo.views import (
    index,
    complete_task,
    tag_list,
    add_task,
    update_task,
    delete_task,
    add_tag,
    update_tag,
    delete_tag,
)

app_name = "todo"

urlpatterns = [
    path("", index, name="index"),
    path("complete_task/<int:task_id>/", complete_task, name="complete_task"),
    path("tags/", tag_list, name="tag_list"),
    path("add_task/", add_task, name="add_task"),
    path("update_task/<int:task_id>/", update_task, name="update_task"),
    path("delete_task/<int:task_id>/", delete_task, name="delete_task"),
    path("add_tag/", add_tag, name="add_tag"),
    path("update_tag/<int:tag_id>/", update_tag, name="update_tag"),
    path("delete_tag/<int:tag_id>/", delete_tag, name="delete_tag"),

]
