from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


#-------------------------------------------------------------------------------------------------------------
#element會用到的功能
class CustomTimeoutException(Exception):
    
    def __init__(self, message):
        super().__init__(message)

class Basepage:
    
    def __init__(self,driver):  
        self.driver = driver
          
    def find_ele_after_visible(self,xpath,ele_name,timelimit = 10):
        try:
            element = WebDriverWait(self.driver, timelimit).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    
            if element:
                return element
            element = WebDriverWait(self.driver, timelimit).until(EC.presence_of_element_located((By.XPATH, xpath)))
    
            if element:
                self.driver.execute_script('arguments[0].scrollIntoView({ block: "center", inline: "center" });', element)
                element = WebDriverWait(self.driver, timelimit).until(EC.visibility_of_element_located((By.XPATH, xpath)))
                return element
        except TimeoutException:
            raise CustomTimeoutException(f"Element [{ele_name}]was unvisiable within {timelimit} seconds.")
        

    def find_ele_after_clickable(self,xpath,ele_name,timelimit = 10):
        try:
            element = WebDriverWait(self.driver, timelimit).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    
            if element:
                return element
            element = WebDriverWait(self.driver, timelimit).until(EC.presence_of_element_located((By.XPATH, xpath)))
    
            if element:
                self.driver.execute_script('arguments[0].scrollIntoView({ block: "center", inline: "center" });', element)
                element = WebDriverWait(self.driver, timelimit).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                return element
        except TimeoutException:
            raise CustomTimeoutException(f"Element [{ele_name}]was unclickable within {timelimit} seconds.")
        
    def find_ele_after_presence(self,xpath,ele_name,timelimit = 10):
        try:
            element = WebDriverWait(self.driver, timelimit).until(EC.presence_of_element_located((By.XPATH, xpath)))

            if element:
                return element
        except TimeoutException:
            raise CustomTimeoutException(f"Element [{ele_name}]was not presence within {timelimit} seconds.")

     
 
