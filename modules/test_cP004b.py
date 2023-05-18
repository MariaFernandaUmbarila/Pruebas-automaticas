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
import time

#Cambio de nombre de usuario por uno registrado previamente
class TestCP004b():

  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def test_cP004b(self):
    
    directorio = os.path.abspath("./values/values_cP004b.csv").replace('\\', '/')
    data = pd.read_csv(directorio)
    contador = 0
    log = []
    url = "http://localhost:8080/twitter-clone/"

    #Para cada dato en el archivo CSV
    for e, p, u in zip(data['email'], data['password'], data['username']):

      contador += 1
        
      self.driver.get(url)
      #Maximizar ventana
      self.driver.maximize_window()

      #Para tiempos de respuesta
      navigationStart = self.driver.execute_script("return window.performance.timing.navigationStart")
      responseStart = self.driver.execute_script("return window.performance.timing.responseStart")

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
        self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(9) img").click()
        self.driver.find_element(By.ID, "exampleInputPassword1").click()

        #Limpiar el campo
        self.driver.find_element(By.ID, "exampleInputPassword1").clear()
        #Valores de la columna username
        self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(u)

        self.driver.find_element(By.NAME, "submit").click()

        try:

          #Busca el mensaje de error
          self.driver.find_element(By.XPATH, "//p[contains(text(), ' This username is already use ')]")

          #Log para el caso exitoso
          log.append([
            contador,
            'Exitosa', 
            'Nombre de usuario no ha sido modificado', 
            f'{e}-{p}-{u}',
            responseStart - navigationStart]
          )  

        except NoSuchElementException:

          #Log para el caso fallido
          log.append([
            contador,
            'Fallida', 
            'Nombre de usuario fue cambiado aunque ya exista', 
            f'{e}-{p}-{u}',
            responseStart - navigationStart]
          )

        #Esperar para que el elemento siguiente aparezca en pantalla
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()
      
      except NoSuchElementException:  

        #Log para el caso fallido
        log.append([
          contador,
          'Fallida', 
          'Login de usuario fallido', 
          f'{e}-{p}-{u}',
          responseStart - navigationStart]
        )

        continue      
  
    return log

#Escritura de los resultados en CSV
  def escribirResultado():

    nuevaInstancia = TestCP004b()
    nuevaInstancia.setup_method()

    inicio = time.time()
    ejecucion = nuevaInstancia.test_cP004b()
    fin = time.time()

    with open('./results/result_cp004b.csv', 'w+', newline='') as file:
      
      writer = csv.writer(file)
      writer.writerow(['Ejecucion', 'Resultado', 'Detalle', 'DatosUsados', 'TiempoRes'])

      for i in ejecucion:
        writer.writerow([i[0], i[1], i[2], i[3], i[4]])

    return fin - inicio