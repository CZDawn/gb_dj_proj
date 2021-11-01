from basketapp.models import Basket

def basket(request):
   basket = []
   if request.user.is_authenticated:
       #basket = request.user.basket.select_related()
       basket = Basket.objects.filter(user=request.user)
   return {'basket': basket,}

