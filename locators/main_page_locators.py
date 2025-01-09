from selenium.webdriver.common.by import By

class MainPageLocators:

    TOP_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and @class='Button_Button__ra12g']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")

    LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    LOGO_YANDEX = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

    QUESTIONS_AND_ANSWERS = [
        ((By.ID, "accordion__heading-0"), (By.XPATH, "//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')]")),
        ((By.ID, "accordion__heading-1"), (By.XPATH, "//p[contains(text(),'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')]")),
        ((By.ID, "accordion__heading-2"), (By.XPATH, "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')]")),
        ((By.ID, "accordion__heading-3"), (By.XPATH, "//p[contains(text(),'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')]")),
        ((By.ID, "accordion__heading-4"), (By.XPATH, "//p[contains(text(),'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')]")),
        ((By.ID, "accordion__heading-5"), (By.XPATH, "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')]")),
        ((By.ID, "accordion__heading-6"), (By.XPATH, "//p[contains(text(),'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')]")),
        ((By.ID, "accordion__heading-7"), (By.XPATH, "//p[contains(text(),'Да, обязательно. Всем самокатов! И Москве, и Московской области.')]")),
    ]