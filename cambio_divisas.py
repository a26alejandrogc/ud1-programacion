cantidad_libras_esterlinas = float(input("Introduce la cantidad de libras esterlinas: "))
tasa_cambio = 1.16  # Tasa de cambio de libras a euros (puede variar)
cantidad_euros = cantidad_libras_esterlinas * tasa_cambio
print(f"{cantidad_libras_esterlinas} libras esterlinas equivalen a {cantidad_euros:.2f} euros.")