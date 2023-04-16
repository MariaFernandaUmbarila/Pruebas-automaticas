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
import pyautogui

#Cambio de foto de perfil por una foto válida
class TestCP005a():

  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def test_cP005a(self):
    
    directorio = os.path.abspath("./values/values_cP005a.csv").replace('\\', '/')
    data = pd.read_csv(directorio)
    contador = 0
    log = []
    url = "https://tucan.toolsincloud.net/"

    #Para cada dato en el archivo CSV
    for e, p, r in zip(data['email'], data['password'], data['route']):

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
      #Esperar para que el elemento siguiente aparezca en pantalla
      self.driver.implicitly_wait(2) 
      
      try:

        self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(7) strong").click()
        self.driver.find_element(By.CSS_SELECTOR, ".home-edit-button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".image-upload:nth-child(2) .far").click()
        
        #Valores de la columna route
        self.driver.find_element(By.ID, "file-input").send_keys(r)
        self.driver.find_element(By.NAME, "update").click()

        pyautogui.hotkey('esc')
        #Esperar para que el elemento siguiente aparezca en pantalla
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()

        try:

          #Verificar que se haya realizado la publicación
          self.driver.find_element(By.XPATH, "//p[contains(text(), ' image must be image ')]")

          #Log para el caso fallido
          log.append([
            contador,
            'Fallida', 
            'Imagen de usuario no fue modificada', 
            f'{e}-{p}-{r}']
          ) 
        
        except NoSuchElementException:            

          #Log para el caso exitoso
          log.append([
            contador,
            'Exitosa', 
            'Se realizo el cambio de imagen de perfil', 
            f'{e}-{p}-{r}']
          )

      except NoSuchElementException:  

        #Log para el caso fallido
        log.append([
          contador,
          'Fallida', 
          'Login de usuario exitoso pero usuario no existe', 
          f'{e}-{p}']
        )

        continue
  
    return log
  
  #Escritura de los resultados en CSV
  def escribirResultado():

    nuevaInstancia = TestCP005a()
    nuevaInstancia.setup_method()
    ejecucion = nuevaInstancia.test_cP005a()

    with open('./results/result_cp005a.csv', 'w+', newline='') as file:
      
      writer = csv.writer(file)
      writer.writerow(['Ejecucion', 'Resultado', 'Detalle', 'DatosUsados'])

      for i in ejecucion:
        writer.writerow([i[0], i[1], i[2], i[3]])