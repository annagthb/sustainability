class OpenstreetmapService:
    ##TODO
    def __init__(self):
        self.url = "https://www.openstreetmap.org/"
        self.authorisationHeader={'Authorization':'Bearer myEncryptedApiToken','Content-Type':'application/json'}
        

    def getBoundingBox(coordinates):
        ##TODO
        apiRequest=self.api_url+"/api/0.6/map?bbox={left},{bottom},{right},{top}".format(left = coordinates["left"],bottom=coordinates["bottom"],right=coordinates["right"],top=coordinates["top"])
        response = requests.get(apiRequest)
        result=response.json()