import csv
import os, re

#Rango para uso de los ciclos for
rangoA = range(220,230)

#Generar archivo para el caso de prueba CP001a
def generarCP001a(): 

    with open('values/values_cP001a.csv', 'w+', newline='') as file:

        writer = csv.writer(file)

        header = ['name', 'username', 'email', 'password']
        writer.writerow(header)

        for i in rangoA:

            name = f'namePrueba{i}'
            username = f'usernamePrueba{i}'
            email = f'casoprueba{i}@software.com'
            password = 'PruebaTuCan'

            writer.writerow([name, username, email, password])

#Generar archivo para el caso de prueba CP001b
def generarCP001b():

    with open('values/values_cP001b.csv', 'w+', newline='') as file:

        writer = csv.writer(file)

        header = ['name', 'username', 'email', 'password']
        writer.writerow(header)

        for i in rangoA:

            name = f'namePrueba{i}'
            username = f'usernamePrueba{i}'
            email = f'casoprueba{i}@software.com'
            password = 'PruebaTuCan'

            writer.writerow([name, username, email, password])

#Generar archivo para el caso de prueba CP002a
def generarCP002a():

    with open('values/values_cP002a.csv', 'w+', newline='') as file:

        writer = csv.writer(file)

        header = ['email', 'password']
        writer.writerow(header)

        for i in rangoA:

            email = f'casoprueba{i}@software.com'
            password = 'PruebaTuCan'

            writer.writerow([email, password])

#Generar archivo para el caso de prueba CP002b
def generarCP002b():

    with open('values/values_cP002b.csv', 'w+', newline='') as file:

        writer = csv.writer(file)

        header = ['email', 'password']
        writer.writerow(header)

        for i in rangoA:

            email = f'casonoexiste{i}@software.com'
            password = 'PruebaTuCan'

            writer.writerow([email, password])

#Generar archivo para el caso de prueba CP003a
def generarCP003a():

    with open('values/values_cP003a.csv', 'w+', newline='') as file:

        writer = csv.writer(file)

        header = ['email', 'password', 'text']
        writer.writerow(header)

        for i in rangoA:

            email = f'casoprueba{i}@software.com'
            password = 'PruebaTuCan'
            text = f'Un caso de prueba para ingenieria de software III Chrome {i}'

            writer.writerow([email, password, text])

#Generar archivo para el caso de prueba CP003b
def generarCP003b():

    with open('values/values_cP003b.csv', 'w+', newline='') as file:

        writer = csv.writer(file)

        header = ['email', 'password', 'text']
        writer.writerow(header)

        for i in rangoA:

            email = f'casoprueba{i}@software.com'
            password = 'PruebaTuCan'

            writer.writerow([email, password, ''])

#Generar archivo para el caso de prueba CP004a
def generarCP004a():

    with open('values/values_cP004a.csv', 'w+', newline='') as file:

        writer = csv.writer(file)

        header = ['email', 'password', 'username']
        writer.writerow(header)

        for i in rangoA:

            email = f'casoprueba{i}@software.com'
            password = 'PruebaTuCan'
            username = f'cambioUser{i}'

            writer.writerow([email, password, username])

#Generar archivo para el caso de prueba CP004b
def generarCP004b():

    with open('values/values_cP004b.csv', 'w+', newline='') as file:

        writer = csv.writer(file)

        header = ['email', 'password', 'username']
        writer.writerow(header)

        for i in rangoA:

            email = f'casoprueba{i}@software.com'
            password = 'PruebaTuCan'
            username = f'pruebasoftware3'

            writer.writerow([email, password, username])

#Generar archivo para el caso de prueba CP005a
def generarCP005a():

    with open('values/values_cP005a.csv', 'w+', newline='') as file:

        writer = csv.writer(file)

        header = ['email', 'password', 'route']
        writer.writerow(header)

        directorio = os.path.abspath("media/5a.png").replace('\\', '/')

        for i in rangoA:

            email = f'casoprueba{i}@software.com'
            password = 'PruebaTuCan'
            route = f'{directorio}'

            writer.writerow([email, password, route])

#Generar archivo para el caso de prueba CP005b
def generarCP005b():

    with open('values/values_cP005b.csv', 'w+', newline='') as file:

        writer = csv.writer(file)

        header = ['email', 'password', 'route']
        writer.writerow(header)

        directorio = os.path.abspath("media/5b.txt").replace('\\', '/')

        for i in rangoA:

            email = f'casoprueba{i}@software.com'
            password = 'PruebaTuCan'
            route = f'{directorio}'

            writer.writerow([email, password, route])

#Generar archivo para el caso de prueba CP006a
def generarCP006a():

    with open('values/values_cP006a.csv', 'w+', newline='') as file:

        writer = csv.writer(file)

        header = ['email', 'password', 'new']
        writer.writerow(header)

        for i in rangoA:

            email = f'casoprueba{i}@software.com'
            password = 'PruebaTuCan'
            new = f'NuevaTuCan'

            writer.writerow([email, password, new])

#Generar archivo para el caso de prueba CP006b
def generarCP006b():

    with open('values/values_cP006b.csv', 'w+', newline='') as file:

        writer = csv.writer(file)

        header = ['email', 'password', 'new']
        writer.writerow(header)

        for i in rangoA:

            email = f'casoprueba{i}@software.com'
            password = 'NuevaTuCan'
            new = f'Nue'

            writer.writerow([email, password, new])

#Para ejecutarlas todas
def generarTodos():
    generarCP001a() ; generarCP001b()
    generarCP002a() ; generarCP002b()
    generarCP003a() ; generarCP003b()
    generarCP004a() ; generarCP004b()
    generarCP005a() ; generarCP005b()
    generarCP006a() ; generarCP006b()

     
#Match case para generar los CSV
def main(casoGenerar):
    match casoGenerar:
        case 1: generarCP001a()
        case 2: generarCP001b()
        case 3: generarCP002a()
        case 4: generarCP002b()
        case 5: generarCP003a()
        case 6: generarCP003b()
        case 7: generarCP004a()
        case 8: generarCP004b()
        case 9: generarCP005a()
        case 10: generarCP005b()
        case 11: generarCP006a()
        case 12: generarCP006b()
        case 13: generarTodos()
        case _: print("Error en la ejecución")