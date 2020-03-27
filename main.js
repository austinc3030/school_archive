// ****************************************************************************
// Name: main.js
// Abstract: This is the main js script to launch and start the application
// ****************************************************************************
const electron = require( 'electron' )
const app = electron.app
const BrowserWindow = electron.BrowserWindow
const path = require( 'path' )

// Create a variable to hold the mainWindow
let mainWindow = null

// Python Stuff
const PY_DIST_FOLDER = 'backend'
const PY_MODULE      = 'api'    // without .py suffix

// Create variables for the python process and port
let pyProc = null
let pyPort = null

// Loading screen stuff
let loadingScreen;



// ****************************************************************************
// Name: nullifyLoadingScreen
// Abstract: Set the loading screen to null
// ****************************************************************************
const nullifyLoadingScreen = ( ) => {
  
  loadingScreen = null

} // End nullifyLoadingScreen( )



// ****************************************************************************
// Name: didFinishLoad
// Abstract: Create a loading screen
// ****************************************************************************
const didFinishLoad = ( ) => {
  
  loadingScreen.show( )

} // End didFinishLoad( )



// ****************************************************************************
// Name: createLoadingScreen
// Abstract: Create a loading screen
// ****************************************************************************
const createLoadingScreen = () => {

  loadingScreen = new BrowserWindow( 
    Object.assign( 
      {
      
        width:        200,
        height:       400,
        frame:        false,
        transparent:  true
      
      }  // End assign
    
    ) // End BrowserWindow

  ) // End loadingScreen
  
  loadingScreen.setResizable( false )

  loadingScreen.loadURL( 
    require( 'url' ).format( 
      
      {
      
        pathname: path.join( __dirname, 'frontend', 'pages', 'loading.html' ),
        protocol: 'file:',
        slashes: true
      
      } // End format

    ) // End loadURL

  ) // End loadingScreen

  loadingScreen.on( 'closed', nullifyLoadingScreen )
  
  loadingScreen.webContents.on('did-finish-load', didFinishLoad )

} // End createLoadingScreen



// ****************************************************************************
// Name: getScriptPath
// Abstract: Build the path to the python rpc server
// ****************************************************************************
const getScriptPath = ( ) => {

  return path.join( __dirname, PY_DIST_FOLDER, PY_MODULE )

} // End getScriptPath( )



// ****************************************************************************
// Name: selectPort
// Abstract: Select the port the python rpc server should listen on
// ****************************************************************************
const selectPort = ( ) => {

  pyPort = 4242

  return pyPort

} // End selectPort( )



// ****************************************************************************
// Name: createPyProc
// Abstract: Start the python rpc server
// ****************************************************************************
const createPyProc = ( ) => {
  
  let script = getScriptPath( )
  let port   = '' + selectPort( )

  pyProc = require( 'child_process' ).execFile( script, [ port ] )

  if ( pyProc != null ) {
    
    console.log( 'child process success on port ' + port )
  
  } // End if

} // End createPyProc( )



// ****************************************************************************
// Name: nullifyMainWindow
// Abstract: Set the main window to null when closing
// ****************************************************************************
const nullifyMainWindow = ( ) => {
    
  mainWindow = null

} // End nullifyMainWindow( )



// ****************************************************************************
// Name: createWindow
// Abstract: Create the window and set the necessary parameters
// ****************************************************************************
const createWindow = ( ) => {
 
  mainWindow = new BrowserWindow( 
    { 
  
      width:  800, 
      height: 600, 
      show:   false 
  
    } // End BrowserWindow
  
  ) // End mainWindow

  mainWindow.loadURL( 
    require( 'url' ).format( 
      
      {
      
        pathname: path.join( __dirname, 'frontend', 'pages', 'index.html' ),
        protocol: 'file:',
        slashes: true
      
      } // End format

    ) // End loadURL

  ) // End mainWindow
  
  // Shows web tools during debugging
  // Should be commented when building release
  mainWindow.webContents.openDevTools( )

  // When closing, nullify the Main Window
  mainWindow.on( 'closed', nullifyMainWindow )

 if ( loadingScreen ) {
    
    loadingScreen.close()
    
  } // End if
    
  mainWindow.show( )

} // End createWindow( )



// ****************************************************************************
// Name: createWindowIfNull
// Abstract: Creates the main window if the window is currently null
// ****************************************************************************
const createWindowIfNull = ( ) => {
 
  if ( mainWindow === null ) {
    
    createWindow( )
  
  } // End if

} // End createWindowIfNull( )



// ****************************************************************************
// Name: exitPyProc
// Abstract: Kill the python rpc server
// ****************************************************************************
const exitPyProc = ( ) => {

  pyProc.kill( )
  pyProc = null
  pyPort = null

} // End exitPyProc( )



// ****************************************************************************
// Name: quitApp
// Abstract: Needed for mac, when closing application, make sure to "quit" 
//           the application
// ****************************************************************************
const quitApp = ( ) => {
    
  if ( process.platform !== 'darwin' ) {
  
    app.quit( )
  
  } // End if

} // End nullifyMainWindow( )



// ****************************************************************************
// Name: quitApp
// Abstract: Needed for mac, when closing application, make sure to "quit" 
//           the application
// ****************************************************************************
const listenForPython = ( ) => {

  // Create the client for the server
  const zerorpc = require( "zerorpc" )
  let client = new zerorpc.Client( )

  // Connect to the rpc server
  client.connect( "tcp://127.0.0.1:4242" )

  // Check if the server is ready
  client.invoke( "echo", "server ready", ( error, res ) => {

    if( error || res !== 'server ready' ) {

      console.error( error ) 

    } else {

      console.log( "server is ready" )

      // Check if the server is ready
      client.invoke( "startDriver", ( error, res ) => {

        if( error || res !== 'success' ) {

          console.error( error )

        } else {

          console.log( "Chromium Backend Started" )

          createWindow( )

        } // End if

      }) // End invoke( "echo" )

    } // End if

  }) // End invoke( "echo" )

} // End listenForPython( )



// ****************************************************************************
// Name: appReady
// Abstract: When ready, launch loading screen and python server, wait until 
//           we hear from the python server, then create the main window
// ****************************************************************************
const appReady = ( ) => {

  createLoadingScreen( )

  createPyProc( )

  listenForPython( )

} // End appReady( )



// When ready, start the python rpc server
app.on( 'ready', appReady )

// When activated, if the mainWindow is null, then create the window
app.on( 'activate', createWindowIfNull )

// When closing, kill the python rpc server
app.on( 'will-quit', exitPyProc )

// Needed for mac, make sure the application actually quits when closed
app.on( 'window-all-closed', quitApp )
