import base64
import requests
import json


class AnaplanAPI:
    
    url = 'https://api.anaplan.com/1/3/'
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._user()
        self._getHeaders()
        self._downloadHeaders()
        self._postHeaders()
        self._putHeaders()
        
    def _user(self):
        user = 'Basic ' + str(base64.b64encode((
            f'{self.username}:{self.password}'
            ).encode('utf-8')).decode('utf-8'))
        self.user = user
        return self.user
    
    def _getHeaders(self):
        getHeaders = {'Authorization': self.user}
        self.getHeaders = getHeaders
        return self.getHeaders
    
    def _downloadHeaders(self):
        downloadHeaders = {
            'Authorization': self.user,
            'Content-Type': 'application/json'
        }
        self.downloadHeaders = downloadHeaders
        return self.downloadHeaders
    
    def _postHeaders(self):
        postHeaders = {
            'Authorization': self.user,
            'Content-Type': 'application/json'
        }
        self.postHeaders = postHeaders
        return self.postHeaders
    
    def _putHeaders(self):
        putHeaders = {
            'Authorization': self.user,
            'Content-Type': 'application/octet-stream'
        }
        self.putHeaders = putHeaders
        return self.putHeaders

    def getWorkspaces(self):
        getWorkspaces = requests.get(
            AnaplanAPI.url + 'workspaces',
            headers=self.getHeaders)
        return getWorkspaces.json()
    
    def getModels(self, wGuid=''):
        if wGuid:
            getModels = requests.get(
                AnaplanAPI.url + f'workspaces/{wGuid}/models', 
                headers=self.getHeaders)
        else:
            getModels = requests.get(
                AnaplanAPI.url + 'models',
                headers=self.getHeaders)
        return getModels.json()

    def getFiles(self, wGuid, mGuid):
        getFiles = requests.get(
            AnaplanAPI.url + f'workspaces/{wGuid}/models/{mGuid}/files',
            headers=self.getHeaders)
        return getFiles.json()

    def getImports(self, wGuid, mGuid):
        getImports = requests.get(
            AnaplanAPI.url + f'workspaces/{wGuid}/models/{mGuid}/imports',
            headers=self.getHeaders)
        return getImports.json()
    
    def getExports(self, wGuid, mGuid):
        getExports = requests.get(
            AnaplanAPI.url + f'workspaces/{wGuid}/models/{mGuid}/exports',
            headers=self.getHeaders)
        return getExports.json()
    
    def getActions(self, wGuid, mGuid):
        getActions = requests.get(
            AnaplanAPI.url + f'workspaces/{wGuid}/models/{mGuid}/actions',
            headers=self.getHeaders)
        return getActions.json()
    
    def getProcesses(self, wGuid, mGuid):
        getProcesses = requests.get(
            AnaplanAPI.url + f'workspaces/{wGuid}/models/{mGuid}/processes',
            headers=self.getHeaders)
        return getProcesses.json()
    
    def export(self, wGuid, mGuid, fileId):
        postExport = requests.post(
            AnaplanAPI.url + f'workspaces/{wGuid}/' + \
                f'models/{mGuid}/exports/{fileId}/tasks',
            headers=self.postHeaders,
            data=json.dumps({'localeName': 'en_US'}))
        return postExport
    
    def downloadFile(self, wGuid, mGuid, fileId):
        getChunk = requests.get(
            AnaplanAPI.url + f'workspaces/{wGuid}/' + \
               f'models/{mGuid}/files/{fileId}/chunks/0', 
            headers=self.downloadHeaders)
        return getChunk #.content #.status_code
    
    def fileUpload(self, wGuid, mGuid, fileId, dataFile):
        fileUpload = requests.put(
            AnaplanAPI.url + f'workspaces/{wGuid}/' + \
                f'models/{mGuid}/files/{fileId}',
            headers=self.putHeaders, 
            data=(dataFile))
        return fileUpload
    
    def Import(self, wGuid, mGuid, importId):
        postImport = requests.post(
            AnaplanAPI.url + f'workspaces/{wGuid}/' + \
                f'models/{mGuid}/imports/{importId}/tasks',
            headers=self.postHeaders,
            data=json.dumps({'localeName': 'en_US'}))
        return postImport

    def process(self, wGuid, mGuid, processId):
        postProcess = requests.post(
            AnaplanAPI.url + f'workspaces/{wGuid}/' + \
                f'models/{mGuid}/processes/{processId}/tasks',
            headers=self.postHeaders,
            data=json.dumps({'localeName': 'en_US'}))
        return postProcess

    