from django.db.models.signals import post_save
from django.dispatch import receiver
from service.blackend.models.notice import Messquery, Messblack, Messtemp
from service.interface.contrib.pusher import Push


@receiver(post_save, sender=Messquery)
def post_notice_push(instance, created, **kwargs):
    if created:
        if instance.channel.channel == u"推送":
            try:
                black = Messblack.objects.get(bid=instance.group.id)
                return False
            except Messblack.DoesNotExist:
                typels = Messtemp.objects.get(type=instance.type)
                message = instance.content + typels.content
                return Push.use().send(alias=instance.group.id, message=message, extras={})

        elif instance.channel.channel == u"短信":
            pass
