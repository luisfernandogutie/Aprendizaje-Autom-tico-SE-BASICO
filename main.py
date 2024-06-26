# main.py

from recommendation import sistema_experto_recomendacion

if __name__ == "__main__":
    print("Sistema Experto de Recomendación de Películas")
    print("Por favor, ingrese sus preferencias de géneros de películas (1 para Sí, 0 para No):")
    accion = int(input("¿Le gusta la acción? (1/0): "))
    comedia = int(input("¿Le gusta la comedia? (1/0): "))
    drama = int(input("¿Le gusta el drama? (1/0): "))
    ciencia_ficcion = int(input("¿Le gusta la ciencia ficción? (1/0): "))
    
    recomendacion = sistema_experto_recomendacion(accion, comedia, drama, ciencia_ficcion)
    print(recomendacion)
