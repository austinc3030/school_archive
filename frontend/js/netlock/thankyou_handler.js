// Require jquery
const jquery = require( 'jquery' )
window.$ = window.jQuery=jquery;

// Require path
const path = require( 'path' )

// Create the client for the server
const zerorpc = require( "zerorpc" )
let client = new zerorpc.Client( )

// Get a reference to the elements
let gobacktologinnew = document.querySelector( '#gobacktologinnew' )
let gobacktossid = document.querySelector( '#gobacktossid' )
let gobacktofeature = document.querySelector( '#gobacktofeature' )
let gobacktoencryption = document.querySelector( '#gobacktoencryption' )

// Constant for the progressStep
const progressStep = 'thankyou'

// Get a reference to the main process
const remote = require('electron').remote
const mainWindow = remote.getCurrentWindow( )



// Connect to the rpc server
client.connect( "tcp://127.0.0.1:4242" )



// ****************************************************************************
// Name: fgobacktologinnew
// Abstract: Go back to the loginnew screen
// ****************************************************************************
const fgobacktologinnew = ( ) => {
  
  mainWindow.loadURL(
    require( 'url' ).format(

      {

        pathname: path.join( __dirname, '..', '..', 'pages', 'loginnew.html' ),
        protocol: 'file:',
        slashes: true

      } // End format

    ) // End loadURL

  ) // End mainWindow

} // End fgobacktologinnew( )



// ****************************************************************************
// Name: fgobacktossid
// Abstract: Go back to the ssid screen
// ****************************************************************************
const fgobacktossid = ( ) => {

  mainWindow.loadURL(
    require( 'url' ).format(

      {

        pathname: path.join( __dirname, '..', '..', 'pages', 'ssid.html' ),
        protocol: 'file:',
        slashes: true

      } // End format

    ) // End loadURL

  ) // End mainWindow

} // End fgobacktossid( )



// ****************************************************************************
// Name: fgobacktofeature
// Abstract: Go back to the feature screen
// ****************************************************************************
const fgobacktofeature = ( ) => {

  mainWindow.loadURL(
    require( 'url' ).format(

      {

        pathname: path.join( __dirname, '..', '..', 'pages', 'feature.html' ),
        protocol: 'file:',
        slashes: true

      } // End format

    ) // End loadURL

  ) // End mainWindow

} // End fgobacktofeature( )



// ****************************************************************************
// Name: fgobacktoencryption
// Abstract: Go back to the encryption screen
// ****************************************************************************
const fgobacktoencryption = ( ) => {

  mainWindow.loadURL(
    require( 'url' ).format(

      {

        pathname: path.join( __dirname, '..', '..', 'pages', 'encryption.html' ),
        protocol: 'file:',
        slashes: true

      } // End format

    ) // End loadURL

  ) // End mainWindow

} // End fgobacktoencryption( )



// ****************************************************************************
// Name: fsetProgressStep
// Abstract: Update the backend with the current progress step
// ****************************************************************************
const fsetProgressStep = ( ) => {

  // Tell the backend what step we are on
  client.invoke( "setProgressStep", progressStep, ( error, res ) => {

    if( error || res !== 'success' ) {

      console.error( error )

    } else {

      console.log( "Backend progress step updated successfully." )

    } // End if

  } ) // End invoke( "setProgressStep" )

} // End fsetProgressStep( )



// Add an event listener to the steps
gobacktologinnew.addEventListener( 'click', fgobacktologinnew ) // End EventListener
gobacktossid.addEventListener( 'click', fgobacktossid ) // End EventListener
gobacktofeature.addEventListener( 'click', fgobacktofeature ) // End EventListener
gobacktoencryption.addEventListener( 'click', fgobacktoencryption ) // End EventListener

// When everything is loaded, notify the backend that we are on the current step
mainWindow.webContents.once( 'did-finish-load', fsetProgressStep )