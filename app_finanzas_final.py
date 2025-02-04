import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Configuración de la Página ---
st.set_page_config(page_title="Análisis Financiero", page_icon="📈", layout="wide")

# --- Estilo Personalizado ---
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .main {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    h1, h2, h3, h4 {
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #007BFF;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        margin-bottom: 10px;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .stTextInput, .stNumberInput {
        border-radius: 5px;
        padding: 8px;
        border: 1px solid #ddd;
        margin-bottom: 10px;
    }
        table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 20px;
        background-color: #fff;
    }
    table, th, td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
    }
    th {
        background-color: #f2f2f2;
        font-weight: bold;
    }
    .big-number {
        font-size: 1.7em; /* Ajusta el tamaño de la fuente según lo desees */
        font-weight: bold;
        color: #333; /* Puedes ajustar el color si lo necesitas */
        text-align: center;
    }
      .percentage {
        font-size: 1.5em; /* Ajusta el tamaño de la fuente según lo desees */
        font-weight: bold;
        color: #28a745; /* Puedes ajustar el color si lo necesitas */
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Funciones de Cálculo ---
def dif(a, b, c):
    return a - b - c

def calcular_aumento_trimestral(valor_inicial, porcentaje_aumento):
    return valor_inicial * (1 + porcentaje_aumento)

def inicializar_data():
    data = {
    'Año': [],
    'Trimestre': [],
    'Caja_Banco': [],
    'Creditos_Corrientes': [],
    'Inversiones': [],
    'Existencias': [],
    'Bienes_de_uso': [],
    'Total_Activo': [],
    'Deudores_por_Ventas':[],
        'Deudas_comerciales': [],
    'Deudas_finacieras': [],
    'Deudas_Sociales': [],
    'Deudas_Fiscales': [],
    'Otras_deudas': [],
    'Pasivo_corto_plazo': [],
    'Pasivo_largo_Plazo': [],
    'Total_Pasivo': [],
        'Capital': [],
        'Reservas': [],
        'Resultados_No_Asignados': [],
        'Otros_Recursos': [],
        'Recursos_Propios': [],
            'ventas':[],
    'Costos_de_Producción_Variables':[],
    'Variación_de_existencias':[],
    'Gastos_Variables':[],
    'Costos_fijos_de_produccion':[],
    'Gastos_administrativos':[],
    'Gastos_financieros':[],
    'Otros_ingresos_y_egresos':[],
    'Resultados_Extraordinarios':[],
    'Impuesto_a_las_Ganancias':[],
    'Total_ventas':[],
    'Total_Consumos_Variables':[],
    'Total_Costos_fijos':[],
    'Total_Otros_Gastos':[],
    'Total_Resultados_Extraordinarios':[],
    'Margen_Bruto':[],
    'Utilidad_Bruta':[],
    'Utilidad_Operacional':[],
    'Utilidad_Neta':[]
    }
    return data

def cargar_datos_activo():
    st.header(f"Carga de Activo del Trimestre 1")

    with st.expander("Caja y Bancos", expanded=True):
        Caja = st.number_input('Caja:', value=0.0, step=0.01, key="caja_input")
        Bancos = st.number_input('Bancos:', value=0.0, step=0.01, key="bancos_input")
        Caja_Banco = Caja + Bancos
        st.write(f'Caja y Bancos: {Caja_Banco}')

    with st.expander("Créditos corrientes", expanded=True):
        Deudores_por_Ventas = st.number_input('Deudores por Ventas:', value=0.0, step=0.01, key="deudores_ventas_input")
        Creditos_Fiscales = st.number_input('Créditos Fiscales:', value=0.0, step=0.01, key="creditos_fiscales_input")
        Otros_realizados = st.number_input('Otros realizados:', value=0.0, step=0.01, key="otros_realizados_input")
        Creditos_Corrientes = Deudores_por_Ventas + Creditos_Fiscales + Otros_realizados
        st.write(f'Créditos Corrientes: {Creditos_Corrientes}')

    with st.expander("Inversiones", expanded=True):
        Inversiones = st.number_input('Inversiones:', value=0.0, step=0.01, key="inversiones_input")
        st.write(f'Inversiones: {Inversiones}')

    with st.expander("Existencias", expanded=True):
        Existencias = st.number_input('Existencias:', value=0.0, step=0.01, key="existencias_input")
        st.write(f'Existencias: {Existencias}')

    with st.expander("Inmovilizado", expanded=True):
        Bienes_de_uso = st.number_input('Bienes de uso:', value=0.0, step=0.01, key="bienes_uso_input")
        st.write(f'Bienes de uso: {Bienes_de_uso}')

    Total_Activo = Caja_Banco + Creditos_Corrientes + Existencias + Bienes_de_uso + Inversiones
    st.write(f'Total Activo Trimestre 1: {Total_Activo}')
    
    if st.button("Guardar Activo",key="guardar_activo_button"):
        st.session_state.activo_cargado = True
        st.session_state.activo_data = {
            'Caja_Banco': Caja_Banco,
            'Creditos_Corrientes': Creditos_Corrientes,
            'Inversiones': Inversiones,
            'Existencias': Existencias,
            'Bienes_de_uso': Bienes_de_uso,
            'Total_Activo': Total_Activo,
            'Deudores_por_Ventas': Deudores_por_Ventas
        }
    
def cargar_datos_pasivo():
    st.header(f'Carga de Pasivo del Trimestre 1')

    with st.expander("Pasivo a Corto Plazo", expanded=True):
        Deudas_comerciales=st.number_input("Deudas Comerciales:", value=0.0, step=0.01, key="deudas_comerciales_input")
        Deudas_finacieras=st.number_input("Dedudas Financieras:", value=0.0, step=0.01, key="deudas_financieras_input")
        Deudas_Sociales=st.number_input("Deudas Sociales:", value=0.0, step=0.01, key="deudas_sociales_input")
        Deudas_Fiscales=st.number_input("Deudas Fiscales:", value=0.0, step=0.01, key="deudas_fiscales_input")
        Otras_deudas=st.number_input("Otras Deudas:", value=0.0, step=0.01, key="otras_deudas_input")
        Pasivo_corto_plazo=sum([Deudas_comerciales,Deudas_finacieras,Deudas_Sociales,Deudas_Fiscales,Otras_deudas])
        st.write(f'Pasivo a Corto Plazo: {Pasivo_corto_plazo}')

    with st.expander("Pasivo a Largo Plazo", expanded=True):
        Pasivo_largo_Plazo=st.number_input("Pasivo Largo Plazo:", value=0.0, step=0.01, key="pasivo_largo_plazo_input")
        st.write(f'Pasivo a Largo Plazo: {Pasivo_largo_Plazo}')

    Total_Pasivo=Pasivo_corto_plazo+Pasivo_largo_Plazo
    st.write(f'Total Pasivo Trimestre 1: {Total_Pasivo}')

    if st.button("Guardar Pasivo", key="guardar_pasivo_button"):
        st.session_state.pasivo_cargado = True
        st.session_state.pasivo_data = {
            'Deudas_comerciales': Deudas_comerciales,
            'Deudas_finacieras': Deudas_finacieras,
            'Deudas_Sociales': Deudas_Sociales,
            'Deudas_Fiscales': Deudas_Fiscales,
            'Otras_deudas': Otras_deudas,
            'Pasivo_corto_plazo': Pasivo_corto_plazo,
            'Pasivo_largo_Plazo': Pasivo_largo_Plazo,
            'Total_Pasivo': Total_Pasivo
        }
    

def cargar_datos_patrimonio_neto():
    st.header(f'Carga del Patrimonio Neto Trimestre 1')

    with st.expander("Recursos Propios", expanded=True):
        Capital=st.number_input("Capital:", value=0.0, step=0.01, key="capital_input")
        Reservas=st.number_input("Reservas:", value=0.0, step=0.01, key="reservas_input")
        Resultados_No_Asignados=st.number_input("Resultados No Asignados:", value=0.0, step=0.01, key="resultados_no_asignados_input")
        Otros_Recursos=st.number_input("Otros Recursos:", value=0.0, step=0.01, key="otros_recursos_input")
        Recursos_Propios=sum([Capital,Reservas,Resultados_No_Asignados,Otros_Recursos])
        st.write(f'Recursos Propios: {Recursos_Propios}')
    
    if st.button("Guardar Patrimonio Neto", key="guardar_patrimonio_button"):
         st.session_state.patrimonio_cargado = True
         st.session_state.patrimonio_data = {
            'Capital': Capital,
            'Reservas': Reservas,
            'Resultados_No_Asignados': Resultados_No_Asignados,
            'Otros_Recursos': Otros_Recursos,
            'Recursos_Propios': Recursos_Propios
         }
    
def cargar_datos_resultados():
    st.header(f'Carga de Cuentas de Resultados Trimestre 1')

    with st.expander("Ventas", expanded=True):
        ventas=st.number_input("Ventas:", value=0.0, step=0.01, key="ventas_input")
        Total_ventas=sum([ventas])
        st.write(f'Total ventas: {Total_ventas}')

    with st.expander("Consumos Variables", expanded=True):
        Costos_de_Producción_Variables=st.number_input("Costos de Producción Variables:", value=0.0, step=0.01, key="costos_produccion_variables_input")
        Variación_de_existencias=st.number_input("Variación de existencias:", value=0.0, step=0.01, key="variacion_existencias_input")
        Total_Consumos_Variables=sum([Costos_de_Producción_Variables,Variación_de_existencias])
        st.write(f'Total Consumos Variables: {Total_Consumos_Variables}')

    with st.expander("Gastos Variables", expanded=True):
        Gastos_Variables=st.number_input("Gastos Variables:", value=0.0, step=0.01, key="gastos_variables_input")
        Total_Gastos_Variables=sum([Gastos_Variables])
        st.write(f'Total Gastos Variables: {Total_Gastos_Variables}')

    Margen_Bruto=dif(Total_ventas,Total_Consumos_Variables, Gastos_Variables)
    st.write(f'Margen Bruto: {Margen_Bruto}')

    with st.expander("Costos Fijos de Producción", expanded=True):
        Costos_fijos_de_produccion=st.number_input("Costos Fijos de Producción:", value=0.0, step=0.01, key="costos_fijos_produccion_input")
        Gastos_administrativos=st.number_input("Gastos Administrativos:", value=0.0, step=0.01, key="gastos_administrativos_input")
        Total_Costos_fijos=sum([Costos_fijos_de_produccion,Gastos_administrativos])
        st.write(f'Total Costos Fijos: {Total_Costos_fijos}')

    Utilidad_Bruta=dif(Margen_Bruto,Total_Costos_fijos,0)
    st.write(f'Utilidad Bruta: {Utilidad_Bruta}')

    with st.expander("Otros Gastos", expanded=True):
        Gastos_financieros=st.number_input("Gastos Financieros:", value=0.0, step=0.01, key="gastos_financieros_input")
        Otros_ingresos_y_egresos=st.number_input("Otros Ingresos y Egresos:", value=0.0, step=0.01, key="otros_ingresos_egresos_input")
        Total_Otros_Gastos=sum([Gastos_financieros,Otros_ingresos_y_egresos])
        st.write(f'Total Otros Gastos: {Total_Otros_Gastos}')

    Utilidad_Operacional=dif(Utilidad_Bruta,Gastos_financieros,-Otros_ingresos_y_egresos)
    st.write(f'Utilidad Operacional: {Utilidad_Operacional}')

    with st.expander("Resultados Extraordinarios e Impuesto", expanded=True):
        Resultados_Extraordinarios=st.number_input("Resultados Extraordinarios:", value=0.0, step=0.01, key="resultados_extraordinarios_input")
        Impuesto_a_las_Ganancias=st.number_input("Impuesto a las Ganancias:", value=0.0, step=0.01, key="impuesto_ganancias_input")
        Total_Resultados_Extraordinarios=sum([Resultados_Extraordinarios,Impuesto_a_las_Ganancias])
        st.write(f'Total Resultados Extraordinarios e Impuesto: {Total_Resultados_Extraordinarios}')

    Utilidad_Neta=dif(Utilidad_Operacional,Total_Resultados_Extraordinarios,0)
    st.write(f'Utilidad Neta: {Utilidad_Neta}')
    
   
    if st.button("Guardar Resultados", key="guardar_resultados_button"):
        st.session_state.resultados_cargado = True
        st.session_state.resultados_data = {
            'ventas': ventas,
            'Costos_de_Producción_Variables': Costos_de_Producción_Variables,
            'Variación_de_existencias': Variación_de_existencias,
            'Gastos_Variables': Gastos_Variables,
            'Costos_fijos_de_produccion': Costos_fijos_de_produccion,
            'Gastos_administrativos': Gastos_administrativos,
            'Gastos_financieros': Gastos_financieros,
            'Otros_ingresos_y_egresos': Otros_ingresos_y_egresos,
            'Resultados_Extraordinarios': Resultados_Extraordinarios,
            'Impuesto_a_las_Ganancias': Impuesto_a_las_Ganancias,
            'Total_ventas': Total_ventas,
            'Total_Consumos_Variables': Total_Consumos_Variables,
            'Total_Costos_fijos': Total_Costos_fijos,
            'Total_Otros_Gastos': Total_Otros_Gastos,
            'Total_Resultados_Extraordinarios': Total_Resultados_Extraordinarios,
            'Margen_Bruto': Margen_Bruto,
            'Utilidad_Bruta': Utilidad_Bruta,
            'Utilidad_Operacional': Utilidad_Operacional,
            'Utilidad_Neta': Utilidad_Neta
        }
    
def calcular_datos_trimestrales(data, porcentaje_aumentos, inversiones):
    for trimestre in range(2, 5):
        
        data['Trimestre'].append(trimestre)
        data['Año'].append(2023)

        # Calcular aumentos basados en los porcentajes y la inversión para cada trimestre
        
        data['Caja_Banco'].append(calcular_aumento_trimestral(data['Caja_Banco'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Creditos_Corrientes'].append(calcular_aumento_trimestral(data['Creditos_Corrientes'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Inversiones'].append(inversiones[trimestre - 2])
        data['Existencias'].append(calcular_aumento_trimestral(data['Existencias'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Bienes_de_uso'].append(calcular_aumento_trimestral(data['Bienes_de_uso'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Total_Activo'].append(data['Caja_Banco'][-1]+data['Creditos_Corrientes'][-1]+data['Inversiones'][-1]+data['Existencias'][-1]+data['Bienes_de_uso'][-1])
        data['Deudores_por_Ventas'].append(calcular_aumento_trimestral(data['Deudores_por_Ventas'][-1], porcentaje_aumentos[trimestre - 2]))
        
        data['Deudas_comerciales'].append(calcular_aumento_trimestral(data['Deudas_comerciales'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Deudas_finacieras'].append(calcular_aumento_trimestral(data['Deudas_finacieras'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Deudas_Sociales'].append(calcular_aumento_trimestral(data['Deudas_Sociales'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Deudas_Fiscales'].append(calcular_aumento_trimestral(data['Deudas_Fiscales'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Otras_deudas'].append(calcular_aumento_trimestral(data['Otras_deudas'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Pasivo_corto_plazo'].append(data['Deudas_comerciales'][-1]+data['Deudas_finacieras'][-1]+data['Deudas_Sociales'][-1]+data['Deudas_Fiscales'][-1]+data['Otras_deudas'][-1])
        data['Pasivo_largo_Plazo'].append(calcular_aumento_trimestral(data['Pasivo_largo_Plazo'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Total_Pasivo'].append(data['Pasivo_corto_plazo'][-1]+data['Pasivo_largo_Plazo'][-1])
        
        data['Capital'].append(calcular_aumento_trimestral(data['Capital'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Reservas'].append(calcular_aumento_trimestral(data['Reservas'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Resultados_No_Asignados'].append(calcular_aumento_trimestral(data['Resultados_No_Asignados'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Otros_Recursos'].append(calcular_aumento_trimestral(data['Otros_Recursos'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Recursos_Propios'].append(data['Capital'][-1]+data['Reservas'][-1]+data['Resultados_No_Asignados'][-1]+data['Otros_Recursos'][-1])
        
        
        data['ventas'].append(calcular_aumento_trimestral(data['ventas'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Costos_de_Producción_Variables'].append(calcular_aumento_trimestral(data['Costos_de_Producción_Variables'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Variación_de_existencias'].append(calcular_aumento_trimestral(data['Variación_de_existencias'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Gastos_Variables'].append(calcular_aumento_trimestral(data['Gastos_Variables'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Costos_fijos_de_produccion'].append(calcular_aumento_trimestral(data['Costos_fijos_de_produccion'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Gastos_administrativos'].append(calcular_aumento_trimestral(data['Gastos_administrativos'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Gastos_financieros'].append(calcular_aumento_trimestral(data['Gastos_financieros'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Otros_ingresos_y_egresos'].append(calcular_aumento_trimestral(data['Otros_ingresos_y_egresos'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Resultados_Extraordinarios'].append(calcular_aumento_trimestral(data['Resultados_Extraordinarios'][-1], porcentaje_aumentos[trimestre - 2]))
        data['Impuesto_a_las_Ganancias'].append(data['Impuesto_a_las_Ganancias'][-1])
        
        # Calcula los totales
        Total_ventas = data['ventas'][-1]
        Total_Consumos_Variables = data['Costos_de_Producción_Variables'][-1] + data['Variación_de_existencias'][-1]
        Total_Costos_fijos = data['Costos_fijos_de_produccion'][-1] + data['Gastos_administrativos'][-1]
        Total_Otros_Gastos = data['Gastos_financieros'][-1] + data['Otros_ingresos_y_egresos'][-1]
        Total_Resultados_Extraordinarios = data['Resultados_Extraordinarios'][-1] + data['Impuesto_a_las_Ganancias'][-1]
        
        Margen_Bruto=dif(Total_ventas,Total_Consumos_Variables, data['Gastos_Variables'][-1])
        Utilidad_Bruta=dif(Margen_Bruto,Total_Costos_fijos,0)
        Utilidad_Operacional=dif(Utilidad_Bruta,data['Gastos_financieros'][-1],-data['Otros_ingresos_y_egresos'][-1])
        Utilidad_Neta=dif(Utilidad_Operacional,Total_Resultados_Extraordinarios,0)
        
        data['Total_ventas'].append(Total_ventas)
        data['Total_Consumos_Variables'].append(Total_Consumos_Variables)
        data['Total_Costos_fijos'].append(Total_Costos_fijos)
        data['Total_Otros_Gastos'].append(Total_Otros_Gastos)
        data['Total_Resultados_Extraordinarios'].append(Total_Resultados_Extraordinarios)
        data['Margen_Bruto'].append(Margen_Bruto)
        data['Utilidad_Bruta'].append(Utilidad_Bruta)
        data['Utilidad_Operacional'].append(Utilidad_Operacional)
        data['Utilidad_Neta'].append(Utilidad_Neta)
        
    return data    
        


def crear_dataframes(data):
    df_activo = pd.DataFrame(data)[['Año', 'Trimestre', 'Caja_Banco', 'Creditos_Corrientes', 'Inversiones', 'Existencias', 'Bienes_de_uso','Total_Activo','Deudores_por_Ventas']].set_index(['Año', 'Trimestre'])
    df_pasivo = pd.DataFrame(data)[['Año', 'Trimestre', 'Deudas_comerciales', 'Deudas_finacieras', 'Deudas_Sociales', 'Deudas_Fiscales', 'Otras_deudas', 'Pasivo_corto_plazo', 'Pasivo_largo_Plazo', 'Total_Pasivo']].set_index(['Año', 'Trimestre'])
    df_patrimonio_neto = pd.DataFrame(data)[['Año', 'Trimestre', 'Capital', 'Reservas', 'Resultados_No_Asignados', 'Otros_Recursos', 'Recursos_Propios']].set_index(['Año', 'Trimestre'])
    df_resultados = pd.DataFrame(data)[['Año','Trimestre', 'ventas', 'Costos_de_Producción_Variables', 'Variación_de_existencias', 'Gastos_Variables', 'Costos_fijos_de_produccion', 'Gastos_administrativos', 'Gastos_financieros', 'Otros_ingresos_y_egresos', 'Resultados_Extraordinarios', 'Impuesto_a_las_Ganancias','Total_ventas', 'Total_Consumos_Variables', 'Total_Costos_fijos', 'Total_Otros_Gastos', 'Total_Resultados_Extraordinarios','Margen_Bruto','Utilidad_Bruta', 'Utilidad_Operacional', 'Utilidad_Neta']].set_index(['Año', 'Trimestre'])
    df_final= pd.concat([df_activo,df_pasivo,df_patrimonio_neto,df_resultados], axis=1)
    return df_final, df_activo, df_patrimonio_neto

def ratios_patrimoniales(df_final, df_activo):
    ratios_df = pd.DataFrame(
        index=range(1, 5),
        columns=['Índice de prueba ácida', 'Índice de liquidez', 'Índice de autofinanciación',
                 'Nivel de endeudamiento', 'Índice de inmovilización', 'Existencias en días de compra',
                 'Días de cobro a clientes']
    )
    # Calcular ratios para cada trimestre
    for trimestre in range(1, 5):
        Caja_Banco = df_final.loc[(2023, trimestre), 'Caja_Banco']
        Creditos_Corrientes = df_final.loc[(2023, trimestre), 'Creditos_Corrientes']
        Deudores_por_Ventas = df_activo.loc[(2023, trimestre), 'Deudores_por_Ventas']
        Inversiones = df_final.loc[(2023, trimestre), 'Inversiones']
        Existencias = df_final.loc[(2023, trimestre), 'Existencias']
        Bienes_de_uso = df_final.loc[(2023, trimestre), 'Bienes_de_uso']
        Pasivo_corto_plazo = df_final.loc[(2023, trimestre), 'Pasivo_corto_plazo']
        Recursos_Propios = df_final.loc[(2023, trimestre), 'Recursos_Propios']
        Total_Activo = df_final.loc[(2023, trimestre), 'Total_Activo']
        Total_Pasivo = df_final.loc[(2023, trimestre), 'Total_Pasivo']
        Costos_de_Producción_Variables = df_final.loc[(2023, trimestre), 'Total_Consumos_Variables']
        ventas = df_final.loc[(2023, trimestre), 'ventas']
        
        indice_prueba_acida = (Caja_Banco + Creditos_Corrientes) / Pasivo_corto_plazo
        indice_liquidez = (Caja_Banco + Creditos_Corrientes + Existencias+Inversiones) / Pasivo_corto_plazo
        indice_autofinanciacion = Recursos_Propios / Total_Activo
        nivel_endeudamiento = Total_Pasivo / Recursos_Propios
        indice_inmovilizacion = Bienes_de_uso / Recursos_Propios
        existencias_dias_compra = (Existencias / Costos_de_Producción_Variables) * 365
        dias_cobro_clientes = (Deudores_por_Ventas/ventas)*365
        
        ratios_df.loc[trimestre] = [
            indice_prueba_acida, indice_liquidez, indice_autofinanciacion, nivel_endeudamiento,
            indice_inmovilizacion, existencias_dias_compra, dias_cobro_clientes
        ]
    return ratios_df
        
def plot_ratios(ratios_df):
    ratios_to_plot = {
        'Liquidez y Autofinanciación': ['Índice de prueba ácida', 'Índice de liquidez', 'Índice de autofinanciación'],
        'Nivel de Enduedamiento': ['Nivel de endeudamiento', 'Índice de inmovilización'],
        'Gestión en Días': ['Existencias en días de compra', 'Días de cobro a clientes']
    }

    for group_name, ratios in ratios_to_plot.items():
        # Get the data for the current group of ratios
        group_data = ratios_df[ratios]

        # Iterate through each quarter to create separate bars for each quarter
        for quarter in group_data.index:  # Iterate using index values (1, 2, 3, 4)
            fig, ax = plt.subplots(figsize=(10, 6))
            # Bar plot
            X_axis = ratios
            Y_axis = group_data.loc[quarter].values

            ax.bar(X_axis, Y_axis, color=['skyblue', 'lightcoral', 'lightgreen', 'orange', 'violet'])
            ax.set_xlabel("Ratios", fontsize=12)
            ax.set_ylabel("Valor", fontsize=12)
            ax.set_title(f"Ratios - {group_name} (Gráfico de Barras) - Trimestre {quarter}", fontsize=16)
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            st.pyplot(fig)
           
            # Pie chart
            fig1, ax1 = plt.subplots(figsize=(8, 8))
            ax1.pie(Y_axis, labels=X_axis, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightcoral', 'lightgreen', 'orange', 'violet'])
            ax1.set_title(f"Ratios - {group_name} (Gráfico Circular) - Trimestre {quarter}", fontsize=16)
            ax1.axis('equal')
            st.pyplot(fig1)
            
            
def ratios_financieros(df_final, df_activo, df_patrimonio_neto):
    ratios_financieros_df = pd.DataFrame(
        index=range(1, 5),
        columns=['ROIC', 'ROIC_despues_impuestos', 'Tiempo_cobro_ventas',
                 'Tiempo_pago_proveedores','Rentabilidad_neta_activo','ROI',
                 'Punto_equilibrio']
    )
    # Calcular ratios para cada trimestre
    for trimestre in range(1, 5):
        Utilidad_Operacional = df_final.loc[(2023, trimestre), 'Utilidad_Operacional']
        Recursos_Propios = df_final.loc[(2023, trimestre), 'Recursos_Propios']
        Creditos_Corrientes = df_final.loc[(2023, trimestre), 'Creditos_Corrientes']
        Deudores_por_Ventas = df_activo.loc[(2023, trimestre), 'Deudores_por_Ventas']
        Utilidad_Neta = df_final.loc[(2023, trimestre), 'Utilidad_Neta']
        Impuesto_a_las_Ganancias = df_final.loc[(2023, trimestre), 'Impuesto_a_las_Ganancias']
        Gastos_financieros = df_final.loc[(2023, trimestre), 'Gastos_financieros']
        Deudas_comerciales = df_final.loc[(2023, trimestre), 'Deudas_comerciales']
        Total_Activo = df_final.loc[(2023, trimestre), 'Total_Activo']
        Capital = df_final.loc[(2023, trimestre), 'Capital']
        Pasivo_largo_Plazo = df_final.loc[(2023, trimestre), 'Pasivo_largo_Plazo']
        ventas = df_final.loc[(2023, trimestre), 'ventas']
        Deudas_comerciales = df_final.loc[(2023, trimestre), 'Deudas_comerciales']
        Costos_de_Producción_Variables = df_final.loc[(2023, trimestre), 'Total_Consumos_Variables']
        Total_Costos_fijos = df_final.loc[(2023, trimestre), 'Total_Costos_fijos']
        Margen_Bruto = df_final.loc[(2023, trimestre), 'Margen_Bruto']
    
        ROIC = (Utilidad_Operacional / Recursos_Propios)
        ROIC_despues_impuestos = (Utilidad_Neta / Recursos_Propios)
        Tiempo_cobro_ventas = (Deudores_por_Ventas * 120) / ventas
        Tiempo_pago_proveedores = (Deudas_comerciales * 120) / Costos_de_Producción_Variables
        Rentabilidad_neta_activo = (Utilidad_Neta) / Total_Activo       
        
        ROI = ((Utilidad_Neta+ Impuesto_a_las_Ganancias) / Total_Activo)/100
        Punto_equilibrio = ((Gastos_financieros+Total_Costos_fijos+Impuesto_a_las_Ganancias) / (Margen_Bruto/ventas) )/1000
    
        ratios_financieros_df.loc[trimestre] = [
            ROIC, ROIC_despues_impuestos, Tiempo_cobro_ventas, Tiempo_pago_proveedores,
            Rentabilidad_neta_activo, ROI, Punto_equilibrio
        ]
    return ratios_financieros_df
    
def ratios_economicos(df_final, df_activo, df_patrimonio_neto):
    ratios_economicos_df = pd.DataFrame(
        index=range(1, 5),
        columns=['Margen_de_Utilidad_Bruta', 'Margen_Operativo', 'Margen_Neto',
                 'Margen_sobre_ventas', 'Punto_de_Equilibrio_Económico',
                 'Margen_de_seguridad_Económico']
    )
    # Calcular ratios para cada trimestre
    for trimestre in range(1, 5):
        Utilidad_Bruta = df_final.loc[(2023, trimestre), 'Utilidad_Bruta']
        Margen_Bruto = df_final.loc[(2023, trimestre), 'Margen_Bruto']
        Utilidad_Neta=df_final.loc[(2023, trimestre), 'Utilidad_Neta']
        ventas = df_final.loc[(2023, trimestre), 'ventas']
        Total_Consumos_Variables = df_final.loc[(2023, trimestre), 'Total_Consumos_Variables']
        Total_Costos_fijos = df_final.loc[(2023, trimestre), 'Total_Costos_fijos']
        Gastos_financieros = df_final.loc[(2023, trimestre), 'Gastos_financieros']

        Margen_de_Utilidad_Bruta=Margen_Bruto/ventas
        Margen_Operativo = Utilidad_Bruta / ventas
        Margen_Neto = Utilidad_Neta  / ventas
        Margen_sobre_ventas = (ventas - Total_Consumos_Variables) / ventas
        Punto_de_Equilibrio_Económico = (
           (Gastos_financieros + Total_Costos_fijos) / (Margen_Bruto / ventas)
            ) / 1000
                
                
        Margen_de_seguridad_Económico = (ventas - Punto_de_Equilibrio_Económico*1000) /ventas


        ratios_economicos_df.loc[trimestre] = [
            Margen_de_Utilidad_Bruta, Margen_Operativo, Margen_Neto, Margen_sobre_ventas,
            Punto_de_Equilibrio_Económico, Margen_de_seguridad_Económico
        ]
    return ratios_economicos_df


# --- Sidebar para Navegación ---
st.sidebar.title("Navegación")
page = st.sidebar.radio("Ir a", ["Bienvenida", "Carga de Datos", "Ratio Patrimonial","Gráfico Ampliado Patrimonial", "Ratios Financieros", "Ratios Económicos"])

# --- Inicialización de la Sesión ---
if 'data' not in st.session_state:
    st.session_state.data = inicializar_data()
if 'datos_cargados' not in st.session_state:
    st.session_state.datos_cargados = False
if 'activo_cargado' not in st.session_state:
    st.session_state.activo_cargado = False
if 'pasivo_cargado' not in st.session_state:
    st.session_state.pasivo_cargado = False
if 'patrimonio_cargado' not in st.session_state:
    st.session_state.patrimonio_cargado=False
if 'resultados_cargado' not in st.session_state:
     st.session_state.resultados_cargado=False
if 'activo_data' not in st.session_state:
     st.session_state.activo_data=None
if 'pasivo_data' not in st.session_state:
    st.session_state.pasivo_data=None
if 'patrimonio_data' not in st.session_state:
    st.session_state.patrimonio_data=None
if 'resultados_data' not in st.session_state:
    st.session_state.resultados_data=None

# --- Páginas ---
if page == "Bienvenida":
    st.title("Bienvenido al Analizador Financiero")
    st.write("Esta aplicación te permite realizar un análisis financiero completo de tu empresa.")
    st.write("Comienza cargando los datos en la sección 'Carga de Datos'.")
    st.image("https://media.istockphoto.com/id/1434164608/es/foto/an%C3%A1lisis-de-datos-financieros-y-contables-gr%C3%A1ficos-y-conceptos-de-presupuesto.jpg?s=2048x2048&w=is&k=20&c=bK472uJ_l3o0F_n_s-p5b7kM3f-B-7oP_3V_j52sFyg=", width=700)


elif page == "Carga de Datos":
    st.title("Carga de Datos")
    
    if not st.session_state.datos_cargados:
        
        with st.container():
            cargar_datos_activo()
        with st.container():
            cargar_datos_pasivo()
        with st.container():
            cargar_datos_patrimonio_neto()
        with st.container():
            cargar_datos_resultados()

        # Inputs para los porcentajes de aumento por trimestre
        porcentaje_aumento_trim2 = st.number_input("Porcentaje de aumento para el Trimestre 2:", value=0.0, step=0.01, key="aumento_trim2") / 100
        porcentaje_aumento_trim3 = st.number_input("Porcentaje de aumento para el Trimestre 3:", value=0.0, step=0.01, key="aumento_trim3") / 100
        porcentaje_aumento_trim4 = st.number_input("Porcentaje de aumento para el Trimestre 4:", value=0.0, step=0.01, key="aumento_trim4") / 100

        porcentaje_aumentos = [
            porcentaje_aumento_trim2,
            porcentaje_aumento_trim3,
            porcentaje_aumento_trim4
        ]
        
        # Inputs para la inversión por trimestre
        inversion_trim2 = st.number_input("Inversión para el Trimestre 2:", value=0.0, step=0.01, key="inversion_trim2")
        inversion_trim3 = st.number_input("Inversión para el Trimestre 3:", value=0.0, step=0.01, key="inversion_trim3")
        inversion_trim4 = st.number_input("Inversión para el Trimestre 4:", value=0.0, step=0.01, key="inversion_trim4")
        
        inversiones = [
            inversion_trim2,
            inversion_trim3,
            inversion_trim4
        ]
    
        if st.button("Cargar Datos", key="cargar_todo_button", disabled = not all([st.session_state.activo_cargado,st.session_state.pasivo_cargado,st.session_state.patrimonio_cargado,st.session_state.resultados_cargado])):
            st.session_state.data['Trimestre'].append(1)
            st.session_state.data['Año'].append(2023)
            
            for key, value in st.session_state.activo_data.items():
                st.session_state.data[key].append(value)
            for key, value in st.session_state.pasivo_data.items():
                st.session_state.data[key].append(value)
            for key, value in st.session_state.patrimonio_data.items():
                st.session_state.data[key].append(value)
            for key, value in st.session_state.resultados_data.items():
                 st.session_state.data[key].append(value)
            
            st.session_state.data = calcular_datos_trimestrales(st.session_state.data, porcentaje_aumentos, inversiones)
            st.session_state.datos_cargados = True
            st.success("Datos Cargados Exitosamente! Navega a las siguientes páginas para ver los análisis")
    else:
        st.write("Los datos ya fueron cargados.")


elif page == "Ratio Patrimonial":
    if st.session_state.datos_cargados:
        df_final, df_activo, df_patrimonio_neto = crear_dataframes(st.session_state.data)
        ratios_df = ratios_patrimoniales(df_final, df_activo)

         # Visualizar los ratios en una tabla
        st.header("Ratios Patrimoniales por Trimestre")
        for trimestre in ratios_df.index:
            st.subheader(f"Trimestre {trimestre}")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f'<p class="big-number">{"{:.2f}".format(ratios_df.loc[trimestre, "Índice de prueba ácida"])}</p>', unsafe_allow_html=True)
                st.write("Índice de prueba ácida")
                st.markdown(f'<p class="big-number">{"{:.2f}".format(ratios_df.loc[trimestre, "Índice de liquidez"])}</p>', unsafe_allow_html=True)
                st.write("Índice de liquidez")
            with col2:
                st.markdown(f'<p class="percentage">{"{:.2%}".format(ratios_df.loc[trimestre, "Índice de autofinanciación"])}</p>', unsafe_allow_html=True)
                st.write("Índice de autofinanciación")
                st.markdown(f'<p class="big-number">{"{:.2f}".format(ratios_df.loc[trimestre, "Nivel de endeudamiento"])}</p>', unsafe_allow_html=True)
                st.write("Nivel de endeudamiento")
            with col3:
                st.markdown(f'<p class="big-number">{"{:.2f}".format(ratios_df.loc[trimestre, "Índice de inmovilización"])}</p>', unsafe_allow_html=True)
                st.write("Índice de inmovilización")
                st.markdown(f'<p class="big-number">{"{:.2f}".format(ratios_df.loc[trimestre, "Existencias en días de compra"])}</p>', unsafe_allow_html=True)
                st.write("Existencias en días de compra")
                st.markdown(f'<p class="big-number">{"{:.2f}".format(ratios_df.loc[trimestre, "Días de cobro a clientes"])}</p>', unsafe_allow_html=True)
                st.write("Días de cobro a clientes")
    else:
        st.write("Por favor, carga los datos primero.")


elif page == "Gráfico Ampliado Patrimonial":
    if st.session_state.datos_cargados:
        df_final, df_activo, df_patrimonio_neto = crear_dataframes(st.session_state.data)
        ratios_df = ratios_patrimoniales(df_final, df_activo)
        st.header("Gráfico Ampliado de Ratios Patrimoniales")
        plot_ratios(ratios_df)
    else:
        st.write("Por favor, carga los datos primero.")
        
elif page == "Ratios Financieros":
    if st.session_state.datos_cargados:
        df_final, df_activo, df_patrimonio_neto = crear_dataframes(st.session_state.data)
        ratios_financieros_df = ratios_financieros(df_final, df_activo, df_patrimonio_neto)
        # Visualizar los ratios en una tabla
        st.header("Ratios Financieros por Trimestre")
        for trimestre in ratios_financieros_df.index:
            st.subheader(f"Trimestre {trimestre}")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f'<p class="percentage">{"{:.2%}".format(ratios_financieros_df.loc[trimestre, "ROIC"])}</p>', unsafe_allow_html=True)
                st.write("ROIC")
                st.markdown(f'<p class="percentage">{"{:.2%}".format(ratios_financieros_df.loc[trimestre, "ROIC_despues_impuestos"])}</p>', unsafe_allow_html=True)
                st.write("ROIC después de impuestos")
            with col2:
                 st.markdown(f'<p class="big-number">{"{:.2f}".format(ratios_financieros_df.loc[trimestre, "Tiempo_cobro_ventas"])}</p>', unsafe_allow_html=True)
                 st.write("Tiempo cobro ventas")
                 st.markdown(f'<p class="big-number">{"{:.2f}".format(ratios_financieros_df.loc[trimestre, "Tiempo_pago_proveedores"])}</p>', unsafe_allow_html=True)
                 st.write("Tiempo pago proveedores")
            with col3:
                st.markdown(f'<p class="percentage">{"{:.2%}".format(ratios_financieros_df.loc[trimestre, "Rentabilidad_neta_activo"])}</p>', unsafe_allow_html=True)
                st.write("Rentabilidad neta activo")
                st.markdown(f'<p class="percentage">{"{:.2%}".format(ratios_financieros_df.loc[trimestre, "ROI"])}</p>', unsafe_allow_html=True)
                st.write("ROI")
                st.markdown(f'<p class="big-number">{"{:.2f}".format(ratios_financieros_df.loc[trimestre, "Punto_equilibrio"])}</p>', unsafe_allow_html=True)
                st.write("Punto de equilibrio")

    else:
        st.write("Por favor, carga los datos primero.")

elif page == "Ratios Económicos":
    if st.session_state.datos_cargados:
        df_final, df_activo, df_patrimonio_neto = crear_dataframes(st.session_state.data)
        ratios_economicos_df = ratios_economicos(df_final, df_activo, df_patrimonio_neto)
         # Visualizar los ratios en una tabla
        st.header("Ratios Económicos por Trimestre")
        for trimestre in ratios_economicos_df.index:
             st.subheader(f"Trimestre {trimestre}")
             col1, col2, col3 = st.columns(3)
        
             with col1:
                st.markdown(f'<p class="percentage">{"{:.2%}".format(ratios_economicos_df.loc[trimestre, "Margen_de_Utilidad_Bruta"])}</p>', unsafe_allow_html=True)
                st.write("Margen de Utilidad Bruta")
                st.markdown(f'<p class="percentage">{"{:.2%}".format(ratios_economicos_df.loc[trimestre, "Margen_Operativo"])}</p>', unsafe_allow_html=True)
                st.write("Margen Operativo")
             with col2:
                 st.markdown(f'<p class="percentage">{"{:.2%}".format(ratios_economicos_df.loc[trimestre, "Margen_Neto"])}</p>', unsafe_allow_html=True)
                 st.write("Margen Neto")
                 st.markdown(f'<p class="big-number">{"{:.2f}".format(ratios_economicos_df.loc[trimestre, "Margen_sobre_ventas"])}</p>', unsafe_allow_html=True)
                 st.write("Margen sobre ventas")
             with col3:
                st.markdown(f'<p class="big-number">{"{:.2f}".format(ratios_economicos_df.loc[trimestre, "Punto_de_Equilibrio_Económico"])}</p>', unsafe_allow_html=True)
                st.write("Punto de Equilibrio Económico")
                st.markdown(f'<p class="percentage">{"{:.2%}".format(ratios_economicos_df.loc[trimestre, "Margen_de_seguridad_Económico"])}</p>', unsafe_allow_html=True)
                st.write("Margen de Seguridad Económico")

    else:
        st.write("Por favor, carga los datos primero.")