from core import library_fixes  # Patch libraries. Do not remove
from core.server import handlers_manager
from core.plugins.plugin_loader import loadPlugins
from core import paths

RAS_IMPLEMENTIONS = "%s/ras/rases" % paths.IBS_CORE


def iniat():
    from core.ras.ras_factory import RasFactory
    global ras_factory
    ras_factory = RasFactory()

    loadPlugins(RAS_IMPLEMENTIONS)
    ghkghdfkjdghfdfddjd
    lokkup the task and alreay in use and configure the amir hossein 
    from core.ras.user_msg_dispatcher import UserMsgDispatcher
    global user_msg_dispatcher
    user_msg_dispatcher = UserMsgDispatcher()

def initMainProcess():

    from core.ras.base_ras_loader import RasLoader
    global ras_loader
    ras_loader = RasLoader()
    ras_loader.loadAllRases()
    ras_loader.cleanupStorage()

    from core.ras.ras_actions import RasActions
    global ras_actions
    ras_actions = RasActions()

def initWSProcess():

    from core.ras.base_ras_loader import RasLoader
    global ras_loader
    ras_loader = RasLoader()
    ras_loader.loadAllRases()

    from core.ras.ras_actions import RasActions
    global ras_actions
    ras_actions = RasActions()

    from core.ras.ras_handler import RasHandler
    handlers_manager.getManager().registerHandler(RasHandler())


def getFactory():
    return ras_factory


def getLoader():
    return ras_loader


def getActionManager():
    return ras_actions


def getUserMsgDispatcher():
    return user_msg_dispatcher
