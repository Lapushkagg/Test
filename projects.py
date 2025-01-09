import requests

class projects:

  def __init__(self, url):
    self.url = url

  def get_progects(self,par):
    resp = requests.get(self.url+'/api-v2/projects', headers=par)
    data = resp.json()
    return data.get("content", []) 
  

  def create_progect(self,  par, title):
    progect = {
            "title": title
     }

    resp = requests.post(self.url + '/api-v2/projects', json = progect, headers = par)
    return resp.json()
  

  def get_progect(self, id, par):
    resp = requests.get(self.url+'/api-v2/projects/'+str(id), headers=par)
    return resp.json()

  def edit(self, par, id, name, deleted = False):
    
   company = {
     
        "title": name,
        "deleted": deleted
     }
    
   resp = requests.put(self.url+'/api-v2/projects/'+str(id), json=company, headers=par)
   return resp.json()
  
