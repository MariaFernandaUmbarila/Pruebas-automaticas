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

#Cambio de contraseña de usuario por una contraseña no válida
class TestCP006b():

  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def test_cP006b(self):

    directorio = os.path.abspath("./values/values_cP006b.csv").replace('\\', '/')
    data = pd.read_csv(directorio)
    contador = 0
    log = []
    url = "http://localhost:8080/twitter-clone/"

    #Para cada dato en el archivo CSV
    for e, p, n in zip(data['email'], data['password'], data['new']):

      contador += 1
 
      self.driver.get(url)
      #Maximizar ventana
      self.driver.maximize_window()

      #Para tiempos de respuesta
      navigationStart = self.driver.execute_script("return window.performance.timing.navigationStart")
      responseStart = self.driver.execute_script("return window.performance.timing.responseStart")

      #Esperar para que el elemento siguiente aparezca en pantalla
      self.driver.implicitly_wait(2)
      
      #Valores de la columna email
      self.driver.find_element(By.NAME, "email").click()
      self.driver.find_element(By.NAME, "email").send_keys(e)

      #Valores de la columna password
      self.driver.find_element(By.NAME, "password").click()
      self.driver.find_element(By.NAME, "password").send_keys(p)
      self.driver.find_element(By.NAME, "login").click()

      #Esperar para que el elemento siguiente aparezca en pantalla
      self.driver.implicitly_wait(2)

      try:

        self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(9) img").click()
        self.driver.find_element(By.ID, "v-pills-profile-tab").click()
        self.driver.implicitly_wait(2) 

        #Valores de la columna password
        self.driver.find_element(By.NAME, "old_password").click()
        self.driver.find_element(By.NAME, "old_password").send_keys(p)
        
        #Valores de la columna new
        self.driver.find_element(By.NAME, "new_password").click()
        self.driver.find_element(By.NAME, "new_password").send_keys(n)

        #Valores de la columa new
        self.driver.find_element(By.NAME, "ver_password").click()
        self.driver.find_element(By.NAME, "ver_password").send_keys(n)

        self.driver.find_element(By.CSS_SELECTOR, ".text-center:nth-child(5) > .btn").click()

        try:

          #Buscar el mensaje de error
          self.driver.find_element(By.XPATH, "//p[contains(text(), ' New Password must between 5 and 20 length ')]")

          #Log para el caso exitoso
          log.append([
            contador,
            'Exitosa', 
            'Password no se cambio', 
            f'{e}-{p}-{n}',
            responseStart - navigationStart]
          )

          self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()
        
        except NoSuchElementException: 

          self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()
          continue

      except NoSuchElementException:  

        #Log para el caso fallido
        log.append([
          contador,
          'Fallida', 
          'Login de usuario exitoso pero usuario no existe', 
          f'{e}-{p}',
          responseStart - navigationStart]
        )

        continue
  
    return log
  
  #Escritura de los resultados en CSV
  def escribirResultado():

    nuevaInstancia = TestCP006b()
    nuevaInstancia.setup_method()

    inicio = time.time()
    ejecucion = nuevaInstancia.test_cP006b()
    fin = time.time()

    with open('./results/result_cp006b.csv', 'w+', newline='') as file:
      
      writer = csv.writer(file)
      writer.writerow(['Ejecucion', 'Resultado', 'Detalle', 'DatosUsados', 'TiempoRes'])

      for i in ejecucion:
        writer.writerow([i[0], i[1], i[2], i[3], i[4]])

    return fin - inicio