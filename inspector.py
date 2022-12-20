from playwright.sync_api import sync_playwright, Error
import json 



def clear_cookies(cookies):
    for item in cookies:
        del item['sameSite']
    json.dump(cookies, open('static/state.json', 'w'), indent=4)



class Inspector():

    def __init__(self, new_session):

        cookies = json.load(open('static/state.json', 'r'))
        if new_session:
            clear_cookies(cookies) # only call it if the session is new 

        playwright = sync_playwright().start() 
        self.browser = playwright.webkit.launch(headless=True)
        self.context = self.browser.new_context(java_script_enabled=False)
        self.context.add_cookies(cookies)
        self.page = self.context.new_page()
        self.page.goto("https://glamorously-beautiful-iris-flat-dev.wayscript.cloud/")

    def check_output(self):
        #print(page.content())
        self.page.reload()
        output = self.page.locator('textarea[id="output"]').text_content()
        return output
        

    def loop(self):
        
        try:
            print(self.check_output())
            self.page.wait_for_timeout(100)
            self.loop() 

        except KeyboardInterrupt:
            raise KeyboardInterrupt
            self.close()
        
    def close(self):# aperta agora
        self.context.close()
        self.browser.close()



if __name__ == "__main__":
    Inspector(new_session=False).loop()