#--------------------------------------------------------------------------------------------------------------------------------
#定位器
trello_page_locator = {  
    #輸入信箱的地方
    'input_email':'//*[@id="username"]',
    #輸入密碼的地方
    'input_password':'//*[@id="password"]',
    #提交帳號密碼
    'login_submit':'//*[@id="login-submit"]/span',
    #選擇工作區的菜單
    'workspace_switcher':'//*[contains(@data-testid,"workspace-switcher")]',
    #進入選擇的工作區
    'into_workspace':'//*[contains(@data-testid,"workspace-switcher-popover-tile")]//*[contains(normalize-space(),"{workspace_name}")]',
    #看板們
    'boards':'//*[contains(@class,"cZx7p8hAQGLEz5 l7ix_KdG4LuugK")]',
    #工作區進入看板的按鈕
    'workspace_into_board':'//*[contains(@title,"{board_name}")and contains(@class,"hPB1MFHtrhA_in")]',
    #看板旁邊三個點點的按鈕
    'board_overflow_menu':'//*[contains(@title,"{board_name}")]/following-sibling::*//*[contains(@data-testid,"OverflowMenuHorizontalIcon")]',
    #關閉或離開看板按鈕
    'close_board':'//*[contains(@data-testid,"ForwardIcon")]',
    #確認關閉看板按鈕
    'confirm_close_board':'//button[contains(@data-testid,"popover-close-board-confirm")]',
    #查看已關閉的看板
    'check_closed_board':'//footer[contains(@class,"vccO4XHqldnulB")]//button',
    #刪除面板
    'delete_board':'//*[contains(@class,"KIigWC5xzGtpZ7")and contains(normalize-space(),"{board_name}")]//button[contains(@data-testid,"close-board-delete-board-button")]',
    #確認刪除面板
    'delete_board_confirm':'//button[contains(@data-testid,"close-board-delete-board-confirm-button")]',
    #離開關閉看板展示頁面
    'leave_closed_board':'//button//*[contains(@data-testid,"CloseIcon")]',
    #創建看板按鈕
    'create_board_button':'//button[contains(@data-testid,"create-board-tile")]',
    #看板名稱輸入欄位
    'input_board_title':'//input[contains(@data-testid,"create-board-title-input")]',
    #確認創建看板按鈕
    'create_board_submit':'//button[contains(@data-testid,"create-board-submit-button")]',
    #創建列表按鈕
    'create_list_button':'//button[contains(@data-testid,"list-composer")]',
    #新列表名稱輸入欄位
    'new_listname_input':'//textarea[contains(@class,"oe8RymzptORQ7h")]',
    #確認創建列表
    'create_list_submit':'//button[contains(@data-testid,"list-composer-add")]',
    #列表三個點點按鈕
    'list_overflow_menu':'//*[contains(normalize-space(),"{list_name}")]/following-sibling::*//*[contains(@data-testid,"list-edit-menu-button")]',
    #列表封存按鈕
    'archive_list_button':'//button[contains(@data-testid,"list-actions-archive")]',
    #看板內右上角三個點點按鈕
    'overflow_menu_inboard':'//button[contains(@class,"GDunJzzgFqQY_3 frrHNIWnTojsww bxgKMAm3lq5BpA HAVwIqCeMHpVKh SEj5vUdI3VvxDc")]',
    #查看已封存的項目
    'check_archived':'//button//*[contains(@data-testid,"ArchiveIcon")]',
    #切換卡片/列表
    'archived-switcher':'//*[contains(@class,"n5zDRPNW0f6sNr bxgKMAm3lq5BpA SEj5vUdI3VvxDc")]',
    #刪除列表
    'delete_list':'//*[contains(normalize-space(),"{list_name}")]/following-sibling::*//*[contains(@data-testid,"TrashIcon")]',
    #確認刪除按鈕
    'delete_confirm':'//*[contains(@class,"ciZFdWIjoKjp4t bxgKMAm3lq5BpA KpU415sFFvOzGZ PnEv2xIWy3eSui SEj5vUdI3VvxDc")]',
    #新增卡片按鈕
    'create_card_button':'//*[contains(normalize-space(),"{list_name}")]/following-sibling::*//button[contains(@data-testid,"list-add")]',
    #新卡片名稱輸入欄位
    'new_cardname_input':'//textarea[contains(@data-testid,"list-card")]',
    #確認新增卡片
    'create_card_submit':'//button[contains(@data-testid,"list-card-composer-add")]',
    #快捷編輯卡片按鈕(滑鼠放上去才可見)
    'card-editor':'//*[contains(@data-testid,"trello-card")and contains(normalize-space(),"{card_name}")]//*[contains(@data-testid,"quick-card-editor-button")]',
    #卡片按鈕
    'card-button':'//*[contains(@data-testid,"trello-card")and contains(normalize-space(),"{card_name}")]',
    #封存卡片按鈕
    'card-archive-button':'//button[contains(@data-testid,"archive")]',
    #刪除卡片按鈕
    'card-delete-button':'//button[contains(@data-testid,"delete")]',
    #新增描述按鈕
    'add_description_button':'//button[contains(@class,"krMmYdD0ayf5Qo")]',
    #卡片描述輸入欄位
    'card_description_textarea':'//*[contains(@id,"ak")]',
    #儲存描述按鈕
    'description_save_button':'//*[contains(@data-testid,"description-save")]',
    #卡片描述的文字
    'card_description':'//*[contains(@class,"ak-renderer-doc")]',
    #新增checklist按鈕
    'create_checklist_button':'//button[contains(@data-testid,"checklist")]',
    #確認新增checklist
    'create_checklist_submit':'//button[contains(@class,"HwRbvTPVxzo9OE bxgKMAm3lq5BpA SEj5vUdI3VvxDc")]',
    #該死的跳出式菜單關閉按鈕
    'board_menu_close_button':'//button[contains(@data-testid,"board-menu-close-button")]'
    
}

#-------------------------------------------------------------------------------------------------------------------
#operator
class Operator(Basepage):
    
    def __init__(self,driver):
        super().__init__(driver)
        self.locator = trello_page_locator
    
    def click_button(self,element_name,**kwargs):
        xpath_template = self.locator[element_name]
        try:
            xpath = xpath_template.format(**kwargs)
        except:
            xpath = xpath_template
   
        button_to_click = self.find_ele_after_clickable(xpath, element_name)
        button_to_click.click()

    def send_keys_to_element(self,element_name,text_to_send,**kwargs):
        xpath_template = self.locator[element_name]
        try:
            xpath = xpath_template.format(**kwargs)
        except:
            xpath = xpath_template
        text_area = self.find_ele_after_visible(xpath,element_name)
        text_area.send_keys(text_to_send)
       
    def move_mouse_to_element(self,element_name,**kwargs):
        xpath_template = self.locator[element_name]
        try:
            xpath = xpath_template.format(**kwargs)
        except:
            xpath = xpath_template
        element = self.find_ele_after_presence(xpath,element_name)
        mouse = ActionChains(self.driver)
        mouse.move_to_element(element).perform()
    
    def check_element_existence(self, element_name,**kwargs):
        xpath_template = self.locator[element_name]
        try:
            xpath = xpath_template.format(**kwargs)
        except:
            xpath = xpath_template
        try:
            self.find_ele_after_presence(xpath, element_name)
            return True
        except CustomTimeoutException:
            return False
        
    def wait_element_visible(self,element_name,**kwargs):
        xpath_template = self.locator[element_name]
        try:
            xpath = xpath_template.format(**kwargs)
        except:
            xpath = xpath_template
        self.find_ele_after_visible(xpath,element_name)
        
        