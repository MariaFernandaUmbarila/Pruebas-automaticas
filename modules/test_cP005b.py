"""
María Fernanda Umbarila Suárez
Ingeniería de Software III
2023-1
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import pandas as pd
import os, csv, time
import pyautogui
import time

#Cambio de foto de perfil por una foto no válida
class TestCP005b():

  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def test_cP005b(self):
    
    directorio = os.path.abspath("./values/values_cP005b.csv").replace('\\', '/')
    data = pd.read_csv(directorio)
    contador = 0
    log = []
    url = "http://localhost:8080/twitter-clone/"

    #Para cada dato en el archivo CSV
    for e, p, r in zip(data['email'], data['password'], data['route']):

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
      #Esperar para que el elemento siguiente aparezca en pantalla
      self.driver.implicitly_wait(2) 
      
      try:

        self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(7) strong").click()
        self.driver.find_element(By.CSS_SELECTOR, ".home-edit-button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".image-upload:nth-child(2) .far").click()
        
        #Valores de la columna route
        self.driver.find_element(By.ID, "file-input").send_keys(r)
        self.driver.find_element(By.NAME, "update").click()

        try:

          #Verificar que se haya realizado la publicación
          self.driver.find_element(By.XPATH, "//p[contains(text(), ' image must be image ')]")

          #Log para el caso exitoso
          log.append([
            contador,
            'Exitosa', 
            'No se realizo el cambio de imagen de perfil', 
            f'{e}-{p}-{r}',
            responseStart - navigationStart]
          )

          pyautogui.hotkey('esc')          
          #Esperar para que el elemento siguiente aparezca en pantalla
          time.sleep(2)
          self.driver.find_element(By.NAME, "update").click()
          time.sleep(1)
          self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()
        
        except NoSuchElementException:  

          #Log para el caso fallido
          log.append([
            contador,
            'Fallida', 
            'Imagen de usuario fue modificada', 
            f'{e}-{p}-{r}',
            responseStart - navigationStart]
          ) 

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

    nuevaInstancia = TestCP005b()
    nuevaInstancia.setup_method()

    inicio = time.time()
    ejecucion = nuevaInstancia.test_cP005b()
    fin = time.time()

    with open('./results/result_cp005b.csv', 'w+', newline='') as file:
      
      writer = csv.writer(file)
      writer.writerow(['Ejecucion', 'Resultado', 'Detalle', 'DatosUsados', 'TiempoRes'])

      for i in ejecucion:
        writer.writerow([i[0], i[1], i[2], i[3], i[4]])

    return fin - inicio