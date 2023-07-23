from .models import Food

def global_data(request):
    data={
        'foodData':Food.objects.all()
    }
    return data