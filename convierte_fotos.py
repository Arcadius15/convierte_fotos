import os
from PIL import Image

def convert_images_to_jpg(folder_path):
    # Lista de extensiones de archivo que consideraremos como imágenes
    image_extensions = ('.png', '.jpeg', '.bmp', '.tiff', '.gif')

    # Recorremos todos los archivos en la carpeta especificada
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Verificamos si es un archivo y si tiene una extensión válida
        if os.path.isfile(file_path) and filename.lower().endswith(image_extensions):
            # Abrimos la imagen usando Pillow
            with Image.open(file_path) as img:
                # Si la imagen ya está en formato JPG, no hacemos nada
                if img.format == 'JPEG':
                    print(f"{filename} ya está en formato JPG.")
                else:
                    # Convertimos a JPG
                    rgb_im = img.convert('RGB')
                    # Guardamos con la extensión .jpg
                    new_filename = os.path.splitext(filename)[0] + '.jpg'
                    new_file_path = os.path.join(folder_path, new_filename)
                    rgb_im.save(new_file_path, 'JPEG')
                    print(f"Convertido {filename} a {new_filename}.")

# Uso del script
folder_path = '/ruta/a/tu/carpeta/de/imagenes'
convert_images_to_jpg(folder_path)
