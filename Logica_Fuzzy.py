from tkinter import *
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plot

# Variáveis do Problema
velocidade = ctrl.Antecedent(np.arange(0, 101, 1), "velocidade")
limite = ctrl.Antecedent(np.arange(0, 101, 1), "limite")
multa = ctrl.Consequent(np.arange(0, 101, 1), "multa")

velocidade.automf(names=["baixa", "media", "alta"])

# Cria funções de pertinência usando tipos variados
limite["baixo"] = fuzz.trimf(limite.universe, [0, 0, 50])
limite["medio"] = fuzz.gaussmf(limite.universe, 50, 10)
limite["alto"] = fuzz.gaussmf(limite.universe, 100, 20)

multa["baixa"] = fuzz.trapmf(multa.universe, [0, 0, 20, 50])
multa["media"] = fuzz.trimf(multa.universe, [30, 50, 70])
multa["alta"] = fuzz.trimf(multa.universe, [50, 100, 100])

# Regras de decisões
rule1 = ctrl.Rule(limite["baixo"] & velocidade["alta"], multa["alta"])
rule2 = ctrl.Rule(limite["medio"] & velocidade["alta"], multa["media"])
rule3 = ctrl.Rule(limite["alto"] & velocidade["alta"], multa["baixa"])
rule4 = ctrl.Rule(limite["baixo"] & velocidade["media"], multa["media"])
rule5 = ctrl.Rule(limite["medio"] & velocidade["media"], multa["baixa"])

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

        self.lblvelocidade = Label(self.conteiner2, text="Velocidade:")
        self.lblvelocidade["font"] = self.fonte
        self.lblvelocidade["width"] = 20
        self.lblvelocidade.pack(side = LEFT)

        self.respvelocidade = Entry(self.conteiner2)
        self.respvelocidade["font"] = self.fonte
        self.respvelocidade["width"] = 10
        self.respvelocidade.pack(side = LEFT)

        self.lbllimite = Label(self.conteiner3, text="Limite de velocidade:")
        self.lbllimite["font"] = self.fonte
        self.lbllimite["width"] = 20
        self.lbllimite.pack(side=LEFT)

        self.resplimite = Entry(self.conteiner3)
        self.resplimite["font"] = self.fonte
        self.resplimite["width"] = 10
        self.resplimite.pack(side=LEFT)

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
        aux1 = self.respvelocidade.get()
        aux2 = self.resplimite.get()

        multa_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
        multa_simulador = ctrl.ControlSystemSimulation(multa_ctrl)
        multa_simulador.input["velocidade"] = float(aux1)
        multa_simulador.input["limite"] = float(aux2)
        multa_simulador.compute()

        print(round(multa_simulador.output["multa"]))
        self.resultcalculo["text"] = round(multa_simulador.output["multa"])

    def print_grafico(self):
        velocidade.view()
        #cv2.imshow('Imagem Original',velocidade.view()) 
        #cv2.moveWindow('Imagem Original',100,100)
        limite.view()
        #cv2.imshow('Imagem Original',limite.view()) 
        #cv2.moveWindow('Imagem Original',100,100)
        multa.view()
        #cv2.imshow('Imagem Original',multa.view())
        #cv2.moveWindow('Imagem Original',100,100)

    def grafico_resultado(self):
        aux1 = self.respvelocidade.get()
        aux2 = self.resplimite.get()

        multa_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
        multa_simulador = ctrl.ControlSystemSimulation(multa_ctrl)
        multa_simulador.input["velocidade"] = float(aux1)
        multa_simulador.input["limite"] = float(aux2)
        multa_simulador.compute()

        velocidade.view(sim=multa_simulador)
        limite.view(sim=multa_simulador)
        multa.view(sim=multa_simulador)

root = Tk()
Aplicacao(root)
root.mainloop()
