from __future__ import print_function

import os
import sys
import time

import zerorpc

from calc import calc as real_calc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os.path import expanduser


# Global vars for the chromedriver and chromium binaries
chromedriver_path   = None
chromium_path       = None



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



def getChromiumPath():
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



class CalcApi( object ):



    def calc( self, text ):
    
        # Based on the input text, return the int result
    
        try:
    
            return real_calc( text )
    
        except Exception as e:
    
            return 0.0   

    # End calc( ) 


    
    def echo( self, text ):
    
        # echo any text
    
        return text

    # End echo( )



    def getChromedriverPath( self ):

        return chromedriver_path

    # End getChromedriverPaths



    def getChromiumPath( self ):

        return chromium_path

    # End getChromiumPaths



    def startChromiumBackend( self ):
    
        # Start the Chromium Backend
    
        try:

            chrome_options = Options( )
            chrome_options.add_argument( "--disable-extensions" )
            chrome_options.binary_location = chromium_path
            driver = webdriver.Chrome( executable_path = chromedriver_path, options = chrome_options )

            driver.get( 'http://www.google.com/' )
            time.sleep( 5 ) # Let the user actually see something!
            search_box = driver.find_element_by_name( 'q' )
            search_box.send_keys( 'ChromeDriver' )
            search_box.submit( )
            time.sleep( 5 ) # Let the user actually see something!
            driver.quit( )

        except Exception as e:
    
            return e

        return "success"  

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