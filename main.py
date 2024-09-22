from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        sindescuento = cantidad * 9000
        if edad >= 18 and edad <= 30:
            peso="$"
            descuento = sindescuento * 0.15
            desctotal = sindescuento - descuento
        elif edad > 30:
            peso = "$"
            descuento = sindescuento * 0.25
            desctotal = sindescuento - descuento
        else:
            peso= ""
            descuento = "No aplica descuento"
            desctotal = sindescuento
        return render_template('ejercicio1.html', nombre=nombre, sindescuento=sindescuento, descuento=descuento, desctotal=desctotal, peso=peso)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']
        if nombre == "juan" and contraseña == "admin" :
            mensaje = "Bienvenido administrador Juan"
            return render_template('ejercicio2.html', nombre=nombre, contraseña=contraseña, mensaje=mensaje)
        elif nombre == "pepe" and contraseña == "user" :
            mensaje = "Bienvenido usuario Pepe"
            return render_template('ejercicio2.html', nombre=nombre, contraseña=contraseña, mensaje=mensaje)
        else:
            mensaje = "Usuario o contraseña incorrectos"
        return render_template('ejercicio2.html', nombre=nombre, contraseña=contraseña, mensaje=mensaje)
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)

