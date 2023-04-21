import os
# [START vision_text_detection]
def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_text_detection]
    with io.open(path, 'rb') as image_file: 
        content = image_file.read()
	
    image = vision.Image(content=content)
	
    response = client.text_detection(image=image)
    texts = response.text_annotations
	
    result = ""
	
    for text in texts: 
        #result+='\n"{}"'.format(text.description)
        result+=text.description+" "
        continue
		
    if response.error.message:
    	raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
	
    return result
    # [END vision_python_migration_text_detection]
# [END vision_text_detection]


print(">Iniciando script...")
dir_path = 'Induccion-Asesor'
#dir_path = 'ToOCR_SC2-6'
print(">Obteniendo fichero para escritura...")
f=open("txt/induccion-asesor13.txt","w",encoding="utf-8")
#f=open("txt/proposito.txt","w",encoding="utf-8")
print(">El fichero esta listo para su escritura")
print(">Obteniendo contenido del directorio IMG...")
contenido = os.listdir(dir_path)
print(">Listado de contenido de directorio listo")
print(">Iniciando ocr...")
print(">El ocr esta listo")
print(">Iniciando rutina de identificacion de texto...")
for fichero in contenido:
    if (fichero != ".DS_Store"):
        print('>Obteniendo el elemento: '+dir_path+ '/'+fichero)
        f.write(">----------Imagen: "+fichero+"----------<\n")
        texto = detect_text(dir_path+ '/'+fichero)
        f.write(texto+"\n")
    continue

print(">Termino rutina de identificacion de texto, cerrando archivo...")
f.close()
print(">Archivo cerrado, fin de script")