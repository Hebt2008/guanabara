from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# 1. Configurar o serviço do WebDriver (ajuste o caminho conforme necessário)
# Se o chromedriver estiver no PATH do sistema, Service() pode não ser necessário.
# Exemplo com caminho específico:
# service = Service(executable_path='/caminho/para/seu/chromedriver.exe')
# driver = webdriver.Chrome(service=service)

# Caso o driver esteja nas variáveis de ambiente do sistema (mais comum):
driver = webdriver.Chrome()


try:
    # 2. Abrir o site desejado
    driver.get("https://aternos.org/server/#google_vignette")
    print("Site aberto.")

    # Opcional: Aguardar um pouco para a página carregar completamente
    time.sleep(2)

    # 3. Encontrar o elemento (por exemplo, um link com o texto "More information...")
    # Inspecione o elemento no navegador para encontrar o seletor apropriado (ID, Name, Class Name, XPath, Link Text, etc.)
    # Neste exemplo, vamos simular a busca por um link.
    
    # Supondo que exista um link na página com o texto "More information..."
    # Se fosse um botão com ID="myButton", o código seria:
    # button = driver.find_element(By.ID, "myButton")

    link = driver.find_element(By.LINK_TEXT, "More information...")

    # 4. Clicar no elemento
    link.click()
    print("Elemento clicado.")

    # Opcional: Aguardar para ver o resultado do clique
    time.sleep(3)

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    # 5. Fechar o navegador no final
    driver.quit()
    print("Navegador fechado.")
