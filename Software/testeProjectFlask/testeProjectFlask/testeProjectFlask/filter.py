class filter(object):
    """This class is responsible for applying filters"""

    def gerarCsv(x,y,endereco):
        with open(endereco + "\\teste_de_conceitos_data.csv", mode='w') as csv_file:
            fieldnames = ['time', 'value']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for time in range(0,len(x),1):
                writer.writerow({'time': x[time], 'value': y[time]})
