from django.test import TestCase

        #==========Login testing starts==========

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from django.test import LiveServerTestCase

# class LoginTest(LiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.driver = webdriver.Chrome()
#         cls.driver.get(cls.live_server_url + "/login.html")
#         cls.driver.maximize_window()

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#         super().tearDownClass()

#     def test_login_successful(self):
#         wait = WebDriverWait(self.driver, 20)  # Adjust timeout as needed

#         # Wait for the username input field
#         username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
#         password_input = self.driver.find_element(By.NAME, "password")

#         # Input username and password
#         username_input.send_keys("neha")
#         password_input.send_keys("Neha@123")

#         # Wait for the login button to be clickable
#         login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
#         login_button.click()

#         # Redirect to the dashboard URL after successful login
#         dashboard_url = self.live_server_url + "/dashboard"
#         self.driver.get(dashboard_url)

            #==========Login testing ends==========    



# from django.urls import reverse
# from home.models import CustomUser  # Import your CustomUser model

# class YourTest(TestCase):
#     def setUp(self):
#         # Create a custom user
#         self.user = CustomUser.objects.create_user(
#             username='admin', email='admin@gmail.com', password='Ajce24@mca')

#     def test_login(self):
#         # Attempt to log in
#         login_url = reverse('login')  # Replace with your login URL name
#         data = {'username': 'admin', 'password': 'Ajce24@mca'}
#         response = self.client.post(login_url, data)
        
#         # Check if login was successful (you might have different response codes or redirects)
#         self.assertEqual(response.status_code, 200)  # Replace 200 with the expected status code

#     def test_add_product(self):
#         # Assuming authenticated user, add a product
#         add_product_url = reverse('addequip')  # Replace with your add product URL name
#         data = {
#             'name': 'Product Name',
#             'rating': 5,
#             'description': 'Product Description',
#             # Add other required fields as needed
#         }
        
#         # Log in the user first
#         self.client.login(username='admin', password='Ajce24@mca')
#         response = self.client.post(add_product_url, data)
        
#         # Check if adding product was successful (add appropriate checks)
#         self.assertEqual(response.status_code, 200)  # Replace 200 with the expected status code

#     def test_view_equipments(self):
#         # Assuming authenticated user, attempt to view equipments
#         view_equip_url = reverse('view_equip')  # Replace with your view equipments URL name
        
#         # Log in the user first
#         self.client.login(username='admin', password='Ajce24@mca')
#         response = self.client.get(view_equip_url)
        
#         # Check if viewing equipments was successful (add appropriate checks)
#         self.assertEqual(response.status_code, 200)  # Replace 200 with the expected status code


# from django.test import TestCase
# from django.urls import reverse
# from home.models import CustomUser  # Import your CustomUser model

# class YourTest(TestCase):
#     # def setUp(self):
#     #     # Create a custom user
#     #     self.user = CustomUser.objects.create_user(
#     #         username='admin', email='admin@gmail.com', password='Ajce24@mca')

#     def test_login_then_add_product_then_view_equip(self):
#         # Attempt to log in
#         login_url = reverse('login')  # Replace with your login URL name
#         data = {'username': 'admin', 'password': 'Ajce24@mca'}
#         response = self.client.post(login_url, data, follow=True)

#         # Check if login was successful
#         self.assertEqual(response.status_code, 200)  # Expecting a successful login

#         # Follow the redirects to find the final URL
#         final_url = response.request.get("PATH_INFO", "")  # Fetch the final URL after redirects

#         # Now, add a product
#         add_product_url = reverse('addequip')  # Replace with your add product URL name
#         product_data = {
#             'name': 'Speakers',
#             'rating': 5,
#             'description': 'HP Speakers',
            
#         }
#         add_product_response = self.client.post(add_product_url, product_data, follow=True)

#         # Check if adding product was successful
#         self.assertEqual(add_product_response.status_code, 200)  # Expecting a successful page load

#         # Check if the viewequip.html page is loaded successfully
#         view_equip_url = reverse('view_equip')  # Replace with your viewequip URL name
#         view_equip_response = self.client.get(view_equip_url)

#         # Check if viewing equipments was successful
#         self.assertEqual(view_equip_response.status_code, 200)  # Expecting a successful page load

                    

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from django.test import LiveServerTestCase

# class LoginTest(LiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.driver = webdriver.Chrome()
#         cls.driver.maximize_window()

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#         super().tearDownClass()

#     def test_login_successful_and_search_product(self):
#         driver = self.driver
#         wait = WebDriverWait(driver, 20)

#         driver.get(self.live_server_url + "/login.html")

#         # Perform login actions
#         username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
#         password_input = driver.find_element(By.NAME, "password")

#         username_input.send_keys("neha")
#         password_input.send_keys("Neha@123")

#         login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
#         login_button.click()

#         # Wait for successful login and navigate to the dashboard
#         dashboard_url = self.live_server_url + "/dashboard"
#         driver.get(dashboard_url)
#         # Navigate to the product page
#         product_url = self.live_server_url + "/product"
#         driver.get(product_url)

#         # Wait for the product page to load
#         wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'box')]")))

#         # Find and click the 'Rent Now' button for the Excavator product
#         excavator_rent_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//h5[contains(text(), 'Excavator')]/following-sibling::div[@class='option_container']//a[contains(@class, 'option2')]")))
#         excavator_rent_button.click()

#         # Wait for the 'Moving Equip' page to load
#         wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='movingequip_content']")))

