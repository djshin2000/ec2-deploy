from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver


class Photo(models.Model):
    file = models.ImageField(upload_to='photo', blank=True)


@receiver(pre_delete, sender=Photo)
def remove_file_from_s3(sender, instance, **kwargs):
    instance.file.delete(save=False)


@receiver(pre_save, sender=Photo)
def change_file_from_s3(sender, instance, **kwargs):
    try:
        old_obj = Photo.objects.get(pk=instance.pk)
    except ObjectDoesNotExist:
        print('예외 발생(ObjectDoesNotExist): ', ObjectDoesNotExist)
        return False
    except Exception as ex:
        print('예외 발생: ', ex)
        return False
    old_obj.file.delete(save=False)
