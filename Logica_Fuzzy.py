from tkinter import *
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plot

# Variáveis do Problema
comida = ctrl.Antecedent(np.arange(0, 11, 1), "comida")
servico = ctrl.Antecedent(np.arange(0, 11, 1), "servico")
gorjeta = ctrl.Consequent(np.arange(0, 26, 1), "gorjeta")

comida.automf(names=["péssima", "comível", "deliciosa"])

# Cria funções de pertinência usando tipos variados
servico["ruim"] = fuzz.trimf(servico.universe, [0, 0, 5])
servico["aceitável"] = fuzz.gaussmf(servico.universe, 5, 2)
servico["excelente"] = fuzz.gaussmf(servico.universe, 10, 3)

gorjeta["baixa"] = fuzz.trimf(gorjeta.universe, [0, 0, 13])
gorjeta["média"] = fuzz.trapmf(gorjeta.universe, [0, 13, 15, 25])
gorjeta["alta"] = fuzz.trimf(gorjeta.universe, [15, 25, 25])

# Regras de decisões
rule1 = ctrl.Rule(servico["excelente"] | comida["deliciosa"], gorjeta["alta"])
rule2 = ctrl.Rule(servico["aceitável"], gorjeta["média"])
rule3 = ctrl.Rule(servico["ruim"] & comida["péssima"], gorjeta["baixa"])

class Aplicacao:
    def __init__(self, master=None):
        self.fonte = ("Calibri", "8")

        self.conteiner1 = Frame(master)
        self.conteiner1["pady"] = 10
        self.conteiner1.pack()

        self.conteiner2 = Frame(master)
        self.conteiner2["padx"] = 20
        self.conteiner2["pady"] = 5
        self.conteiner2.pack()

        self.conteiner3 = Frame(master)
        self.conteiner3["padx"] = 20
        self.conteiner3["pady"] = 5
        self.conteiner3.pack()

        self.conteiner4 = Frame(master)
        self.conteiner4["padx"] = 20
        self.conteiner4["pady"] = 5
        self.conteiner4.pack()

        self.conteiner5 = Frame(master)
        self.conteiner5["padx"] = 20
        self.conteiner5["pady"] = 5
        self.conteiner5.pack()

        self.conteiner6 = Frame(master)
        self.conteiner6["padx"] = 20
        self.conteiner6["pady"] = 5
        self.conteiner6.pack()

        self.conteiner7 = Frame(master)
        self.conteiner7["padx"] = 20
        self.conteiner7["pady"] = 5
        self.conteiner7.pack()

        self.conteiner8 = Frame(master)
        self.conteiner8["padx"] = 20
        self.conteiner8["pady"] = 5
        self.conteiner8.pack()

        self.conteiner9 = Frame(master)
        self.conteiner9["padx"] = 20
        self.conteiner9["pady"] = 5
        self.conteiner9.pack()

        #######################################

        self.titulo = Label(self.conteiner1, text="Teste")
        self.titulo["font"] = ("Arial", "10")
        self.titulo.pack()

        self.lblcomida = Label(self.conteiner2, text="Qualidade da Comida:")
        self.lblcomida["font"] = self.fonte
        self.lblcomida["width"] = 20
        self.lblcomida.pack(side = LEFT)

        self.respcomida = Entry(self.conteiner2)
        self.respcomida["font"] = self.fonte
        self.respcomida["width"] = 10
        self.respcomida.pack(side = LEFT)

        self.lblservico = Label(self.conteiner3, text="Qualidade do Servico:")
        self.lblservico["font"] = self.fonte
        self.lblservico["width"] = 20
        self.lblservico.pack(side=LEFT)

        self.respservico = Entry(self.conteiner3)
        self.respservico["font"] = self.fonte
        self.respservico["width"] = 10
        self.respservico.pack(side=LEFT)

        self.btncalculo = Button(self.conteiner4, text="Calcular")
        self.btncalculo["font"] = self.fonte
       	self.btncalculo["width"] = 10
        self.btncalculo["command"] = self.resultado_calculo
        self.btncalculo.pack()

        self.textresultado = Label(self.conteiner5, text="Resultado:")
        self.textresultado["font"] = ("Arial", "10", "bold")
        self.textresultado.pack()

        self.resultcalculo = Label(self.conteiner6, text="")
        self.resultcalculo["font"] = self.fonte
        self.resultcalculo.pack()

        self.btngrafico = Button(self.conteiner7, text="Graficos1")
        self.btngrafico["font"] = self.fonte
        self.btngrafico["width"] = 10
        self.btngrafico["command"] = self.print_grafico
        self.btngrafico.pack()

        self.btngraficoresult = Button(self.conteiner8, text="Graficos2")
        self.btngraficoresult["font"] = self.fonte
        self.btngraficoresult["width"] = 10
        self.btngraficoresult["command"] = self.grafico_resultado
        self.btngraficoresult.pack()

    def resultado_calculo(self):
        aux1 = self.respcomida.get()
        aux2 = self.respservico.get()

        gorjeta_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
        gorjeta_simulador = ctrl.ControlSystemSimulation(gorjeta_ctrl)
        gorjeta_simulador.input["comida"] = float(aux1)
        gorjeta_simulador.input["servico"] = float(aux2)
        gorjeta_simulador.compute()

        print(round(gorjeta_simulador.output["gorjeta"]))
        self.resultcalculo["text"] = round(gorjeta_simulador.output["gorjeta"])

    def print_grafico(self):
        comida.view()
        servico.view()
        gorjeta.view()

    def grafico_resultado(self):
        aux1 = self.respcomida.get()
        aux2 = self.respservico.get()

        gorjeta_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
        gorjeta_simulador = ctrl.ControlSystemSimulation(gorjeta_ctrl)
        gorjeta_simulador.input["comida"] = float(aux1)
        gorjeta_simulador.input["servico"] = float(aux2)
        gorjeta_simulador.compute()

        comida.view(sim=gorjeta_simulador)
        servico.view(sim=gorjeta_simulador)
        gorjeta.view(sim=gorjeta_simulador)

root = Tk()
Aplicacao(root)
root.mainloop()
