"""
María Fernanda Umbarila Suárez
Ingeniería de Software III
2023-1
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import pandas as pd
import os, csv

#Ingreso de un usuario existente
class TestCP002a():

  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def test_cP002a(self):

    directorio = os.path.abspath("./values/values_cP002a.csv").replace('\\', '/')
    data = pd.read_csv(directorio)
    contador = 0
    log = []
    url = "https://tucan.toolsincloud.net/"

    #Para cada dato en el archivo CSV
    for e, p in zip(data['email'], data['password']):

      contador += 1

      self.driver.get(url)
      #Maximizar ventana
      self.driver.maximize_window() 

      #Valores de la columna email
      self.driver.find_element(By.NAME, "email").click()         
      self.driver.find_element(By.NAME, "email").send_keys(e)

      #Valores de la columna password
      self.driver.find_element(By.NAME, "password").click()
      self.driver.find_element(By.NAME, "password").send_keys(p) 

      self.driver.find_element(By.NAME, "login").click()
      #Esperar para que cargue el elemento
      self.driver.implicitly_wait(2)

      try:

          #Intenta cerrar sesión para seguir con el siguiente
          self.driver.refresh()
          self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()

          #Log para el caso de éxito
          log.append([
            contador,
            'Exitosa', 
            'Login de usuario exitoso', 
            f'{e}-{p}']
          )

      except NoSuchElementException:  

        #Log para el caso fallido
        log.append([
          contador,
          'Fallida', 
          'Login de usuario fallido', 
          f'{e}-{p}']
        )

        continue     
  
    return log
  
  #Escritura de los resultados en CSV
  def escribirResultado():

    nuevaInstancia = TestCP002a()
    nuevaInstancia.setup_method()
    ejecucion = nuevaInstancia.test_cP002a()

    with open('./results/result_cp002a.csv', 'w+', newline='') as file:
      
      writer = csv.writer(file)
      writer.writerow(['Ejecucion', 'Resultado', 'Detalle', 'DatosUsados'])

      for i in ejecucion:
        writer.writerow([i[0], i[1], i[2], i[3]])