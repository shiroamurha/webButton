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
        self.cookies = json.load(open('static/state.json', 'r'))
        self.saved_output = ' '
        self.output = ' '
        if self.commands.get('new_session'): # key value -> true/false
            clear_cookies(self.cookies) # only call it if the session is new 


    def start(self):

        self.playwright = sync_playwright().start() 
        self.browser = self.playwright.webkit.launch(headless=True)
        self.context = self.browser.new_context(java_script_enabled=False)
        self.context.add_cookies(self.cookies)
        self.page = self.context.new_page()

        # sometimes playwright just cant access for no reason
        try:
            self.page.goto("https://glamorously-beautiful-iris-flat-dev.wayscript.cloud/")
        except:
            self.page.goto("https://glamorously-beautiful-iris-flat-dev.wayscript.cloud/")
        finally:
            self.saved_output = self.page.locator('textarea[id="output"]').text_content()

    def check_output(self):
        #print(page.content())
        self.page.reload()
        self.output_raised = False
        temp_output = self.page.locator('textarea[id="output"]').text_content()
        
        # if self.saved_output is not temp_output:
        self.output = temp_output 
        
        
        if self.commands.get(self.output) != '' and self.commands.get(self.output) != ' ' and self.commands.get(self.output) is not None:
            self.output_raised = True
            for command in self.commands.get(self.output): # for each command line inside the list at key on commands dict  
                os.system(command)

        # assert self.saved_output == temp_output
        return self.output
        

    def loop(self):
        
        try:
            self.saved_output = self.check_output()
            # self.page.wait_for_timeout(100)
            if self.output_raised:
                return self.output

        except (KeyboardInterrupt, ValueError):
            pass
    
    def get_commands(self):
        return self.commands
    
    def update_commands(self, commands):
        self.commands = commands
        json.dump(commands, open('static/commands.json', 'w'), indent=4)

    def close(self):# aperta agora

        try:
            self.page.close()
        except:
            pass
        try:
            self.context.close()
        except:
            pass

        try:
            self.browser.close()
        except:
            pass
        
        try:
            self.playwright.dispose()
        except:
            pass


i = 0
if __name__ == "__main__":
    a = Inspector()
    a.start()
    while i==0:
        print(a.loop())
        i = int(input(' - '))

