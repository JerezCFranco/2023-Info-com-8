# -Crea una función llamada calcular_descuento que tome dos parámetros:
# precio y porcentaje_descuento. La función debe calcular y devolver el precio
# después de aplicar el descuento.

def calcularDescuento(precio,descuento):
    descuentoAplicado=precio*(descuento/100)
    preciototal=precio-descuentoAplicado
    return (f"El precio final del producto con el descuento aplicado es de {preciototal}$.")

precio = int(input("Ingrese el precio del producto: "))
descuento = int(input("Ingrese el porcentaje de descuento aplicado al producto: "))
print(calcularDescuento(precio,descuento))