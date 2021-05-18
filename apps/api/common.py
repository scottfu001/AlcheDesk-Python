from django.utils import timezone


class SoftDeleteModel():

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()
