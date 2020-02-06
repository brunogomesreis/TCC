from testeProjectFlask import mongo
from bson.objectid import ObjectId


patients = mongo.db.Patients
experiments = mongo.db.Experiments
measures = mongo.db.Measures

class file_controller(object):
    """this class is responsible for controlling file and folder management"""
    #def addMeasure(Patient_id,Experiment_id,x,y):
        

    def addPatient(patient):
        patients.update({"cpf": patient['cpf']},
        {"$set": patient},
        w=1, upsert=True)

    def addExperiment(experiment):
        experiments.update({"nome": experiment['nome']},
        {"$set": experiment},
        w=1, upsert=True)

    def addMeasure(measure):
        measures.update({"$and": [{"paciente": ObjectId(measure['paciente'])},{"experimento": ObjectId(measure['experimento'])}]},
        {"$set": measure},
        w=1, upsert=True)

    def getPatientsList():
        return patients.find()

    def getPatient(cpf):
        return patients.find_one({'cpf':cpf})

    def getPatientByName(nome):
        return patients.find_one({'nome':nome})
         
    def getExperimentsList():
         return experiments.find()
    
    def getExperiment(nome):
        return experiments.find_one({'nome':nome})

    def getMeasure(experimentName, patientName):
        experiment =  file_controller.getExperiment(experimentName)
        patient = file_controller.getPatientByName(patientName)
        return measures.find_one({"$and": [{"paciente": ObjectId(patient['_id'])},{"experimento": ObjectId(experiment['_id'])}]})  
         

    def readUplodedFile(file):
        x = []
        y = []
        reader = list(filter(None, file.decode().splitlines()))        
        for row in reader:
            row = row.split(',')
            x.append(row[0])
            y.append(row[1])
        x.pop(0)
        y.pop(0)

        return x,y

    
        

