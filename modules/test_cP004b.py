"""
María Fernanda Umbarila Suárez
Ingeniería de Software III
2023-1
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import pandas as pd

#Cambio de nombre de usuario por uno registrado previamente
class TestCP004b():

  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_cP004b(self):
    
    data = pd.read_csv("values/values_cP004b.csv")
    contador = 0
    log = []

    #Para cada dato en el archivo CSV
    for e, p, u in zip(data['email'], data['password'], data['username']):

      contador += 1

      try:

        self.driver.get("https://tucan.toolsincloud.net/home.php")
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
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(9) img").click()
        self.driver.find_element(By.ID, "exampleInputPassword1").click()
        #Limpiar el campo
        self.driver.find_element(By.ID, "exampleInputPassword1").clear()
        #Valores de la columna username
        self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(u)
        self.driver.find_element(By.NAME, "submit").click()
        #Esperar para que el elemento siguiente aparezca en pantalla
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()
        #Esperar para poder ver el resultado
        self.driver.implicitly_wait(2)

        #Si todo salió bien, agrega el log de éxito
        log.append([contador, 'Ejecución exitosa', f'{e}-{p}-{u}'])

      #Si se presenta alguna excepción también se guarda
      except NoSuchElementException:
        log.append([contador, 'No se encontró el elemento dentro de la página', f'{e}-{p}-{u}'])
        return log
      except ElementNotInteractableException:
        log.append([contador, 'No se puede interactuar con el elemento', f'{e}-{p}-{u}'])
        return log
      except AttributeError:
        log.append([contador, 'Otro error ocurrió', f'{e}-{p}-{u}'])
        return log
  
    return log

     