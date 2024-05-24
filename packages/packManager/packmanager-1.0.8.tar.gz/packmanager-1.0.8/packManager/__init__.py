import os
def install(package,consCall, hasInput):
    if consCall == 1 or consCall == True:
        if hasInput == False or hasInput == 0:
            os.system('pip install ' + package + ' --no-input')
        else:
            os.system('pip install ' + package)
    
    if consCall == 0 or consCall == False:
        if hasInput == False or hasInput == 0:
            os.system('pip install ' + package + ' ' + '-q -q -q ' + '--no-input')
        else:
            os.system('pip install ' + package + ' ' + '-q -q -q ')

def uninstall(package,consCall, hasInput):
    if consCall == 1 or consCall == True:
        if hasInput == False or hasInput == 0:
            os.system('pip uninstall ' + package + ' -y')
        else:
            os.system('pip uninstall ' + package)
    if consCall == 0 or consCall == False:
        if hasInput == False or hasInput == 0:
            os.system('pip uninstall ' + package + ' ' + '-q -q -q ' + '-y')
        else:
            os.system('pip uninstall ' + package + ' ' + '-q -q -q ')
def testInstall(package):
    import importlib.util
    spec = importlib.util.find_spec(package)
    if spec is None:
        return False
    else:
        return True