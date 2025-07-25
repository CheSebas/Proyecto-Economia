# 📊 Simulador de Créditos - Sistemas de Amortización

Esta aplicación de escritorio desarrollada en Python permite simular y comparar diferentes sistemas de amortización de préstamos: **Francés, Alemán, Inglés y Flat**. La herramienta genera tablas de amortización y gráficos para visualizar la evolución de los intereses y saldos.

## 🧰 Tecnologías Utilizadas

- Python 3.7+
- Tkinter (GUI)
- Pandas
- Matplotlib

## 🚀 Características

- Simula el comportamiento de préstamos bajo diferentes sistemas de amortización.
- Visualiza el saldo e intereses en gráficos.
- Compara el interés total, cuota inicial/final y costo total.
- Interfaz intuitiva y fácil de usar.

---

## 🖥️ Requisitos Previos

Antes de ejecutar la aplicación, asegúrate de tener instalado:

- Python 3.7 o superior: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- pip (gestor de paquetes de Python)

---

## 📦 Instalación

1. **Clona este repositorio** o descarga el archivo `.py`:
```bash
git clone https://github.com/tu-usuario/simulador-creditos.git
cd simulador-creditos
```
2. **Crea un entorno virtual (opcional pero recomendado):
```bash
python -m venv env
source env/bin/activate    # En Linux/Mac
env\Scripts\activate       # En Windows
```
3. **Instala las dependencias necesarias:
```bash
pip install pandas matplotlib
```

---

## ▶️ Ejecución

1. **Asegúrate de estar en el mismo directorio donde está el archivo `.py`:
2. **Ejecuta la aplicación:
```bash
Programa.py
```

---

## 📚 Cómo Usar

1. **Ingresa el monto del préstamo, tasa de interés anual (%), y el plazo en meses.
2. **Selecciona un sistema de amortización.
3. **Haz clic en Calcular para ver:
```bash
- Tabla de amortización.
- Gráfico de saldo e intereses.
```
4. **O haz clic en Comparar Sistemas para ver una comparación entre los cuatro métodos.

## 📝 Notas
```bash
- El interés es compuesto mensual, calculado según el sistema de amortización elegido.
- Los resultados son estimativos y no contemplan impuestos, comisiones u otros costos adicionales.
```
