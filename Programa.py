import pandas as pd # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
import tkinter as tk
from tkinter import ttk, messagebox

# Funciones de amortización (como en el código anterior)

def sistema_frances(monto, tasa_interes, plazo):
    tasa_mensual = tasa_interes / 12 / 100
    cuota = monto * tasa_mensual / (1 - (1 + tasa_mensual) ** -plazo)
    saldo = monto
    pagos = []

    for i in range(1, plazo + 1):
        interes = saldo * tasa_mensual
        capital = cuota - interes
        saldo -= capital
        pagos.append([i, cuota, capital, interes, saldo])

    return pd.DataFrame(pagos, columns=["Mes", "Cuota", "Capital", "Interés", "Saldo"])

def sistema_aleman(monto, tasa_interes, plazo):
    saldo = monto
    amortizacion = monto / plazo
    tasa_mensual = tasa_interes / 12 / 100
    pagos = []

    for i in range(1, plazo + 1):
        interes = saldo * tasa_mensual
        cuota = amortizacion + interes
        saldo -= amortizacion
        pagos.append([i, cuota, amortizacion, interes, saldo])

    return pd.DataFrame(pagos, columns=["Mes", "Cuota", "Capital", "Interés", "Saldo"])

def sistema_ingles(monto, tasa_interes, plazo):
    tasa_mensual = tasa_interes / 12 / 100
    interes = monto * tasa_mensual
    pagos = []

    for i in range(1, plazo + 1):
        capital = monto if i == plazo else 0
        cuota = capital + interes
        saldo = 0 if i == plazo else monto
        pagos.append([i, cuota, capital, interes, saldo])

    return pd.DataFrame(pagos, columns=["Mes", "Cuota", "Capital", "Interés", "Saldo"])

def sistema_flat(monto, tasa_interes, plazo):
    interes = (monto * (tasa_interes / 100)) / plazo
    cuota = (monto / plazo) + interes
    saldo = monto
    pagos = []

    for i in range(1, plazo + 1):
        capital = monto / plazo
        saldo -= capital
        pagos.append([i, cuota, capital, interes, saldo])

    return pd.DataFrame(pagos, columns=["Mes", "Cuota", "Capital", "Interés", "Saldo"])

# Función para mostrar el gráfico de amortización
def mostrar_grafico(df, titulo):
    plt.plot(df['Mes'], df['Saldo'], label='Saldo')
    plt.plot(df['Mes'], df['Interés'], label='Interés')
    plt.xlabel('Mes')
    plt.ylabel('Monto')
    plt.title(f"{titulo} - Evolución del Saldo y los Intereses")
    plt.legend()
    plt.show()

# Función para calcular y mostrar resultados
def calcular():
    try:
        monto = float(entry_monto.get())
        tasa_interes = float(entry_tasa.get())
        plazo = int(entry_plazo.get())
        sistema = combo_sistema.get()
        
        if sistema == "Sistema Francés":
            df = sistema_frances(monto, tasa_interes, plazo)
            mostrar_grafico(df, sistema)
        elif sistema == "Sistema Alemán":
            df = sistema_aleman(monto, tasa_interes, plazo)
            mostrar_grafico(df, sistema)
        elif sistema == "Sistema Inglés":
            df = sistema_ingles(monto, tasa_interes, plazo)
            mostrar_grafico(df, sistema)
        elif sistema == "Sistema Flat":
            df = sistema_flat(monto, tasa_interes, plazo)
            mostrar_grafico(df, sistema)
        else:
            messagebox.showerror("Error", "Seleccione un sistema de amortización")
            return
        
        # Mostrar resultados en una nueva ventana
        resultados = tk.Toplevel()
        resultados.title("Resultados de Amortización")
        table = ttk.Treeview(resultados, columns=("Mes", "Cuota", "Capital", "Interés", "Saldo"), show="headings")
        table.heading("Mes", text="Mes")
        table.heading("Cuota", text="Cuota")
        table.heading("Capital", text="Capital")
        table.heading("Interés", text="Interés")
        table.heading("Saldo", text="Saldo")
        
        for _, row in df.iterrows():
            table.insert("", "end", values=list(row))
        
        table.pack(fill="both", expand=True)
    
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos")

