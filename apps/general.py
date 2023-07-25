from .models import Food, Category

def global_data(request):
    data={
        'foodData':Food.objects.all(),
        'categoryData':Category.objects.all()
    }
    return data