from voter import Voter

class Candidate(Voter):
    def __init__(self, electiontype, status, date_application, id = None):
        self.electiontype = electiontype
        self.status = status
        self.date_application = date_application
        self.id = id