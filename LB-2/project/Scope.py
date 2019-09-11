class Scope:
    uniprotId: str
    pdbId: str

    def __init__(self, uniprotId, pdbId):
        self.uniprotId = uniprotId
        self.pdbId = pdbId

