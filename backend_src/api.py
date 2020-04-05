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
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chromedriver_path   = None
chromium_path       = None
webdriver           = None

# Other global variables
currentProgressStep = None
current_username = None
current_password = None
encryption_wpa2 = None
feature_wps = None
feature_upnp = None
feature_castssid = None
new_login_username = None
new_login_password = None
new_ssid_name = None
new_ssid_password = None



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



def fWaitTest( duration ):

    try:

        time.sleep( duration )

        return "success"

    except Exception as e:

        return e

# End fSetProgressStep( )



def fSetCurrentCredentials( username, password ):

    try:

        global current_username
        global current_password

        current_username = username
        current_password = password

        return fTestRouterAccess( )

    except Exception as e:

        return e

# End fSetCurrentCredentials( )



def fGetCurrentCredentials( ):

    try:

        global current_username
        global current_password

        return "User/Pass: " + current_username + " / " + current_password

    except Exception as e:

        return e

# End fSetCurrentCredentials( )



def fSetEncryption( wpa2 ):

    try:

        global encryption_wpa2

        encryption_wpa2 = wpa2

        return "success"

    except Exception as e:

        return e

# End fSetCurrentCredentials( )



def fGetEncryption( ):

    try:

        global encryption_wpa2

        return "Encryption = WPA2: " + str( encryption_wpa2 )

    except Exception as e:

        return e

# End fSetCurrentCredentials( )



def fSetFeatures( wps, upnp, castssid ):

    try:

        global feature_wps
        global feature_upnp
        global feature_castssid

        feature_wps = wps
        feature_upnp = upnp
        feature_castssid = castssid

        return "success"

    except Exception as e:

        return e

# End fSetCurrentCredentials( )



def fGetFeatures( ):

    try:

        global feature_wps
        global feature_upnp
        global feature_castssid

        return "WPS: " + str( feature_wps ) + " UPnP: " + str( feature_upnp ) + " Broadcast SSID: " + str( feature_castssid )

    except Exception as e:

        return e

# End fSetCurrentCredentials( )



def fTestRouterAccess( ):

    try:

        global webdriver
        global current_username
        global current_password

        webdriver.get( "http://" + current_username + ":" + current_password + "@192.168.0.1/" )
        webdriver.set_window_size( 1200, 780 )
        webdriver.switch_to.frame( 2 )

        if ( webdriver.title == "Archer C7" ) :

            return "success"

        else :

            return "unsuccessful"

        # End ifelse

    except Exception as e:

        return e

# End fTestRouterAccess( )



def fSetNewCredentials( username, password ):

    try:

        global current_username
        global current_password
        global new_login_username
        global new_login_password
        global webdriver

        new_login_username = username
        new_login_password = password

        webdriver.get( "http://" + current_username + ":" + current_password + "@192.168.0.1/" )
        webdriver.set_window_size( 1200, 780 )
        webdriver.switch_to.frame( 1 )
        webdriver.find_element( By.ID, "a64" ).click( )
        webdriver.find_element( By.ID, "a71" ).click( )
        webdriver.switch_to.default_content( )
        webdriver.switch_to.frame( 2 )
        WebDriverWait( webdriver , 30000).until(expected_conditions.element_to_be_clickable((By.NAME, "oldname")))
        webdriver.find_element(By.NAME, "oldname").send_keys( current_username )
        webdriver.find_element(By.NAME, "oldpassword").send_keys( current_password )
        webdriver.find_element(By.NAME, "newname").send_keys(new_login_username )
        webdriver.find_element(By.NAME, "newpassword").send_keys(new_login_password)
        webdriver.find_element(By.NAME, "newpassword2").send_keys(new_login_password)
        webdriver.find_element(By.NAME, "Save").click( )

        current_username = new_login_username
        current_password = new_login_password

        time.sleep(1)

        return fTestRouterAccess( )

    except Exception as e:

        return e

# End fSetCurrentCredentials( )



def fGetNewCredentials( ):

    try:

        global new_login_username
        global new_login_password

        return "User/Pass: " + new_login_username + " / " + new_login_password

    except Exception as e:

        return e

# End fSetCurrentCredentials( )



