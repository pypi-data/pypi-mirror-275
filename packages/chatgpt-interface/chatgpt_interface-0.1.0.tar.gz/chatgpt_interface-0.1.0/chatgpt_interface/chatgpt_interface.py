from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ChatGPTInterface:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.wait = WebDriverWait(self.driver, 10)

    def open_chat(self, url):
        self.driver.get(url)

    def send_prompt(self, prompt):
        chat_input_box = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))  # Замените селектор на нужный
        )
        chat_input_box.clear()
        chat_input_box.send_keys(prompt)
        chat_input_box.send_keys(Keys.RETURN)

    def get_response(self):
        response_box = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.response"))  # Замените селектор на нужный
        )
        return response_box.get_attribute('innerHTML')

    def close(self):
        self.driver.quit()
