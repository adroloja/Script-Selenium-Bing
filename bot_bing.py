import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#####################################################################################################################
#
#           SCRIPT QUE CONECTA CON BING Y HACE LOS RETOS Y LAS BUSQUEDAS DIARIAS PARA CONSEGUIR LA RECOMPENSA
#                                           AUTOR: ADRIAN J
#
#####################################################################################################################


url = 'https://rewards.bing.com/'

# Ruta a chromedriver atentto con las / tienen que ser asi, por defecto el enlace del explorador te los pondra del reves
path_chromedriver = ''

#####################################################################################################################
#
#                                       FUNCION QUE DEVUELVE EL DRIVER
#
#####################################################################################################################


def run_bot():

    # Configurando las opciones

    options = webdriver.ChromeOptions()

    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-site-isolation-trials")
    options.add_argument("--accept-ssl-certs")


    #Carga el driver    
    driver = webdriver.Chrome(path_chromedriver, options=options)
    
    #URL
    driver.get(url)   
    sleep(4.5)
   

    return driver

#####################################################################################################################
#
#                                       FUNCION QUE HACE LOGIN
#
#####################################################################################################################


def login(driver):

    # Aqui introduce tu email de microsoft bing"
    email = ''

    # Aquí introduce la contraseña
    pass_bing = ''

    email_text = driver.find_element(By.XPATH, '//input[@type="email"]')
    email_text.send_keys(email)

    sleep(1.5)

    boton_aceptar = driver.find_element(By.XPATH, '//input[@type="submit"]')
    boton_aceptar.click()

    sleep(3)

    pass_text = driver.find_element(By.XPATH, '//input[@type="password"]')
    pass_text.send_keys(pass_bing)

    sleep(2.3)

    boton_aceptar = driver.find_element(By.XPATH, '//input[@type="submit"]')
    boton_aceptar.click()

    sleep(3.4)

    boton_aceptar = driver.find_element(By.XPATH, '//input[@type="submit"]')
    boton_aceptar.click()

#####################################################################################################################
#
#                                  FUNCION QUE SE ENCARGA DE HACER LAS BUSQUEDAS DIARIAS
#
#####################################################################################################################

def hacer_busquedas(driver):

    lista_busquedas = ['marca', 'python' 'league of legend', 'elmundo', 'musica', 'curso blockchain', 'chatgpt', 'ropa', 'motos', 'youtube',
                       'futbol', 'clasificacion de la liga', 'calendario champions league', 'mario roman', 'marc marquez', 'graham jarvis',
                       'viaje al caribe', 'numeros en ingles', 'aviones' , 'vuelos a italia', 'vuelos a portugal', 'hotel en andorra',
                       'mejor cerveza 2023', 'mejor futbolista 2022', 'mejor deportista de todos los tiempos', 'receta paella', 'receta fabada asturiana'
                       'donde comer la mejor pizza', 'que es mas sano la cerveza o el vino', 'apartamento en Conil']

    sleep(1.1)

    driver.execute_script("window.open('https://www.bing.com/')")

    sleep(2.1)

    ventanas = driver.window_handles 

    driver.switch_to.window(ventanas[1])

    boton_aceptar_cookie = driver.find_element(By.XPATH, '//a[text()="Aceptar"]')
    boton_aceptar_cookie.click()

    for busqueda in lista_busquedas:

        numero_random = (random.randrange(1,10)/10)

        sleep(0.3 + numero_random)

        cuadro_texto = driver.find_element(By.XPATH, '//textarea[1]')
        cuadro_texto.send_keys("%s \ue007" % busqueda)

        sleep(1 + numero_random)

        driver.back()

    driver.close()

#####################################################################################################################
#
#                                      FUNCION QUE SE ENCARGA DE PINCHAR EN LOS LINKS
#
##################################################################################################################### 

def almacenar_y_pinchar(driver):

    indice = 1

    sleep(4.1)
    
    enlaces = driver.find_elements(By.XPATH, '//div[@class="c-card-content"]')

    print(len(enlaces))

    for enlace in enlaces:

        sleep(1.2)

        try:

            hiper = enlace.find_elements(By.XPATH, './/a[1]')
            driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})',enlace)
            
            sleep(2.1)

            enlace.click()

            sleep(2)

            ventanas = driver.window_handles 
            driver.switch_to.window(ventanas[1])

        except:

            continue 
        
        if indice == 1:
            boton_aceptar_cookie = driver.find_element(By.XPATH, '//a[text()="Aceptar"]')
            boton_aceptar_cookie.click()
        
        indice += 1
        print(indice)
        sleep(1.2)

        driver.close()

        driver.switch_to.window(ventanas[0])
        

#####################################################################################################################
#
#                                       AQUI EMPIEZA EL CONTROL DE TODO EL CODIGO
#
#####################################################################################################################

driver = run_bot()
login(driver)
almacenar_y_pinchar(driver)
#hacer_busquedas(driver)




