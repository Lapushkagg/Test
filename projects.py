import requests
from auth_id import auth_company_id

class projects:

  api = auth_company_id("https://ru.yougile.com") 
  token = api.get_token()
  par = {
        'Token': token
        }

  def __init__(self, url):
    self.url = url

  def get_progects(self,par= par):
    resp = requests.get(self.url+'/api-v2/projects', headers=par)
    return resp.json()
  

  def create_progect(self, title, users = {"50dfbfc9-f778-4909-8396-1986fc2f8026": "admin"},par = par):
    progect = {
            "title": title,
            "users": users
     }

    resp = requests.post(self.url + '/api-v2/projects', json = progect, headers = par)
    return resp.json()
  

  def get_progect(self, id, par = par):
    resp = requests.get(self.url+'/api-v2/projects/'+str(id), headers=par)
    return resp.json()

  def edit(self, id, name, deleted = False, par = par):
    
   company = {
     
        "title": name,
        "deleted": deleted
     }
    
   resp = requests.put(self.url+'/api-v2/projects/'+str(id), json=company, headers=par)
   return resp.json()
  
