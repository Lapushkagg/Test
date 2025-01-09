import requests

class auth_company_id:
   
  def __init__(self, url):
    self.url = url

  def get_conpany(self, user = 'lapushkagg8@gmail.com', password = 'Zzzxxx12345',name = 'Company'):
    
    creds = {
        'login': user,
        'password': password,
        'name': name
        }
    
    resp = requests.post(self.url+'/api-v2/auth/companies', json=creds)
    return resp.json()["content"][0]['id']
      
  def get_token(self, user = 'lapushkagg8@gmail.com', password = 'Zzzxxx12345'):
    
    creds = {
        'login': user,
        'password': password,
        'companyId': self.get_conpany()
        }
    
    resp = requests.post(self.url+'/api-v2/auth/keys/get', json=creds)
    return resp.json()[0]['key']
