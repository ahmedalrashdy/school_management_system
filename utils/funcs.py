from django.utils import timezone

def upload_file(instance, filename,):
     date = timezone.now()
     return f"{date.year}/{date.month}/{date.day}/{filename}"
     
     