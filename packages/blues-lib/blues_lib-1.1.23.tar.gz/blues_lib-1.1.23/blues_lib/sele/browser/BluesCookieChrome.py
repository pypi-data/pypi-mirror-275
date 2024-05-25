
import sys,os,re,time
from .BluesChrome import BluesChrome

sys.path.append(re.sub('blues_lib.*','blues_lib',os.path.realpath(__file__)))
from util.BluesFiler import BluesFiler  
from util.BluesURL import BluesURL   
from util.BluesConsole import BluesConsole   
from util.BluesPowerShell import BluesPowerShell    
from config.BluesConfig import BluesConfig    

class BluesCookieChrome(BluesChrome):

  def __init__(self,config={},arguments={},experimental_options={}):
    self.loginer_executor = BluesPowerShell.get_env_value('LOGINER_EXECUTOR')
    self.relogin_time = 1
    super().__init__(config,arguments,experimental_options)

    
  def after_created(self):
    self.config['url'] = self.config.get('login_url') # 使用superclass访问 url属性逻辑
    super().after_created()
    # open home page with cookie
    self.add_cookie_file_and_browse()

  '''
  @description : support to login by default cookie
  '''
  def add_cookie_and_browse(self,url,cookies=''):
    '''
    @description : get a page afater add cookies
    @param {dict|str} cookies
    '''
    if cookies:
      self.action.cookie.add_cookies(cookies) 
    self.driver.get(url)

  def add_cookie_file_and_browse(self):
    login_url = self.config.get('login_url')
    loggedin_url = self.config.get('loggedin_url')
    cookie_file = self.config.get('cookie_file')
    login_selector = self.config.get('login_selector')

    default_file = BluesConfig.get_download_http_domain_file(self.driver.current_url,'txt')
    file_path = cookie_file if cookie_file else default_file
    if file_path:
      cookies = BluesFiler.read(file_path)
    else:
      cookies = ''
    self.add_cookie_and_browse(loggedin_url,cookies)
    
    is_login = self.is_login(login_selector)
    if is_login:
      BluesConsole.success('The cookie in file %s is still valid. Logged in %s successfully' % (file_path,loggedin_url))
      return 
    BluesConsole.success('The cookie in file %s is invalid. Relogin %s now' % (file_path,login_url))

    if not self.loginer_executor:
      BluesConsole.error('The env variable LOGINER_EXECUTOR is missing!')   
      self.quit() # close the browser
      return 

    if self.relogin_time>0:
      BluesConsole.warn('Relogin failure, and you can only re-log in once')
      self.quit() # close the browser
      return

    result = self.relogin()
    if result['code'] == 200:
      BluesConsole.success('The site (%s) relogin successfully' % loggedin_url)
      # reopen the page
      self.add_cookie_and_browse_file() 

    else:
      BluesConsole.error('The site (%s) relogin failure: %s,%s' % (loggedin_url,result['message'],result['output']))


  def is_login(self,login_selector,wait_time=3):
    '''
    @description : is login or not
    @param {str} login_selector : the css selector of a element in login page
    @param {int} wait_time : wait n seconds to wait document loaded
    @returns {boolean}
    '''
    if self.action.element.wait(login_selector,wait_time):
      return False 
    else:
      return True
  
  def relogin(self,url):
    main_domain = BluesURL.get_main_domain(url) 

    self.relogin_time+=1

    if self.loginer_executor.endswith('.py'):
      ps_script = 'python %s %s' % (self.loginer_executor,main_domain)
    
    if self.loginer_executor.endswith('.exe'):
      ps_script = '%s %s ' % (self.loginer_executor,main_domain)

    BluesConsole.info('Relogin by : %s' % ps_script)

    return BluesPowerShell.execute(ps_script)

