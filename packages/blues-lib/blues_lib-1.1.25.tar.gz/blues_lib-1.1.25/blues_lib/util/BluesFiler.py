import os,requests,json
from datetime import datetime,timedelta

class BluesFiler:

  @classmethod
  def removedirs(cls,directory):
    '''
    @description Remove all child dir and files
    @param {string} directory 
    '''
    removed_count = 0
    for root, dirs, files in os.walk(directory):
      for file in files:
        os.remove(os.path.join(root, file))
        removed_count +=1
      for dir in dirs:
        os.rmdir(os.path.join(root, dir))
        removed_count +=1
    return removed_count

  @classmethod
  def download(cls,urls,directory,success=None,error=None):
    '''
    @description Download multi files
    @param {list} urls files' remote url
    @param {string} directory : Local directory to save the downloaded files
    @param {function} success : Callback function called on success
    @param {function} error : Callback function called on failure
    @returns {dict} complex result
    '''

    result = cls.__get_result()

    if not urls:
      return result 

    for url in urls:
      # download the image
      (code,file_or_msg) = cls.download_one(url,directory)
      if code == 200:
        item = {
          'url':url,
          'file':file_or_msg,
          'callback_value':None
        }
        if success:
          item['callback_value'] = success(file_or_msg)
        result['success']['count']+=1
        result['success']['files'].append(item)
        result['files'].append(file_or_msg)
        result['code'] = 200
      else:
        item = {
          'url':url,
          'message':file_or_msg,
          'callback_value':None
        }
        if error:
          item['callback_value'] = error(str(e))
        result['error']['count']+=1
        result['error']['files'].append(item)
    
    return result 

  @classmethod
  def download_one(cls,url,directory):
    '''
    @description : download one file
    @param {str} url : file's remote url
    @param {str} directory : The dir to save the download file
    '''
    try:
      # Ensure directory existence
      cls.makedirs(directory)
      # Keep the file name unchanged
      file_name = url.split('/')[-1]
      local_file = directory+'/'+file_name

      # 永远保持覆盖
      res=requests.get(url)
      res.raise_for_status()
      with open(local_file,'wb') as f:
        f.write(res.content)
        f.close()
        return (200,local_file) 

    except Exception as e:
      return (500,str(e))

  @classmethod
  def read(cls,file_path):
    try:
      with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    except Exception as e:
      return None

  @classmethod
  def read_json(cls,file_path):
    try:
      with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
    except Exception as e:
      return None

  @classmethod
  def write_json(cls,file,data,indent=2):
    return BluesFiler.write(file,json.dumps(data,indent=indent))

  @classmethod
  def __get_result(cls):
    return {
      'code':500,
      'files':[],
      'success':{
        'count':0,
        'files':[],
      },
      'error':{
        'count':0,
        'files':[],
      },
    }

  @classmethod
  def write(cls,file_path,text,mode='w'):
    '''
    @description : write text to file
    @param {str} file_path : file's path
    @param {str} text : content
    @param {str} mode : write mode
      - 'w' : clear the history content
      - 'a' : append text
    @returns {None} 
    '''
    dir_path = os.path.dirname(file_path)
    if dir_path!='.':
      cls.makedirs(dir_path)

    try:
      with open(file_path,mode,encoding='utf-8') as file:
        file.write(text)
        return file_path
    except Exception as e:
      return None

  @classmethod
  def exists(cls,path):
    '''
    @description : Does a dir or file exist
    @param {str} path
    @returns {bool} 
    '''
    return os.path.exists(path)

  @classmethod
  def makedirs(cls,path):
    '''
    @description : Create dirs (support multilevel directory) if they don't exist
    @param {str} path : multilevel dir
    @returns {None}
    '''
    if not cls.exists(path):
      os.makedirs(path)

  @classmethod
  def get_rename_file(cls,file_path,new_name='',prefix='',suffix='',separator='-'):
    '''
    @description : get the new file name path
    '''
    path_slices = file_path.split('/')
    original_name = path_slices[-1]
    copy_name = new_name if new_name else original_name
    if prefix:
      copy_name = prefix+separator+copy_name
    if suffix:
      copy_name = copy_name+separator+suffix
    path_slices[-1]=copy_name
    copy_path='/'.join(path_slices)
    return copy_path

  @classmethod
  def removefiles(cls,directory,retention_days=7):
    '''
    @description : clear files before n days
    @param {str} directory
    @param {int} retention_days : default 7
    @returns {int} deleted files count
    '''
    # 转换天数到时间间隔
    threshold = datetime.now() - timedelta(days=retention_days)
    removed_count = 0
    # 遍历目录
    for item in os.scandir(directory):
      try:
        # 获取文件的最后修改时间
        file_modified_time = datetime.fromtimestamp(os.path.getmtime(item.path))
        # 如果文件的最后修改时间早于阈值，则删除文件
        if os.path.isfile(item.path) and file_modified_time < threshold:
          os.remove(item.path)
          removed_count +=1
      except OSError as e:
        pass

    return removed_count
