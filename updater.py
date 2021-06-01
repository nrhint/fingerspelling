##Nathan Hinton
##This is for updating the program and checking for updates

from requests import get as getUrl

def runUpdate(config):
    print('running updater...')
    if checkForUpdates(config):
        downloadUpdates()

def checkForUpdates(version):
    print('checking for updates...')
    url = 'https://github.com/nrhint/fingerspelling/blob/main/version'
    data = getUrl(url)
    text = data.text
    pointer = text.index('id="LC1"')
    self_version = version
    while text[pointer] != '>':
        pointer += 1
    start = pointer+1
    while text[pointer] != '<':
        pointer += 1
    end = pointer
    onlineVersion = text[start:end]
    print('most recent version: %s'%onlineVersion)
    print('your version is %s'%self_version)
    if onlineVersion != self_version:
        return True
    else:
        return False
    
def downloadUpdates():
    print('downloading updates...')
    from os.path import isdir
    baseUrl = 'https://raw.github.com/nrhint/fingerspelling/main'
    tree = getUrl(baseUrl+'/tree.tree')
    tree = tree.text.split('\n')
    for path in tree:
        tmpUrl = baseUrl+str(path[1:])
        tmpUrl = tmpUrl.replace('\\', '/')
        #print(tmpUrl)
        file = getUrl(tmpUrl)
        print(path)
        text = file.text.replace(u"\uFFFD", " !!!Unknown char was here!!! ")
        try:
            open(path, 'w').write(text)
        except PermissionError:
            if isdir(path):
                print('folder skipped')
            else:
                print("Error...")
                input()
                raise Exception

        print("%s downloaded..."%tmpUrl)
    print('Finished downloading. Please restart the program...')
    input('Press enter to close: ')
    quit()
