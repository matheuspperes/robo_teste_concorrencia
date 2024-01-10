from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServiceChrome
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import asyncio


##CONTROLLER
class Controller:
    def __init__(self) -> None:
        self.lista_parcial_contratos = []
    
    def start(self, req):
        data = req.json
        
        print(data.get('import_id'))
        instances = data.get('instances')
        
        for param in data:
            if data[param] == '' or data[param] == None:
                return {'status': 401, 'message': f'Parâmetro "{param}" inexistente'}, 401
        
        print("Logins: ", instances)
        print("Import ID: : ", data['import_id'])
        
        browsers = []
        for user in instances:
            browser = self.open_browsers(user)
            browsers.append(browser)
            if not browser:
                continue
        
        try:
            while True:
                # requisição buscando contratos
                # payload = {"limit": len(instances), "secret_key": "fc521c77-bf8e-461c-bcd4-ecfe4161a346"}
                # items = requests.get(url='', data=payload)
                
                items = [{"id": 1,"site": "https://www.youtube.com/"}, {"id": 2,"site": "https://www.python.org/"}, {"id": 3,"site": "https://www.mongodb.com/"}]
                self.lista_parcial_contratos = items
                
                
                asyncio.run(self.tasks(len(instances), browsers))
                self.lista_parcial_contratos = []
                break
        
            return
        
        except Exception as e:
            print("exception ", e)
            return
             
    def tasks(self, num_instances, browsers):
        # Launch 3 browser instances
        
        # Open each URL in a different browser instance
        tasks = []
        for index in range(num_instances):
            task = asyncio.create_task(self.start_robot(browsers[index], self.lista_parcial_contratos[index]))
            tasks.append(task)
            self.start_robot(browsers[index], self.lista_parcial_contratos[index])
                            
    def open_browsers(self, user):
        service_chrome = ServiceChrome(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service_chrome)
        print(user)
        driver.maximize_window()
        driver.get("https://vuejs.org/")
        
        return driver
        
    def start_robot(self, driver, contract):                    
        driver.get(contract['site'])
        driver.get("https://vuejs.org/")
        sleep(5)
        return {"error": True, "type": "", "data": ""}
    