from flask import Flask, render_template, redirect, url_for, request, make_response, flash
import forms
from act_cajas import Calculadora, Traductor
from act3_Resistencias import Resistencia
from flask_wtf.csrf import CSRFProtect
 

app = Flask(__name__)
app.config['SECRET_KEY']="esta es tu clave encriptada"
csrf=CSRFProtect(app)

@app.route('/')
def mainn():
    return redirect('/cajas_dinamica')

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    registrar_Alumno = forms.UserForm(request.form)
    Mat = ''
    Nom = ''
    App = ''
    Apm = ''
    Email = ''
        
    if request.method == 'POST' and registrar_Alumno.validate():
        Mat = registrar_Alumno.matricula.data
        Nom = registrar_Alumno.nombre.data
        App = registrar_Alumno.apaterno.data
        Apm = registrar_Alumno.amaterno.data
        Email = registrar_Alumno.email.data
    
    return render_template('alumnos.html', form = registrar_Alumno, mat=Mat, nom=Nom, app=App, apm=Apm, ema=Email, name="Alumnos")

@app.route('/cajas_dinamica', methods=['GET', 'POST'])
def method_name(): 
    Active = False
    Ns = 0
    
    if request.method == 'POST':
        Ns = int(request.form.get('numero'))
        Active = Ns != 0
    
    return render_template('cajas.html', active = Active, ns = Ns, name="Cajas Dinámicas")


@app.route('/calcular', methods=['GET', 'POST'])
def calcular():
    Numeros = Calculadora.get_Array(request.form)
    
    return render_template("calcular.html",
                           numeros = Numeros,
                           repetidos = Calculadora.contar_repeticiones(Numeros),
                           comas = Calculadora.concatenar_Numeros(Numeros),
                           promedio = Calculadora.promedio(Numeros),
                           nMenor = Calculadora.num_Menor(Numeros),
                           nMayor = Calculadora.num_Mayor(Numeros),
                           name = "Resultado de " + str(len(Numeros)) + " números")

@app.route('/cookie', methods=['GET', 'POST'])
def cookies():
    reg_user = forms.LoginForm(request.form)
    
    response = make_response(render_template('cookie.html', name = 'Cookie', form = reg_user))
    
    if request.method == 'POST' and reg_user.validate():
        user = reg_user.username.data
        passw = reg_user.password.data
        datos = user + '@' + passw
        seccess_message= 'Bienvvenido {}'.format(user)
        response.set_cookie('datos_user', datos)
        flash(success_message)
        # print(user+' '+pasw)
    return response


@app.route('/traductor', methods=['GET', 'POST'])
def traductor():
    reg_palabra = forms.Languages(request.form)
    result = ''
    word = ''
    
    if request.method == 'POST':
        status = request.form.get('status')
        if status == 'registrar' and reg_palabra.validate():
            span = reg_palabra.spanish.data
            en = reg_palabra.english.data
            Traductor.guardar(span, en)
        elif status == 'buscar':
            word = request.form.get('word')
            lan = request.form.get('select')
            result = "Traducción: {}".format(Traductor.buscar_Palabra(word, lan))
    return render_template('traductor.html', name='Traductor', form=reg_palabra, result = result, search = word)


@app.route("/resistencia", methods=['GET', 'POST'])
def resistencia():
    resistors = Resistencia()
    res = {}
    banda1 = ''
    banda2 = ''
    banda3 = ''
    tolerancia = ''
    resistencia = forms.ResistenciaForm(request.form)
    if request.method == 'POST' and resistencia.validate():
        banda1 = resistors.setColor(resistencia.banda1.data)
        banda2 = resistors.setColor(resistencia.banda2.data)
        banda3 = resistors.setColor(resistencia.banda3.data)
        tolerancia = resistors.setTolerancia(resistencia.tolerancia.data)
        res = resistors.calcular(resistencia)
        flash('Calculo registrado', 'success')
    return render_template('resistencia.html', form=resistencia, banda1=banda1, banda2=banda2, banda3=banda3, tolerancia=tolerancia, res=res)




if __name__ == "__main__":
    #csrf.init_app(app)
    app.run(debug = True, port=3000)

