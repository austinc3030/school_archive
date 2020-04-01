from __future__ import print_function

import os
import sys
import time

import zerorpc

from selenium import webdriver
from os.path import expanduser
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options



# Global vars for the chromedriver and chromium binaries
chromedriver_path   = None
chromium_path       = None
webdriver           = None

# Other global variables
currentProgressStep = None



def getChromedriverPath( ):
    
    try:

        # Make sure the global chromedriver_path is used
        global chromedriver_path

        # Try to find the chromedriver binary
        success     = False
        binary_path = None

        if sys.platform == 'darwin':

            # Get the user folder
            user_folder = expanduser("~")

            # Possible application folders
            global_apps_folder  = os.path.join('/', 'Applications')
            user_apps_folder    = os.path.join(user_folder, 'Applications')

            # Possible binary paths
            global_binary_path  = os.path.join( global_apps_folder, 'netlock.app', 'Contents', 'Resources', 'app',
                                                'node_modules', 'electron-chromedriver', 'bin', 'chromedriver')
            user_binary_path    = os.path.join( user_apps_folder, 'netlock.app', 'Contents', 'Resources', 'app',
                                                'node_modules', 'electron-chromedriver', 'bin', 'chromedriver')

            # Determine if the application is installed globally or just for the user
            if os.path.isfile( global_binary_path ) :

                # Globally installed
                binary_path = global_binary_path

            elif os.path.isfile( user_binary_path ) :

                # User installed
                binary_path = user_binary_path

            # End ifelse

        # End if

        # Were we successful?
        if binary_path is not None :

            # Yes
            success = True

        # End if

        # Set the global variable
        chromedriver_path = binary_path

        return success

    except Exception as e:
    
            return e
    
# End getChromedriverPath( )



def getChromiumPath( ):

    try:

        # Make sure the global chromium_path is used
        global chromium_path

        # Try to find the chromium binary
        success     = False
        binary_path = None

        if sys.platform == 'darwin':

            # Get the user folder
            user_folder = expanduser( "~" )

            # Possible application folders
            global_apps_folder  = os.path.join( '/', 'Applications' )
            user_apps_folder    = os.path.join( user_folder, 'Applications' )

            # Possible binary paths
            global_binary_path = os.path.join( global_apps_folder, 'netlock.app', 'Contents', 'Resources', 'app',
                                               'node_modules', 'chromium', 'lib', 'chromium', 'chrome-mac',
                                               'Chromium.app', 'Contents', 'MacOS', 'Chromium' )
            user_binary_path = os.path.join( global_apps_folder, 'netlock.app', 'Contents', 'Resources', 'app',
                                             'node_modules', 'chromium', 'lib', 'chromium', 'chrome-mac',
                                             'Chromium.app', 'Contents', 'MacOS', 'Chromium' )

            # Determine if the application is installed globally or just for the user
            if os.path.isfile( global_binary_path ):

                # Globally installed
                binary_path = global_binary_path

            elif os.path.isfile( user_binary_path ):

                # User installed
                binary_path = user_binary_path

            # End ifelse

        # End if

        # Were we successful?
        if binary_path is not None:

            # Yes
            success = True

        # End if

        # Set the global variable
        chromium_path = binary_path

        return success

    except Exception as e:

        return e


# End getChromiumPath( )



def fShutdownAllBackend( ):

    global webdriver

    webdriver.quit( )

    sys.exit( 1 )

    return True

# End fShutdownAllBackend



def fStartChromiumDriver( ):

    # Start the Chromium Backend

    try:

        # Get the chromedriver binary path
        if getChromedriverPath( ) == False :

            # Couldn't find driver binary
            raise ValueError( 'Could not find chromedriver binary' )

        # End if

        # Get the chromium binary path
        if getChromiumPath( ) == False:

            # Couldn't find driver binary
            raise ValueError( 'Could not find chromium binary' )

        # End if

        # Make sure the global chromedriver_path is used
        global webdriver

        chrome_options = Options( )
        chrome_options.add_argument( "--disable-extensions" )
        chrome_options.add_argument( "--incognito" )

        # Commented for development/testing. Will remove when deploying
        # chrome_options.add_argument( "--headless" )

        chrome_options.binary_location = chromium_path
        webdriver = Chrome( executable_path = chromedriver_path, options = chrome_options )

    except Exception as e:

        return e

    return "success"

# End fStartChromiumBackend( )



def fSetProgressStep( step ):

    try:

        global currentProgressStep

        currentProgressStep = step

    except Exception as e:

        return e

    return "success"

# End fSetProgressStep( )



def fGetProgressStep( ):

    try:

        global currentProgressStep

        return currentProgressStep

    except Exception as e:

        return e

# End fSetProgressStep( )



def fWaitTest( ):

    try:

        return "success"

    except Exception as e:

        return e

# End fSetProgressStep( )



class NetLockAPI( object ):



    def echo( self, text ):

        # echo any text

        return text

    # End echo( )



    def startDriver( self ):

        return fStartChromiumDriver( )

    # End startChromiumBackend( )



    def shutdownBackend( self ):

        return fShutdownAllBackend( )

    # End shutdownBackend( )



    def setProgressStep( self, step ):

        return fSetProgressStep( step )

    # End setProgressStep( )



    def getProgressStep( self ):

        return fGetProgressStep( )

    # End setProgressStep( )



    def waitTest( self ):

        return fWaitTest( )

    # End setProgressStep( )



# End NetLockAPI( )



def parsePort( ):
    
    port = 4242
    
    try:
    
        port = int( sys.argv[ 1 ] )
    
    except Exception as e:
    
        pass
    
    return '{}'.format( port )

# End parsePort( )



def main( ):
    
    try:
      
        address = 'tcp://127.0.0.1:' + parsePort( )
        
        rpc_server = zerorpc.Server( NetLockAPI( ) )
        
        rpc_server.bind( address )
        
        print( 'start running on {}'.format( address ) )
        rpc_server.run( )

    except Exception as e:
    
        return e

# End main( )



if __name__ == '__main__':

    main( )

# End __name__