def total_price(request):
    
    total = 0
    
    if request.user.is_authenticated:
        for key, value in request.session['kart'].items():
            total += float(value['precio'])
            
    return {'total_price':total}