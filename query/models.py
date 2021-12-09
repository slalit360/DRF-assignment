from django.db import models
from account.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'query/{}'.format(filename)


# Create your models here.
class Query(models.Model):
    title = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=1000, blank=False)
    file = models.FileField(upload_to=user_directory_path, blank=True)
    user = models.ForeignKey(User, blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.title)


class Answer(models.Model):
    query = models.ForeignKey(Query, blank=False, related_name='answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000, blank=False)
    answered_by = models.ForeignKey(User, blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.query) + " -> " + str(self.answer)
