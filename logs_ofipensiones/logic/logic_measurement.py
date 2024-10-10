from ..models import Logs

def get_Logs():
    queryset = Logs.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_Logs(form):
    log = form.save()
    log.save()
    return ()