import os
import random
import string
import pyzipper
from getpass import getpass

# Generar una contraseña aleatoria
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# Guardar la contraseña y correo en un archivo ZIP protegido con clave
def guardar_contrasena_en_zip(correo, contrasena, clave_zip):
    escritorio = os.path.join(os.path.expanduser("~"), "Documents")
    archivo_txt = os.path.join(escritorio, "credenciales.txt")
    archivo_zip = os.path.join(escritorio, "credenciales_protegidas.zip")

    # Guardar la información en un archivo de texto
    with open(archivo_txt, "w") as archivo:
        archivo.write(f"Correo: {correo}\n")
        archivo.write(f"Contraseña: {contrasena}\n")

    # Crear el ZIP con cifrado AES-256
    with pyzipper.AESZipFile(archivo_zip, "w", compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(clave_zip.encode())  # Convertir la clave en bytes
        zipf.write(archivo_txt, "credenciales.txt")

    # Eliminar el archivo de texto original
    os.remove(archivo_txt)

    print(f"Archivo ZIP cifrado guardado en: {archivo_zip}")

def main():
    try:
        while True:
            correo = input("Ingrese el correo electrónico del usuario: ").strip()
            if "@" in correo and "." in correo:
                break
            print("Por favor, ingrese un correo electrónico válido.")

        while True:
            try:
                longitud = int(input("Ingrese la longitud de la contraseña: "))
                if longitud > 0:
                    break
                print("La longitud debe ser un número positivo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        contrasena = generar_contrasena(longitud)
        print(f"Contraseña generada para {correo}: {contrasena}")

        clave_zip = getpass("Ingrese una clave para proteger el archivo ZIP: ")
        guardar_contrasena_en_zip(correo, contrasena, clave_zip)

        print("El archivo ZIP ha sido generado y está completamente cifrado.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()