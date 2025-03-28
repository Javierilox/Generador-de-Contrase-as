# Generador de Contraseñas

## Descripción
Este proyecto de Python permite generar contraseñas aleatorias con una longitud especificada por el usuario y guardar dichas contraseñas junto con el correo electrónico del usuario en un archivo ZIP protegido con una clave. El archivo ZIP está cifrado utilizando el algoritmo AES-256 para garantizar la seguridad de la información.

## Requisitos
Para ejecutar este proyecto, necesitas tener instaladas las siguientes librerías de Python:
- `os`: Librería estándar de Python para interactuar con el sistema operativo.
- `random`: Librería estándar de Python para generar números y secuencias aleatorias.
- `string`: Librería estándar de Python para trabajar con cadenas de caracteres.
- `pyzipper`: Librería para crear y manipular archivos ZIP con cifrado AES.
- `getpass`: Librería estándar de Python para manejar la entrada de contraseñas de manera segura.

Puedes instalar `pyzipper` utilizando pip:
```sh
pip install pyzipper

## Instalación

Para instalar las dependencias necesarias, asegúrate de tener `pip` configurado en tu sistema. Luego, instala la librería `pyzipper` ejecutando el siguiente comando:

```sh
pip install pyzipper
```

## Funcionalidades

### 1. Generar una contraseña aleatoria
La función `generar_contrasena(longitud)` genera una contraseña aleatoria con la longitud especificada por el usuario. La contraseña incluye:
- Letras mayúsculas
- Letras minúsculas
- Dígitos
- Caracteres especiales

#### Ejemplo:
```python
from generador_contrasenas import generar_contrasena

longitud = 12
contrasena = generar_contrasena(longitud)
print(f"Contraseña generada: {contrasena}")
```

### 2. Guardar la contraseña y el correo en un archivo ZIP protegido con clave
La función `guardar_contrasena_en_zip(correo, contrasena, clave_zip)` guarda el correo electrónico y la contraseña generada en un archivo de texto, y luego comprime este archivo en un archivo ZIP protegido con una clave proporcionada por el usuario.

#### Ejemplo:
```python
from generador_contrasenas import guardar_contrasena_en_zip

correo = "usuario@example.com"
contrasena = "aB3$dEfGh1!2"
clave_zip = "mi_clave_segura"

guardar_contrasena_en_zip(correo, contrasena, clave_zip)
print("Archivo ZIP cifrado guardado en la carpeta Documents.")
```

### 3. Interfaz de usuario
El script solicita al usuario:
1. Su correo electrónico.
2. La longitud deseada para la contraseña.
3. Una clave para proteger el archivo ZIP.

#### Ejemplo de ejecución:
```sh
Ingrese el correo electrónico del usuario: usuario@example.com
Ingrese la longitud de la contraseña: 12
Contraseña generada para usuario@example.com: aB3$dEfGh1!2
Ingrese una clave para proteger el archivo ZIP: ******
Archivo ZIP cifrado guardado en: /home/usuario/Documents/credenciales_protegidas.zip
```

## Manejo de Errores

El script incluye manejo básico de errores para garantizar una experiencia de usuario fluida:
- **Correo electrónico inválido:** Se valida que el correo ingresado tenga un formato correcto.
- **Longitud de contraseña inválida:** Se asegura que la longitud sea un número positivo.
- **Errores inesperados:** Cualquier excepción durante la ejecución será capturada y mostrada al usuario con un mensaje claro.

#### Ejemplo:
```sh
Ingrese el correo electrónico del usuario: usuario
Error: El correo electrónico ingresado no es válido.
```
## Uso
Para ejecutar el script main.py, sigue estos pasos:

Clona este repositorio o descarga el archivo main.py.

Asegúrate de tener instaladas las librerías necesarias.

Ejecuta el script main.py

```sh
