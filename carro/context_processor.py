def importe_total_carro(request):
    total = 0
    if request.session:
        #if request.user.is_authenticated:
        for key, value in request.session['carro'].items():
            total += float(value['precio']) # *value['cantidad'])
    return {'importe_total_carro':total}