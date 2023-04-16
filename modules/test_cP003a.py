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

#Publicación de un Squawk válido por parte del usuario
class TestCP003a():

  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def test_cP003a(self):

    directorio = os.path.abspath("./values/values_cP003a.csv").replace('\\', '/')
    data = pd.read_csv(directorio)
    contador = 0
    log = []
    url = "https://tucan.toolsincloud.net/"

    #Para cada dato en el archivo CSV
    for e, p, t in zip(data['email'], data['password'], data['text']):

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

      try:

        #Esperar para que el elemento siguiente aparezca en pantalla
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.NAME, "status").click()

        #Valoresd de la columna texto
        self.driver.find_element(By.NAME, "status").send_keys(t)
        self.driver.find_element(By.ID, "tweet-input").click()

        try:

          #Verificar que se haya realizado la publicación
          self.driver.find_element(By.CLASS_NAME, "item2-pair")

          #Log para el caso fallido
          log.append([
            contador,
            'Fallida', 
            'No se realizo la publicacion', 
            f'{e}-{p}-{t}']
          )          

        except NoSuchElementException:  

          #Log para el caso exitoso
          log.append([
            contador,
            'Exitosa', 
            'Publicacion realizada', 
            f'{e}-{p}-{t}']
          )                    

        self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()
      
      except NoSuchElementException:  

        #Log para el caso fallido
        log.append([
          contador,
          'Fallida', 
          'Login de usuario fallido', 
          f'{e}-{p}-{t}']
        )

        continue 
  
    return log
  
  #Escritura de los resultados en CSV
  def escribirResultado():

    nuevaInstancia = TestCP003a()
    nuevaInstancia.setup_method()
    ejecucion = nuevaInstancia.test_cP003a()
    print(ejecucion)

    with open('./results/result_cp003a.csv', 'w+', newline='') as file:
      
      writer = csv.writer(file)
      writer.writerow(['Ejecucion', 'Resultado', 'Detalle', 'DatosUsados'])

      for i in ejecucion:
        writer.writerow([i[0], i[1], i[2], i[3]])