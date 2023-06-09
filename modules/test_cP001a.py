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

#Registro de usuario nuevo
class TestCP001a():
    
    #Iniciar el driver
    def setup_method(self):
      self.driver = webdriver.Chrome()
      self.vars = {}
   
    #Pasos del caso de prueba
    def test_cP001a(self):

      directorio = os.path.abspath("./values/values_cP001a.csv").replace('\\', '/')
      data = pd.read_csv(directorio)
      contador = 0
      log = []
      url = "http://localhost:8080/twitter-clone/index.php"

      #Para cada dato en el archivo CSV
      for n, u, e, p in zip(data['name'], data['username'], data['email'], data['password']):
        
        contador += 1      

        self.driver.get(url)
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

        try:

          #Intenta cerrar sesión para seguir con el siguiente
          self.driver.refresh()
          self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()

          #Log para el caso de éxito
          log.append([
            contador,
            'Exitosa', 
            'Creacion de usuario exitosa', 
            f'{n}-{u}-{e}-{p}']
          )

        except NoSuchElementException:  

          #Log para el caso fallido
          log.append([
            contador,
            'Fallida', 
            'Creacion de usuario fallida', 
            f'{n}-{u}-{e}-{p}']
          )

          continue             

      return log
    

    #Escritura de los resultados en CSV
    def escribirResultado():

      nuevaInstancia = TestCP001a()
      nuevaInstancia.setup_method()
      ejecucion = nuevaInstancia.test_cP001a()

      with open('./results/result_cp001a.csv', 'w+', newline='') as file:
        
        writer = csv.writer(file)
        writer.writerow(['Ejecucion', 'Resultado', 'Detalle', 'DatosUsados'])

        for i in ejecucion:
          writer.writerow([i[0], i[1], i[2], i[3]])