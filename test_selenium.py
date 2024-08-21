from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configurar ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Abrir la página de Example.com
driver.get("https://example.com")

# Obtener el título de la página y verificar si contiene "Example Domain"
title = driver.title
if "Example Domain" in title:
    print("Test Passed: The title is correct!")
else:
    print("Test Failed: The title is incorrect.")

# Mantener la ventana abierta para que puedas verla
input("Press Enter to close the browser...")

# Cerrar el navegador
driver.quit()
