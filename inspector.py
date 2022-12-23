from playwright.sync_api import sync_playwright
import os
import json 



def clear_cookies(cookies):
    for item in cookies:
        del item['sameSite']
    json.dump(cookies, open('static/state.json', 'w'), indent=4)



class Inspector():

    def __init__(self):

        
        self.commands = json.load(open('static/commands.json', 'r'))
        cookies = json.load(open('static/state.json', 'r'))
        self.saved_output = ' '
        self.output = ' '
        if self.commands.get('new_session'): # key value -> true/false
            clear_cookies(cookies) # only call it if the session is new 

        playwright = sync_playwright().start() 
        self.browser = playwright.webkit.launch(headless=True)
        self.context = self.browser.new_context(java_script_enabled=False)
        self.context.add_cookies(cookies)
        self.page = self.context.new_page()

        # sometimes playwright just cant access for no reason
        try:
            self.page.goto("https://glamorously-beautiful-iris-flat-dev.wayscript.cloud/")
        except:
            self.page.goto("https://glamorously-beautiful-iris-flat-dev.wayscript.cloud/")

    def check_output(self):
        #print(page.content())
        self.page.reload()
        temp_output = self.page.locator('textarea[id="output"]').text_content()
        
        if self.saved_output != temp_output:
            self.output = temp_output 

            for command in self.commands.get(self.output): # for each command line inside the list at key on commands dict  
                os.system(command)

            # assert self.saved_output == temp_output
        return self.output
        

    def loop(self):
        
        try:
            self.saved_output = self.check_output()
            # self.page.wait_for_timeout(100)
            self.loop() 

        except KeyboardInterrupt:
            raise '' 
            try:
                self.close()
            except:
                pass
        
    def close(self):# aperta agora
        self.context.close()
        self.browser.close()



if __name__ == "__main__":
    Inspector().loop()

