from pages.pagesJejak import PagesJejak
from utils.setup import SetupDriver
import pytest

@pytest.fixture(scope="function")
def driver():
    setup_driver = SetupDriver()
    yield setup_driver.driver
    setup_driver.driver.quit()

# positif case
def test_successPaymentOVO(driver):
    jejak = PagesJejak(driver)
    jejak.openWebsite()
    jejak.clickFirstProgram()
    jejak.clickTanam()
    jejak.inputForm("baskaratimur", "baskaratimur99@gmail.com")
    jejak.clickFieldPayment()
    jejak.selectOvoMethod()
    jejak.clickBayar()
    jejak.inputPhoneOvo("08997771212")
    jejak.clickBayarToConfirm()
    assert jejak.assertMessageSuccess(), "Pembayaran Failed"

# negatif case
def test_emptyNameGoPayment(driver):
    jejak = PagesJejak(driver)
    jejak.openWebsite()
    jejak.clickFirstProgram()
    jejak.clickTanam()
    jejak.inputForm("", "baskaratimur99@gmail.com")
    jejak.clickFieldPayment()
    jejak.selectOvoMethod()
    assert jejak.assertBayarDisabled()