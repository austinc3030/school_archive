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
const PY_DIST_FOLDER = 'py_out'
const PY_FOLDER      = 'py_src'
const PY_MODULE      = 'api'    // without .py suffix

// Create variables for the python process and port
let pyProc = null
let pyPort = null



// ****************************************************************************
// Name: getScriptPath
// Abstract: Build the path to the python rpc server
// ****************************************************************************
const getScriptPath = ( ) => {
  
  if ( process.platform === 'win32' ) {

    return path.join( __dirname, PY_DIST_FOLDER, PY_MODULE + '.exe' )

  } // End if

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
 
  mainWindow = new BrowserWindow( { width: 800, height: 600 } )

  mainWindow.loadURL( 
    require( 'url' ).format( 
      {
        pathname: path.join( __dirname, 'gui', 'index.html' ),
        protocol: 'file:',
        slashes: true
      } 
    ) 
  )
  
  // Shows web tools during debugging
  // Should be commented when building release
  mainWindow.webContents.openDevTools( )

  // When closing, nullify the Main Window
  mainWindow.on( 'closed', nullifyMainWindow )

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



// When ready, start the python rpc server
app.on( 'ready', createPyProc )

// When the app is ready, create the window
app.on( 'ready', createWindow )

// When activated, if the mainWindow is null, then create the window
app.on( 'activate', createWindowIfNull )

// When closing, kill the python rpc server
app.on( 'will-quit', exitPyProc )

// Needed for mac, make sure the application actually quits when closed
app.on( 'window-all-closed', quitApp )