def fConfigure5GSSID( ):

    try:

        global new_ssid_name
        global new_ssid_password
        global current_username
        global current_password

        webdriver.get("http://" + current_username + ":" + current_password + "@192.168.0.1/")
        webdriver.set_window_size(1200, 780)
        webdriver.switch_to.frame(1)
        webdriver.find_element(By.ID, "a14").click()
        webdriver.switch_to.default_content()
        webdriver.switch_to.frame(2)
        WebDriverWait(webdriver, 30000).until(expected_conditions.element_to_be_clickable((By.ID, "ssid")))
        webdriver.find_element( By.ID, "ssid").clear( )
        webdriver.find_element(By.ID, "ssid").send_keys( new_ssid_name + "-5G" )
        webdriver.find_element(By.ID, "Save").click()
        webdriver.switch_to.default_content()
        webdriver.switch_to.frame(1)
        webdriver.find_element(By.ID, "a17").click()
        webdriver.switch_to.default_content()
        webdriver.switch_to.frame(2)
        WebDriverWait(webdriver, 30000).until(expected_conditions.element_to_be_clickable((By.ID, "pskSecret")))
        webdriver.find_element(By.ID, "pskSecret").clear( )
        webdriver.find_element(By.ID, "pskSecret").send_keys(new_ssid_password)
        webdriver.find_element(By.ID, "Save").click()

    except Exception as e:

        return e

# End fConfigure5GSSID( )



def fConfigure2GSSID( ):

    try:

        global new_ssid_name
        global new_ssid_password
        global current_username
        global current_password

        webdriver.get("http://" + current_username + ":" + current_password + "@192.168.0.1/")
        webdriver.set_window_size(1200, 780)
        webdriver.switch_to.frame(1)
        webdriver.find_element(By.ID, "a7").click()
        webdriver.switch_to.default_content()
        webdriver.switch_to.frame(2)
        WebDriverWait(webdriver, 30000).until(expected_conditions.element_to_be_clickable((By.ID, "ssid")))
        webdriver.find_element(By.ID, "ssid").clear( )
        webdriver.find_element(By.ID, "ssid").send_keys( new_ssid_name + "-2.4G" )
        webdriver.find_element(By.ID, "Save").click()
        webdriver.switch_to.default_content()
        webdriver.switch_to.frame(1)
        webdriver.find_element(By.ID, "a10").click()
        webdriver.switch_to.default_content()
        webdriver.switch_to.frame(2)
        WebDriverWait(webdriver, 30000).until(expected_conditions.element_to_be_clickable((By.ID, "pskSecret")))
        webdriver.find_element(By.ID, "pskSecret").clear( )
        webdriver.find_element(By.ID, "pskSecret").send_keys(new_ssid_password)
        webdriver.find_element(By.ID, "Save").click()

    except Exception as e:

        return e

# End fConfigure2GSSID( )


def fSetSSIDInformation( new_ssid, new_password ):

    try:

        global new_ssid_name
        global new_ssid_password

        new_ssid_name = new_ssid
        new_ssid_password = new_password

        fConfigure2GSSID()
        fConfigure5GSSID()

        return "success"

    except Exception as e:

        return e

# End fSetCurrentCredentials( )



def fGetSSIDInformation( ):

    try:

        global new_ssid_name
        global new_ssid_password

        return "SSID: " + new_ssid_name + " Password: " + new_ssid_password

    except Exception as e:

        return e

# End fSetCurrentCredentials( )



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

    # End getProgressStep( )



    def waitTest( self, duration ):

        return fWaitTest( duration )

    # End waitTest( )



    def setCurrentCredentials( self, username, password ):

        return fSetCurrentCredentials( username, password )

    # End setCurrentCredentials( )



    def getCurrentCredentials( self ):

        return fGetCurrentCredentials( )

    # End setCurrentCredentials( )



    def setEncryption( self, wpa2 ):

        return fSetEncryption( wpa2 )

    # End setCurrentCredentials( )



    def getEncryption( self ):

        return fGetEncryption( )

    # End setCurrentCredentials( )



    def setFeatures( self, wps, upnp, castssid ):

        return fSetFeatures( wps, upnp, castssid )

    # End setCurrentCredentials( )



    def getFeatures( self ):

        return fGetFeatures( )

    # End setCurrentCredentials( )



    def setNewCredentials( self, username, password ):

        return fSetNewCredentials( username, password )

    # End setCurrentCredentials( )



    def getNewCredentials( self ):

        return fGetNewCredentials( )

    # End setCurrentCredentials( )



    def setSSIDInformation( self, new_ssid, new_password ):

        return fSetSSIDInformation( new_ssid, new_password )

    # End setCurrentCredentials( )



    def getSSIDInformation( self ):

        return fGetSSIDInformation( )

    # End setCurrentCredentials( )



    def testRouterAccess( self ):

        return fTestRouterAccess( )

    # End testRouterAccess

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