from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag, related_name="tasks")

    class Meta:
        ordering = ["is_completed", "created_at", "deadline"]

    def __str__(self):
        return f"{self.content} {self.created_at}"
