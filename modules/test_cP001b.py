"""
María Fernanda Umbarila Suárez
Ingeniería de Software III
2023-1
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import pandas as pd

#Registro de usuario existente
class TestCP001b():

  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_cP001b(self):

    data = pd.read_csv("values/values_cP001b.csv")
    contador = 0
    log = []

    #Para cada dato en el archivo CSV
    for n, u, e, p in zip(data['name'], data['username'], data['email'], data['password']):

      contador += 1
    
      try:

        self.driver.get("https://tucan.toolsincloud.net/")
        #Maximizar ventana
        self.driver.maximize_window()
        #Esperar para que el elemento siguiente aparezca en pantalla
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.ID, "auto").click()       
        self.driver.find_element(By.ID, "exampleInputEmail1").click()
        #Valores de la columna name
        self.driver.find_element(By.ID, "exampleInputEmail1").send_keys(n)
        self.driver.find_element(By.NAME, "username").click()
        #Valores de la columna username
        self.driver.find_element(By.NAME, "username").send_keys(u)
        #Valores de la columna email
        self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").send_keys(e)
        #Valores de la columna password
        self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(p)
        self.driver.find_element(By.NAME, "signup").click()
        #Esperar para poder ver el resultado
        self.driver.implicitly_wait(2)

        #Si todo salió bien, agrega el log de éxito
        log.append([contador, 'Ejecución exitosa', f'{n}-{u}-{e}-{p}'])

      #Si se presenta alguna excepción también se guarda
      except NoSuchElementException:
        log.append([contador, 'No se encontró el elemento dentro de la página', f'{n}-{u}-{e}-{p}'])
        return log
      except ElementNotInteractableException:
        log.append([contador, 'No se puede interactuar con el elemento', f'{n}-{u}-{e}-{p}'])
        return log
      except AttributeError:
        log.append([contador, 'Otro error ocurrió', f'{n}-{u}-{e}-{p}'])
        return log

    return log
