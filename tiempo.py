# This program is written by pradelson francois on saturday 6/2/2021

from time import *


def informacion():

  proposito = """El objetivo de este programa
es calcular segundos a minutos y viceversa.\n"""
  
  print(proposito)

informacion()

def menu():
  print("1.Segundos a Minutos\n")
  print("2.Minutos a Segundos\n")

menu()

def calculartiempo():

  opcionesDemenu = int(input("Eliga una opción de menu:"))

  if opcionesDemenu<0 or opcionesDemenu>2:
    print("solo hay dos opciones de menu!")
    sleep(1)

  if opcionesDemenu==1:
    segundos = float(input("cuantos segundos a minutos quieres saber?:"))

    calculo1 = segundos//60
    print("calculando........")
    sleep(1) 
    print(f"En {segundos} segundos hay {calculo1} minutos")

  else:
    Minutos = float(input("cuantos Minutos a segundos quieres saber?:"))

    calculo2 = Minutos*60
    print("calculando......")
    sleep(1)

    print(f"En {Minutos} minutos hay {calculo2} segundos")

calculartiempo()   

        









