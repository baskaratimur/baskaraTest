from object.objectJejak import ObjectJejak
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PagesJejak:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.jejak = ObjectJejak()

    def openWebsite(self):
        self.driver.get("https://3pp-ioh.jejakin.dev/")

    def clickFirstProgram(self):
        firstProgram = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.jejak.dataFirstProgram)))
        self.driver.execute_script("arguments[0].scrollIntoView();", firstProgram)
        firstProgram.click()

    def clickTanam(self):
        # page load
        time.sleep(3)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.jejak.clickTanam))).click()

    def inputForm(self, name, email):
        # load form
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.jejak.fieldName))).send_keys(name)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.jejak.fieldEmail))).send_keys(email)

    def clickFieldPayment(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.jejak.selectMethod))).click()

    def selectOvoMethod(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.jejak.ovoMethod))).click()

    def clickBayar(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.jejak.clickBayar))).click()
 
    def clickBayarToConfirm(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.jejak.clickBayar))).click()
        # load page after payment 
        time.sleep(5)

    def loadSuccessPayment(self):
        # page load
        time.sleep(3)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.jejak.messageSuccess)))

    def inputPhoneOvo(self, phone):
        #  load modal
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.jejak.fieldPhoneOvo))).send_keys(phone)

    def assertMessageSuccess(self):
        try:
            elementMessageSuccess = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.jejak.messageSuccess)))
            textMessageSuccess = elementMessageSuccess.text
            print(textMessageSuccess)
            return  "Pembayaran berhasil" in textMessageSuccess 
        except:
            return False
       
    
    def assertBayarDisabled(self):
        try:
            elementButtonBayar = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.jejak.clickBayar)))
            attributeButtonBayar = elementButtonBayar.get_attribute("disabled")
            return attributeButtonBayar == "true"
        except:
            return False
            