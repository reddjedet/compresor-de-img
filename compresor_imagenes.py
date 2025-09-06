import os
from PIL import Image

def comprimir_imagen(ruta_origen, ruta_destino, calidad=85, tamano=(200, 200)):
    """
    Comprime y redimensiona una imagen.
    """
    try:
        with Image.open(ruta_origen) as img:
            img.thumbnail(tamano)
            nombre_archivo, extension = os.path.splitext(os.path.basename(ruta_origen))
            extension = extension.lower()

            if extension in ['.jpg', '.jpeg']:
                img.save(ruta_destino, format='JPEG', quality=calidad, optimize=True)
                print(f"✅ Comprimido JPG: {ruta_origen} -> {ruta_destino}")
            elif extension == '.png':
                img.save(ruta_destino, format='PNG', optimize=True)
                print(f"✅ Comprimido PNG: {ruta_origen} -> {ruta_destino}")
            else:
                print(f"❌ Formato no soportado: {ruta_origen}")

    except Exception as e:
        print(f"❌ Error al procesar {ruta_origen}: {e}")

# --- Configuración para comprimir UNA SOLA IMAGEN ---
if __name__ == "__main__":
    # La solución: Usar una raw string (r'...') para la ruta del archivo de origen
    RUTA_IMAGEN_ORIGINAL = r''
    
    # La solución: Usar una raw string (r'...') para la ruta de la carpeta de destino
    CARPETA_DESTINO = r''
    
    # El código verifica si la carpeta existe y la crea si es necesario.
    if not os.path.exists(CARPETA_DESTINO):
        os.makedirs(CARPETA_DESTINO)
        print(f"📂 Carpeta de destino creada: {CARPETA_DESTINO}")
        
    nombre_archivo = os.path.basename(RUTA_IMAGEN_ORIGINAL)
    RUTA_IMAGEN_COMPRIMIDA = os.path.join(CARPETA_DESTINO, nombre_archivo)

    CALIDAD_JPG = 80 
    TAMANO_AVATAR = (200, 200)

    print("🚀 Iniciando proceso de compresión de imagen individual...")
    comprimir_imagen(RUTA_IMAGEN_ORIGINAL, RUTA_IMAGEN_COMPRIMIDA, CALIDAD_JPG, TAMANO_AVATAR)
    print("\n🎉 Proceso de compresión finalizado.")
