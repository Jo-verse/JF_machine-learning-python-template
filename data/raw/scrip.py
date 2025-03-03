import os
import requests

# URL del dataset
url = "https://raw.githubusercontent.com/4GeeksAcademy/data-preprocessing-project-tutorial/main/AB_NYC_2019.csv"

# Ruta donde se guardará el archivo
file_path = os.path.join("data", "raw", "AB_NYC_2019.csv")

# Descargar el archivo y guardarlo
response = requests.get(url)

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)
    print(f"✅ Archivo guardado en {file_path}")
else:
    print("❌ Error al descargar el archivo")