# --- SCRIPT: Alta de Talento ---

nombre_influencer = "Luna" # String (Texto)
seguidores_instagram = 250500      # Int (Número entero)
precio_post_euro = 1500.50       # Float (Decimal)
es_premium = True                # Boolean (Verdad/Falso)

# Hagamos una operación automática: ¿Cuánto ganamos si le quitamos el 20% de comisión?
comision_agencia = precio_post_euro * 0.20
pago_final_influencer = precio_post_euro - comision_agencia

print(f"Influencer: {nombre_influencer}")
print(f"Precio por post: {precio_post_euro}€ | Comisión Agencia: {comision_agencia}€")
print(f"¿Es cuenta VIP?: {es_premium}")
