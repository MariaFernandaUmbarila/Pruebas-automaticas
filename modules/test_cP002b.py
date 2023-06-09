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

#Ingreso de un usuario que no existe
class TestCP002b():

  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def test_cP002b(self):

    directorio = os.path.abspath("./values/values_cP002b.csv").replace('\\', '/')
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

          #Busca el mensaje de error
          self.driver.find_element(By.XPATH, "//div[contains(text(), 'the email or password is not correct')]")

          #Log para el caso fallido
          log.append([
            contador,
            'Exitosa', 
            'Login de usuario fallido', 
            f'{e}-{p}']
          )          

      except NoSuchElementException:  

        #Log para el caso fallido
        log.append([
          contador,
          'Fallida', 
          'Login de usuario exitoso pero usuario no existe', 
          f'{e}-{p}']
        )

        self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()

        continue     
  
    return log
  
  #Escritura de los resultados en CSV
  def escribirResultado():

    nuevaInstancia = TestCP002b()
    nuevaInstancia.setup_method()
    ejecucion = nuevaInstancia.test_cP002b()

    with open('./results/result_cp002b.csv', 'w+', newline='') as file:
      
      writer = csv.writer(file)
      writer.writerow(['Ejecucion', 'Resultado', 'Detalle', 'DatosUsados'])

      for i in ejecucion:
        writer.writerow([i[0], i[1], i[2], i[3]])