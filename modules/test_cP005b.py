"""
María Fernanda Umbarila Suárez
Ingeniería de Software III
2023-1
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import pandas as pd
import pyautogui, time

#Cambio de foto de perfil por una foto no válida
class TestCP005b():

  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_cP005b(self):
    
    data = pd.read_csv("values/values_cP005b.csv")
    contador = 0
    log = []

    #Para cada dato en el archivo CSV
    for e, p, r in zip(data['email'], data['password'], data['route']):

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
        self.driver.implicitly_wait(2) 
        self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(7) strong").click()
        # 4 | click | css=.home-edit-button | 
        self.driver.find_element(By.CSS_SELECTOR, ".home-edit-button").click()
        # 5 | click | css=.image-upload:nth-child(2) .far | 
        self.driver.find_element(By.CSS_SELECTOR, ".image-upload:nth-child(2) .far").click()
        #Valores de la columna route
        self.driver.find_element(By.ID, "file-input").send_keys(r)
        #pyautogui.press('enter')
        self.driver.find_element(By.NAME, "update").click()
        pyautogui.hotkey('esc')
        time.sleep(3)
        pyautogui.hotkey('esc')
        #Esperar para que el elemento siguiente aparezca en pantalla
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()
        #Esperar para poder ver el resultado
        self.driver.implicitly_wait(2)

        #Si todo salió bien, agrega el log de éxito
        log.append([contador, 'Ejecución exitosa', f'{e}-{p}-{r}'])

      #Si se presenta alguna excepción también se guarda
      except NoSuchElementException:
        log.append([contador, 'No se encontró el elemento dentro de la página', f'{e}-{p}-{r}'])
        return log
      except ElementNotInteractableException:
        log.append([contador, 'No se puede interactuar con el elemento', f'{e}-{p}-{r}'])
        return log
      except AttributeError:
        log.append([contador, 'Otro error ocurrió', f'{e}-{p}-{r}'])
        return log
  
    return log