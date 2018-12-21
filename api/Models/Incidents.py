class Incident(object):
    '''Class contains incident's reports'''
    reports = []
    def __init__(self, incident_id, createdOn, createdBy, incType, location, status, image, video,comment):
        self.incident_id = incident_id
        self.createdOn = createdOn
        self.createdBy = createdBy
        self.incType = incType
        self.location = location
        self.status = status
        self.image = image
        self.video = video
        self.comment = comment