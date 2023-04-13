"""
María Fernanda Umbarila Suárez
Ingeniería de Software III
2023-1
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import pandas as pd

#Publicación de un Squawk válido por parte del usuario
class TestCP003a():

  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_cP003a(self):

    data = pd.read_csv("values/values_cP003a.csv")
    contador = 0
    log = []

    #Para cada dato en el archivo CSV
    for e, p, t in zip(data['email'], data['password'], data['text']):

      contador += 1
 
      try:

        self.driver.get("https://tucan.toolsincloud.net/")
        #Maximizar ventana
        self.driver.maximize_window()
        self.driver.find_element(By.NAME, "email").click()
        #Valores de la columna email
        self.driver.find_element(By.NAME, "email").send_keys(e)
        self.driver.find_element(By.NAME, "password").click()
        #Valores de la columna password
        self.driver.find_element(By.NAME, "password").send_keys(p)
        self.driver.find_element(By.NAME, "login").click()
        #Esperar para que el elemento siguiente aparezca en pantalla
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.NAME, "status").click()
        #Valoresd de la columna texto
        self.driver.find_element(By.NAME, "status").send_keys(t)
        self.driver.find_element(By.ID, "tweet-input").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()
        #Esperar para poder ver el resultado
        self.driver.implicitly_wait(2)

        #Si todo salió bien, agrega el log de éxito
        log.append([contador, 'Ejecución exitosa', f'{e}-{p}-{t}'])

      #Si se presenta alguna excepción también se guarda
      except NoSuchElementException:
        log.append([contador, 'No se encontró el elemento dentro de la página', f'{e}-{p}-{t}'])
        return log
      except ElementNotInteractableException:
        log.append([contador, 'No se puede interactuar con el elemento', f'{e}-{p}-{t}'])
        return log
      except AttributeError:
        log.append([contador, 'Otro error ocurrió', f'{e}-{p}-{t}'])
        return log
  
    return log