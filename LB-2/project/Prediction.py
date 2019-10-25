class Prediction:

    id: str
    ss_checked: str
    ss_predicted: str

    def __init__(self, id="", ss_checked="", ss_predicted=""):
        self.id = id
        self.ss_checked = ss_checked
        self.ss_predicted = ss_predicted

    def increment(self, ss_checked: str, ss_predicted: str):
        self.ss_checked += ss_checked
        self.ss_predicted += ss_predicted




