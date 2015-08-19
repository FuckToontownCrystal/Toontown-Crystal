from direct.directnotify import DirectNotifyGlobal
from src.toontown.parties.DistributedPartyJukeboxActivityBaseAI import DistributedPartyJukeboxActivityBaseAI
import PartyGlobals

class DistributedPartyJukeboxActivityAI(DistributedPartyJukeboxActivityBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyJukeboxActivityAI")
    
    def __init__(self, air, parent, activityTuple):
        DistributedPartyJukeboxActivityBaseAI.__init__(self, air, parent, activityTuple)
        self.music = PartyGlobals.PhaseToMusicData

