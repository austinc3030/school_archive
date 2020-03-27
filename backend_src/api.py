from __future__ import print_function

import os
import sys

import zerorpc

from selenium import webdriver
from os.path import expanduser
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By



# Global vars for the chromedriver and chromium binaries
chromedriver_path   = None
chromium_path       = None
webdriver           = None



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



def changeAdminCredentials( self, oldUser, newUser, oldPass, newPass ):

    try:

        # Make sure the global chromedriver_path is used
        global webdriver

        webdriver.get( "http://" + oldUser + ":" + oldPass + "@192.168.0.1" )
        webdriver.set_window_size( 1440, 900 )
        webdriver.switch_to.frame( 1 )
        webdriver.find_element( By.ID, "a64" ).click( )
        webdriver.find_element( By.ID, "a71" ).click( )
        webdriver.switch_to.default_content( )
        webdriver.switch_to.frame( 2 )
        webdriver.find_element( By.NAME, "oldname" ).send_keys( oldUser )
        webdriver.find_element( By.NAME, "oldpassword" ).send_keys( oldPass )
        webdriver.find_element( By.NAME, "newname" ).send_keys( newUser )
        webdriver.find_element( By.NAME, "newpassword" ).send_keys( newPass )
        webdriver.find_element( By.NAME, "newpassword2" ).send_keys( newPass )
        webdriver.find_element( By.NAME, "Save" ).click( )

    except Exception as e:

        return e

    return "success"

# End setAdminCredentials



def startChromiumDriver( ):

    # Start the Chromium Backend

    try:

        # Make sure the global chromedriver_path is used
        global webdriver

        chrome_options = ChromeOptions( )
        chrome_options.add_argument( "--disable-extensions" )
        chrome_options.binary_location = chromium_path
        webdriver = Chrome( executable_path = chromedriver_path, options = chrome_options )

    except Exception as e:

        return e

    return "success"

# End startChromiumBackend( )



class CalcApi( object ):


    
    def echo( self, text ):
    
        # echo any text
    
        return text

    # End echo( )



    def setAdminCredentials( self, oldUser, newUser, oldPass, newPass ):

        return changeAdminCredentials( self, oldUser, newUser, oldPass, newPass )

    # End getChromiumPaths



    def startDriver( self ):

        return startChromiumDriver( )

    # End startChromiumBackend( )



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
      
        addr = 'tcp://127.0.0.1:' + parsePort( )
        
        s = zerorpc.Server( CalcApi( ) )
        
        s.bind( addr )
        
        print( 'start running on {}'.format( addr ) )
        s.run( )

    except Exception as e:
    
        return e

# End main( )



if __name__ == '__main__':

    main( )

# End __name__