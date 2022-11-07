class OpenstreetmapService:
    def __init__(self):
        self.url = "https://www.openstreetmap.org/"
        self.authorisation={'Authorization':'Bearer ArJJPEmlED6mjSsFnVTETG59xBc5FoMCoohnoG_b33bK3pDQwLM4apVEy6xi3UJM','Content-Type':'application/json'}
        

    def getBoundingBox(coordinates):
        apiRequest=self.api_url+"/api/0.6/map?bbox={left},{bottom},{right},{top}".format(left = coordinates["left"],bottom=coordinates["bottom"],right=coordinates["right"],top=coordinates["top"])
        response = requests.get(apiRequest)
        result=response.json()