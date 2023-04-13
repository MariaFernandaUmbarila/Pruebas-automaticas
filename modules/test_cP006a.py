"""
María Fernanda Umbarila Suárez
Ingeniería de Software III
2023-1
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import pandas as pd

#Cambio de contraseña de usuario por una contraseña válida
class TestCP006a():

  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_cP006a(self):

    data = pd.read_csv("values/values_cP006a.csv")
    contador = 0
    log = []

    #Para cada dato en el archivo CSV
    for e, p, n in zip(data['email'], data['password'], data['new']):

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
        self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(9) img").click()
        self.driver.find_element(By.ID, "v-pills-profile-tab").click()
        self.driver.find_element(By.NAME, "old_password").click()
        #Valores de la columna password
        self.driver.find_element(By.NAME, "old_password").send_keys(p)
        #Valores de la columna new
        self.driver.find_element(By.NAME, "new_password").send_keys(n)
        #Valores de la columa new
        self.driver.find_element(By.NAME, "ver_password").send_keys(n)
        self.driver.find_element(By.CSS_SELECTOR, ".text-center:nth-child(5) > .btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()
        #Esperar para que el elemento siguiente aparezca en pantalla
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.NAME, "email").click()
        #Valores de la columna email
        self.driver.find_element(By.NAME, "email").send_keys(e) 
        self.driver.find_element(By.NAME, "password").click()
        #Valores de la columna new
        self.driver.find_element(By.NAME, "password").send_keys(n)
        self.driver.find_element(By.NAME, "login").click()
        #Esperar para que el elemento siguiente aparezca en pantalla
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()
        #Esperar para poder ver el resultado
        self.driver.implicitly_wait(2)

        #Si todo salió bien, agrega el log de éxito
        log.append([contador, 'Ejecución exitosa', f'{e}-{p}-{n}'])

      #Si se presenta alguna excepción también se guarda
      except NoSuchElementException:
        log.append([contador, 'No se encontró el elemento dentro de la página', f'{e}-{p}-{n}'])
        return log
      except ElementNotInteractableException:
        log.append([contador, 'No se puede interactuar con el elemento', f'{e}-{p}-{n}'])
        return log
      except AttributeError:
        log.append([contador, 'Otro error ocurrió', f'{e}-{p}-{n}'])
        return log
  
    return log