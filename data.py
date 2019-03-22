class calendario():
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.meses = {1: 31, 2: 28, 3: 31, 4: 30, 
                      5: 31, 6: 30, 7: 31, 8: 31,
                      9: 30, 11: 30, 12: 31}

    def imprime_data(self):
        print(f"{self.dia:02d}/{self.mes:02d}/{self.ano:04d}") #f substitui o .format(podendo colocar variavel dentro do {})


    def amanha(self):

        if self.dia < self.meses[self.mes]: #se o dia for menor que o ultimo dia do mes que estou
            self.dia += 1
        else:
            self.dia = 1
            if self.mes == 12:
                self.mes = 1
                self.ano += 1
            else:
                self.mes += 1


        



data = calendario(21,3,2019)
data.imprime_data()
data.amanha()