# Función para comparar los sistemas de amortización
def comparar_sistemas():
    try:
        monto = float(entry_monto.get())
        tasa_interes = float(entry_tasa.get())
        plazo = int(entry_plazo.get())
        
        # Calcular el interés total, cuota inicial, cuota final y costo total para cada sistema
        def obtener_datos_comparacion(df):
            interes_total = df['Interés'].sum()
            cuota_inicial = df.iloc[0]['Cuota']
            cuota_final = df.iloc[-1]['Cuota']
            costo_total = df['Cuota'].sum()
            return interes_total, cuota_inicial, cuota_final, costo_total

        df_frances = sistema_frances(monto, tasa_interes, plazo)
        datos_frances = obtener_datos_comparacion(df_frances)

        df_aleman = sistema_aleman(monto, tasa_interes, plazo)
        datos_aleman = obtener_datos_comparacion(df_aleman)

        df_ingles = sistema_ingles(monto, tasa_interes, plazo)
        datos_ingles = obtener_datos_comparacion(df_ingles)

        df_flat = sistema_flat(monto, tasa_interes, plazo)
        datos_flat = obtener_datos_comparacion(df_flat)
        
        # Crear una ventana de resultados de comparación
        comparacion = tk.Toplevel()
        comparacion.title("Comparación de Sistemas de Amortización")
        
        # Formato de los resultados para cada sistema
        resultados_comparacion = f"""
        Comparación de Sistemas de Amortización:
        
        Sistema Francés:
          - Interés Total: {datos_frances[0]:.2f}
          - Cuota Inicial: {datos_frances[1]:.2f}
          - Cuota Final: {datos_frances[2]:.2f}
          - Costo Total Aproximado: {datos_frances[3]:.2f}
        
        Sistema Alemán:
          - Interés Total: {datos_aleman[0]:.2f}
          - Cuota Inicial: {datos_aleman[1]:.2f}
          - Cuota Final: {datos_aleman[2]:.2f}
          - Costo Total Aproximado: {datos_aleman[3]:.2f}
        
        Sistema Inglés:
          - Interés Total: {datos_ingles[0]:.2f}
          - Cuota Inicial: {datos_ingles[1]:.2f}
          - Cuota Final: {datos_ingles[2]:.2f}
          - Costo Total Aproximado: {datos_ingles[3]:.2f}
        
        Sistema Flat:
          - Interés Total: {datos_flat[0]:.2f}
          - Cuota Inicial: {datos_flat[1]:.2f}
          - Cuota Final: {datos_flat[2]:.2f}
          - Costo Total Aproximado: {datos_flat[3]:.2f}
        """
        
        # Mostrar resultados
        label_resultados = tk.Label(comparacion, text=resultados_comparacion, justify="left", font=("Arial", 12))
        label_resultados.pack(padx=10, pady=10)
    
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Análisis de Créditos - Sistemas de Amortización")

# Entrada de Monto del Préstamo
tk.Label(root, text="Monto del Préstamo:").grid(row=0, column=0, padx=10, pady=10)
entry_monto = tk.Entry(root)
entry_monto.grid(row=0, column=1, padx=10, pady=10)

# Entrada de Tasa de Interés Anual
tk.Label(root, text="Tasa de Interés Anual (%):").grid(row=1, column=0, padx=10, pady=10)
entry_tasa = tk.Entry(root)
entry_tasa.grid(row=1, column=1, padx=10, pady=10)

# Entrada del Plazo en Meses
tk.Label(root, text="Plazo (meses):").grid(row=2, column=0, padx=10, pady=10)
entry_plazo = tk.Entry(root)
entry_plazo.grid(row=2, column=1, padx=10, pady=10)

# Selección del Sistema de Amortización
tk.Label(root, text="Sistema de Amortización:").grid(row=3, column=0, padx=10, pady=10)
combo_sistema = ttk.Combobox(root, values=["Sistema Francés", "Sistema Alemán", "Sistema Inglés", "Sistema Flat"])
combo_sistema.grid(row=3, column=1, padx=10, pady=10)

# Botón para Calcular
btn_calcular = tk.Button(root, text="Calcular", command=calcular)
btn_calcular.grid(row=4, column=0, columnspan=2, pady=10)

# Botón para Comparar Sistemas
btn_comparar = tk.Button(root, text="Comparar Sistemas", command=comparar_sistemas)
btn_comparar.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
