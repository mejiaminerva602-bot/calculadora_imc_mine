from nicegui import ui
import os

def calculoIMC():
    try:
        # 1. Obtener datos
        peso_num = float(peso.value)
        altura_num = float(altura.value)
        
        # 2. Calcular IMC
        imc = peso_num / (altura_num ** 2)
        
        # 3. Mostrar IMC
        resultado.text = f'Tu IMC es: {imc:.2f}'
        
        # 4. Evaluar resultado
        if imc < 18.5:
            mensaje_texto = "Actualmente estás bajo de peso"
        elif 18.5 <= imc < 24.9:
            mensaje_texto = "Tu peso es normal"
        elif 25 <= imc < 30:
            mensaje_texto = "Tienes sobrepeso"
        else:
            mensaje_texto = "Tienes obesidad"
            
        # 5. Mostrar mensaje
        mensaje.text = mensaje_texto
        
    except:
        resultado.text = "Ingresa numeros validos"
        mensaje.text = ""

def limpiar():
    peso.value = ''
    altura.value = ''
    resultado.text = 'Resultado: 0'
    mensaje.text = ''

with ui.column().classes('w-full h-screen items-center justify-center').style('background-color:#2338;').classes('items-center'):
    with ui.card().style('width:400px; background-color:#00233B;').classes('items-center'):
        ui.label('INDICE DE MASA CORPORAL').style('color:white; font-size:30px; font-weight:bold').classes('items-center')
        ui.image('imc.PNG').style('width:250px')
        
        peso = ui.input('Ingresa tu peso en kg').props('dark outlined').style('width:350px')
        altura = ui.input('Ingresa tu estatura').props('dark outlined').style('width:350px')
        
        with ui.row().classes('w-full justify-center no-wrap').style('gap:10px;'):
            ui.button('Calcular', icon='calculate', color='green', on_click=calculoIMC).style('color:white; width:140px')
            ui.button('LIMPIAR', icon='delete', color='red', on_click=limpiar).style('color:white; width:140px')
        
        resultado = ui.label('Resultado: 0').style('color:white; font-size:20px')
        mensaje = ui.label('').style('color:yellow; font-size:18px')

# Esto es lo que le agregas para Render
port = int(os.environ.get("PORT", 8080))
ui.run(host='0.0.0.0', port=port, title='Calculadora IMC')