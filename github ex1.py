velocidade = 10
velocidade_kmh = velocidade * 3.6 

semanas = 1 
segundos = semanas * 7 * 24 * 60 * 60

distancia_km = velocidade_kmh * (segundos / 3600)
print("A ave percorreu uma distância de", distancia_km, "quilômetros durante uma semana.")