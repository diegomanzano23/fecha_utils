# Proyecto de Manipulación de Fechas

## 📌 Descripción
Este proyecto proporciona una serie de funciones en Python para realizar operaciones con fechas, como:
- **Calcular edades** a partir de una fecha de nacimiento.
- **Verificar si una fecha cae en fin de semana**.
- **Sumar días** a una fecha dada.
- **Calcular la diferencia en días** entre dos fechas.
- **Validar el formato de una fecha** antes de procesarla.

## 🏗 Estructura del Proyecto
📁 mi_proyecto
├── 📂 operaciones_fechas
│   ├── 📄 calcular_edad.py
│   ├── 📄 is_weekend.py
│   ├── 📄 day_between_dates.py
│   ├── 📄 sumar_dias.py
│   ├── 📄 date_true_or_false.py
├── 📂 tests
│   ├── 📄 test_operaciones.py
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 setup.py


datacleaner/
├── datacleaner/
|    └── __init__.py
|    └── cleaner.py
|    └── missing.py
|    └── types.py
|    └── constants.py
|    └── outliers.py
├── test/
|    └── pytest.ini
|    └── test_data_types.py
|    └── test_na_manager.py
├── scripts/
|    └── main.py
├── README.md
├── requirements.txt
└── setup.py
## 🚀 Instalación
Para instalar las dependencias necesarias, ejecuta el siguiente comando en tu terminal:

git clone https://github.com/diegomanzano23/fecha_utils.git
cd operaciones_fechas
pip install -r requirements.txt


## 🎮 Ejecución del Programa Principal
Para ejecutar el menú interactivo desde la terminal ubicate en la carpeta del archivo, usa:

python .\scripts\main.py


## ✅ Pruebas
Para ejecutar los tests unitarios y verificar que todo funciona correctamente, utiliza:
python -m unittest discover tests


## 💡 Contribuir
Si deseas contribuir al proyecto, sigue estos pasos:
- Haz un fork del repositorio.
- Crea una nueva rama con tu mejora (git checkout -b feature-nueva)
- Realiza los cambios y crea un commit (git commit -m 'Añadir nueva funcionalidad')
- Sube la rama al repositorio (git push origin feature-nueva)
- Abre un pull request para revisar los cambios.

📌 Autor: Diego Manzano
📅 Fecha de creación: Junio 2025
🔗 Licencia: MIT
