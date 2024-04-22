class ObjectJejak:
    def __init__(self):
        self.dataFirstProgram = "(//div[@id='program-list']//a)[1]"
        self.clickTanam = "//button[.//span[text()= 'Tanam']]"
        self.fieldName = "//input[@id='name']"
        self.fieldEmail = "//input[@id='email']"
        self.fieldPhoneOvo = "//input[@name='ovoPhoneNumber']"
        self.errorMessageEmptyName = "//span[text()='Nama minimum 3 karakter']"
        self.messageSuccess = "//div[text()='Pembayaran berhasil']"
        self.selectMethod = "//label[text()='Pilih Metode Pembayaran']"
        self.ovoMethod = "//img[@alt='ovo']"
        self.clickBayar = "//button[.//span[text()='Bayar']]"
