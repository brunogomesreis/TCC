class csv_and_directory_controller(object):
    """this class is responsible for controlling file and folder management"""

    def newCsv(x,y,endereco):
        with open(endereco + "\\teste_de_conceitos_data.csv", mode='w') as csv_file:
            fieldnames = ['time', 'value']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for time in range(0,len(x),1):
                writer.writerow({'time': x[time], 'value': y[time]})


    def newDirectory(path):
        try:
            os.makedirs(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)


    def generateDefaultPaths(patient):
        subpath = os.getcwd() + "\\" + "Measures" + "\\" + patient + "\\" + datetime.datetime.now().strftime("%y-%m-%d - %H%M%S") + "\\"
        dirOriginal = "Original\\"
        dirIIR = "IIR\\"
        dirFIR = "FIR\\"
        print(subpath)
        if not os.path.exists(subpath):
            newDirectory(subpath)
            newDirectory(subpath + pastaOriginal)
            newDirectory(subpath + pastaIIR)
            newDirectory(subpath + pastaFIR)