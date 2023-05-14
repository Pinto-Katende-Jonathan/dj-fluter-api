from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Publication(models.Model):
    description = models.TextField(max_length=100000)
    #pub_img = models.ImageField(null=True)
    date_pub = models.DateTimeField(auto_now_add=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pub {self.id} msg({self.discussion_set.count()})"
        # self.discussion_set.count() : ici on compte le nombre des discussions que contient la publication


class Discussion(models.Model):
    message = models.TextField(max_length=100000)
    date_msg = models.DateTimeField(auto_now_add=True, blank=True)
    pub_id = models.ForeignKey(Publication, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"msg from {self.user_id.username} related to pub {self.pub_id}"