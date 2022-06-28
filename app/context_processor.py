def total_carrito(request):
    total_precio = 0
    total = 0
    descuento = 0
    total_desc = 0
    stock = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["precio"])
                descuento = round(total * 0.05)
                total_desc = round(total * 0.95)
                stock =  value["stock"] - value["cant"]
    return{"total_carrito": total, "descuento": descuento, "total_desc": total_desc, "stock":stock, "total_precio":total_precio}
