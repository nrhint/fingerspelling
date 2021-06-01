##Nathan Hinton
##This is an updating manager for my program.


def runUpdateManager():
    from util import updater

    version = open('./version', 'r').read()

    if updater.checkForUpdates(version):
        updater.downloadUpdates()
