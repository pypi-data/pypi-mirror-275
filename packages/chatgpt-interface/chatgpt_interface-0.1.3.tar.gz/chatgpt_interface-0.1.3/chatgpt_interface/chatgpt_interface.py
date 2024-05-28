import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class ChatGPTInterface:
    def __init__(self, profile_path, chat_url, prompts):
        self.profile_path = profile_path
        self.chat_url = chat_url
        self.prompts = prompts

        if not os.path.exists(self.profile_path):
            raise FileNotFoundError(f"Profile directory does not exist at {self.profile_path}")

        chrome_options = Options()
        chrome_options.add_argument(f"user-data-dir={self.profile_path}")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--lang=en-US")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--auto-open-devtools-for-tabs")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--disable-features=IsolateOrigins,site-per-process")
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument("--log-level=3")

        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def open_chat(self):
        self.driver.get(self.chat_url)
        self.check_login_button()

    def check_login_button(self):
        try:
            login_button = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='login-button']"))
            )
            if login_button:
                self.prompt_user_action("Login required. Perform login actions and press Enter to continue...")
        except:
            pass

    def prompt_user_action(self, message):
        print(message)
        input()

    def send_prompt(self, prompt):
        chat_input_box = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#prompt-textarea"))
        )
        chat_input_box.clear()

        for line in prompt.split('\n'):
            chat_input_box.send_keys(line)
            chat_input_box.send_keys(Keys.SHIFT, Keys.ENTER)
        
        chat_input_box.send_keys(Keys.RETURN)
        time.sleep(2)

    def get_response(self):
        wait_for_button = WebDriverWait(self.driver, 180)
        send_button = wait_for_button.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='fruitjuice-send-button']"))
        )
        
        response_box = wait_for_button.until(
            EC.presence_of_element_located((By.XPATH, "(//div[@data-message-author-role='assistant']//div[contains(@class, 'markdown')])[last()]"))
        )
        return response_box.get_attribute('innerHTML')

    def process_prompts(self):
        responses = []
        for prompt in self.prompts:
            self.send_prompt(prompt)
            response = self.get_response()
            responses.append((prompt, response))
            # print(response)
        return responses

    def save_profile(self):
        self.driver.quit()
        print(f"Profile saved at {self.profile_path}")
