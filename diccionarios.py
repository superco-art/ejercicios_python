#frutas = {"manzanas": 10, "bananas": 5}#inicializamos el diccionario con dos cajas de frutas
# frutas["bananas"] = 13 #actualizamos el número de bananas a 13
# frutas["naranjas"] = 7 #agregamos un nuevo tipo de fruta, una nueva caja que tiene como cantidad 7 naranjas
# total_frutas = sum(frutas.values()) #sumamos el total de frutas en todas las cajas usando el método values() para obtener los valores del diccionario
# print(frutas) #imprimimos el diccionario completo
# print(f"Hay {frutas['manzanas']} manzanas en la caja.")
# print(f"El total de frutas en todas las cajas es: {total_frutas}.")

# #Fusionar 2 diccionarios
# datos_basicos = {"nombre": "GamerX", "nivel": 15}
# datos_extra = {"puntos": 2500, "nivel": 16}
# datos_perfil = datos_basicos.copy() #creamos una copia del primer diccionario para no modificarlo
# datos_perfil.update(datos_extra) #fusionamos el segundo diccionario en la copia del primero, actualizando el nivel a 16
# print(datos_perfil) #imprimimos el diccionario fusionado, que contiene los datos combinados de ambos diccionarios

#Creamos la ficha tecnica de un influencer usando un diccionario
# campaña_verano = {
#     "cliente": "SuperSoda",
#     "presupuesto": 50000,
#     "redes": ["Instagram", "TikTok"],
#     "objetivo_kpi": "Aumentar seguidores",
#     "finalizada": False
# }
# #Pedimos los datos del cliente usando las claves del diccionario
# print(f"Campaña para el cliente: {campaña_verano['cliente']}")

# #Actualizamos el presupuesto de la campaña
# campaña_verano["presupuesto"] = 60000
# campaña_verano["responsable"] = "Sara"#Agregamos una nueva clave-valor al diccionario para indicar el responsable de la campaña
# print(f"Actualizacion de la campaña: {campaña_verano}")

# colores = {"red": "rojo", "blue": "azul", "green": "verde"}

# # 1. Iterar solo sobre las llaves
# print("Colores en inglés:")
# for eng in colores.keys():
#     print(f"- {eng}")

# # 2. Iterar sobre ítems (llave y valor a la vez)
# for eng, esp in colores.items():
#     print(f"The color {eng} in Spanish is {esp}")

palabra = "programacion"
contador = {}

for letra in palabra:
    # .get(letra, 0) busca la letra; si no la encuentra, devuelve 0
    contador[letra] = contador.get(letra, 0) + 1

print("Conteo de letras:")
print(contador)