#         # Get the URL of the 'Moving Equip' page after clicking 'Rent Now'
#         moving_equip_url = driver.current_url

#         # Navigate to the 'Moving Equip' page
#         driver.get(moving_equip_url)



      

           #==========Search Product starts========

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from django.test import LiveServerTestCase
# from selenium.common.exceptions import StaleElementReferenceException

# class LoginTest(LiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.driver = webdriver.Chrome()
#         cls.driver.maximize_window()

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#         super().tearDownClass()

#     def test_login_successful_and_search_product(self):
#         driver = self.driver
#         wait = WebDriverWait(driver, 20)

#         driver.get(self.live_server_url + "/login.html")

#         # Perform login actions
#         username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
#         password_input = driver.find_element(By.NAME, "password")

#         username_input.send_keys("neha")
#         password_input.send_keys("Neha@123")

#         login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
#         login_button.click()

#         # Wait for successful login
#         dashboard_url = self.live_server_url + "/dashboard"
#         driver.get(dashboard_url) 

#         # Navigate to the product search page
#         driver.get(self.live_server_url + "/search_blog?csrfmiddlewaretoken=m00rTjelqKHY8QIrrYZwkb13bNJcumfNTP7lPwKiochzwGeH4Nf3Vbd8MXMAi0wL&q=Excavator")

#         # Wait for search results on the search result page
#         wait.until(EC.presence_of_element_located((By.CLASS_NAME, "container")))

#         # Capture and print the search results
#         search_results = driver.find_elements(By.CLASS_NAME, "container")
#         for result in search_results:
#             print(result.text)

                        #==========Search Product ends========


#==========================Profile update========================
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from django.test import LiveServerTestCase

# class LoginTest(LiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.driver = webdriver.Chrome()
#         cls.driver.maximize_window()

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#         super().tearDownClass()

#     def test_login_successful(self):
#         self.driver.get(self.live_server_url + "/login.html")

#         wait = WebDriverWait(self.driver, 20)  # Adjust timeout as needed

#         # Wait for the username input field
#         username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
#         password_input = self.driver.find_element(By.NAME, "password")

#         # Input username and password
#         username_input.send_keys("neha")
#         password_input.send_keys("Neha@123")

#         # Wait for the login button to be clickable
#         login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
#         login_button.click()

#         # Redirect to the dashboard URL after successful login
#         dashboard_url = self.live_server_url + "/dashboard"
#         self.driver.get(dashboard_url)

#         # Select 'Account' in the dropdown
#         account_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "account-dropdown")))
#         account_dropdown.click()

#         # Select 'User Profile' from the dropdown
#         user_profile_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='User Profile']")))
#         user_profile_option.click()

#         # Wait for the profile page to load
#         wait.until(EC.presence_of_element_located((By.ID, "first-name")))

#         # Change the first name
#         first_name_input = self.driver.find_element(By.ID, "first-name")
#         first_name_input.clear()
#         first_name_input.send_keys("NewFirstName")

#         # Click on the Save Changes button
#         save_changes_button = self.driver.find_element(By.ID, "save-button")
#         save_changes_button.click()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginAndAddTechnicianTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_login_and_add_technician(self):
        driver = self.driver
        wait = WebDriverWait(driver, 50)

        # Open the login page
        driver.get("http://127.0.0.1:3000/login.html")

        # Enter username and password
        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = driver.find_element(By.NAME, "password")

        username_input.send_keys("arya")
        password_input.send_keys("Arya@123")

        # Click the login button
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
        login_button.click()

        # Wait for successful login and navigation to the dashboard page
        time.sleep(2)  # Adding delay for visibility
        driver.get("http://127.0.0.1:3000/dashboardOrg")

        # Navigate to add_technician.html page
        time.sleep(2)  # Adding delay for visibility
        driver.get("http://127.0.0.1:3000/add_technician/")

        # Wait for the add technician page to load
        time.sleep(2)  # Adding delay for visibility
        wait.until(EC.url_to_be("http://127.0.0.1:3000/add_technician/"))

        # Assert that the correct page has been loaded
        time.sleep(2)  # Adding delay for visibility
        self.assertEqual(driver.current_url, "http://127.0.0.1:3000/add_technician/")

        # Now you can continue with the test steps for the add technician page
        # Fill in the technician information
        name_input = driver.find_element(By.ID, "name")
        phone_number_input = driver.find_element(By.ID, "phone_number")
        expertise_input = driver.find_element(By.ID, "expertise")
        email_input = driver.find_element(By.ID, "email")
        address_input = driver.find_element(By.ID, "address")

        name_input.send_keys("John")
        time.sleep(1)  # Adding delay for visibility
        phone_number_input.send_keys("7902446778")
        time.sleep(1)  # Adding delay for visibility
        expertise_input.send_keys("Electronics")
        time.sleep(1)  # Adding delay for visibility
        email_input.send_keys("johndoe@gmail.com")
        time.sleep(1)  # Adding delay for visibility
        address_input.send_keys("123 Main Street")
        time.sleep(1)  # Adding delay for visibility

        # Submit the form
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        time.sleep(2)  # Adding delay for visibility
        submit_button.click()

        # Wait for the view technicians page to load and navigate to it
        time.sleep(2)  # Adding delay for visibility
        driver.get("http://127.0.0.1:3000/view_technicians/")
        wait.until(EC.url_to_be("http://127.0.0.1:3000/view_technicians/"))

