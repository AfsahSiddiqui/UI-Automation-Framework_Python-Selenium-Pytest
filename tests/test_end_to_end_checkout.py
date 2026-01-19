from utils import config
from utils.driver_utilities import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage


def test_complete_flow():
    driver = get_driver(config.BROWSER)
    driver.get(config.URL)

    login = LoginPage(driver)
    creds = config.CREDENTIALS
    login.login(creds["username"], creds["password"])

    inventory = InventoryPage(driver)
    inventory.add_product_to_cart("Bike Light")

    inventory.remove_product_from_cart("T-Shirt (Red)")

    inventory.see_product_page("Onesie") 
    
    Onesie_Page = ProductPage(driver)

    Onesie_Page.add_to_cart()
    Onesie_Page.go_to_cart()

    cart = CartPage(driver)
    cart.remove_product("Onesie")

    cart.continue_shopping()

    inventory.add_product_to_cart("Fleece Jacket")
    inventory.add_product_to_cart("Bolt T-Shirt")

    inventory.go_to_cart()

    cart.proceed_to_checkout()
    
    checkout = CheckoutPage(driver)
    checkout.enter_details("abc","xyz","lemon")

    checkout.finish_checkout()

    checkout_completed = CheckoutCompletePage(driver)
    checkout_completed.get_success_message()


    driver.quit()
