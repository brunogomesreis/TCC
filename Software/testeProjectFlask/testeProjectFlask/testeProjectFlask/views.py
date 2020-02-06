"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from testeProjectFlask import app
import json
from flask import request
from  testeProjectFlask.file_controller import file_controller
from  testeProjectFlask.operations_controller import operations_controller

@app.route('/')
@app.route('/home', methods=["GET","POST"] )
def home():
    opc = operations_controller()
    if request.method == "POST":
        patientName = request.args.get('paciente')
        experimentName = request.args.get('experimento')
        operation = request.args.get('operacao')
        filtro = request.args.get('filtro')
        measure = file_controller.getMeasure(experimentName,patientName)
        if (operation == 'derivada'):
            bar = opc.create_derivate_plot(measure,filtro)
        elif (operation == 'fft'):
             bar = opc.create_fft_plot(measure,filtro)
        elif (operation == 'interpolado'):
             bar = opc.create_interpolated_plot(measure,filtro)
        else:
            bar = opc.create_plot(measure,filtro)
        return bar
    else:
        bar = opc.create_random_plot()
        return render_template('index.html',
            pacientes = file_controller.getPatientsList(),
            experimentos = file_controller.getExperimentsList(), 
            plot=bar,
            selectedExperiment = "saparada de teste")


@app.route('/cadastro', methods=["GET","POST"])
def cadastro():  

    if request.method == "POST":
        patient = json.loads(request.form['data'])            
        file_controller.addPatient(patient)

    return render_template('cadastro.html',
        title='Cadastro',
        year=datetime.now().year,)

@app.route('/experimento', methods=["GET","POST"])
def experimento():

    if request.method == "POST":
        file = request.data
        experimentName = request.args.get('nome')
        patientCpf = request.args.get('cpf')
        experiment = {
            "nome": experimentName,
        }
        file_controller.addExperiment(experiment)
        experiment =  file_controller.getExperiment(experimentName)
        patient = file_controller.getPatient(patientCpf)        
        x,y = file_controller.readUplodedFile(file)
        measure = {
            "paciente": patient['_id'],
            "experimento": experiment['_id'],
            "x": x,
            "y": y,
        }
        file_controller.addMeasure(measure)
        
        


    return render_template('experimento.html',
        pacientes = file_controller.getPatientsList(),
        experimentos = file_controller.getExperimentsList(),
        title='Experimento',
        year=datetime.now().year,)

#@app.route('/teste/<cpf>')
#def teste(cpf):
#    user = patients.find_one_or_404({"cpf": cpf})
#    return user['email']

#@app.route('/teste2',  methods=["GET","POST"])
#def teste2():
#    if request.method == "POST":
#        file = request.data
        
                 
#    return file_controller.readUplodedFile(file)