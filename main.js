const electron = require( 'electron' )
const app = electron.app
const BrowserWindow = electron.BrowserWindow
const path = require( 'path' )


/*************************************************************
 * py process
 *************************************************************/

const PY_DIST_FOLDER = 'py_out'
const PY_FOLDER      = 'py_src'
const PY_MODULE      = 'api'    // without .py suffix

let pyProc = null
let pyPort = null



const getScriptPath = ( ) => {
  
  if ( process.platform === 'win32' ) {

    return path.join( __dirname, PY_DIST_FOLDER, PY_MODULE + '.exe' )

  }

  return path.join( __dirname, PY_DIST_FOLDER, PY_MODULE )

}



const selectPort = ( ) => {

  pyPort = 4242

  return pyPort

}



const createPyProc = ( ) => {
  
  let script = getScriptPath( )
  let port   = '' + selectPort( )

  pyProc = require( 'child_process' ).execFile( script, [ port ] )

  if ( pyProc != null ) {
    
    console.log( 'child process success on port ' + port )
  
  }

}



const exitPyProc = ( ) => {

  pyProc.kill()
  pyProc = null
  pyPort = null

}



app.on( 'ready', createPyProc )
app.on( 'will-quit', exitPyProc )



/*************************************************************
 * window management
 *************************************************************/

let mainWindow = null



const createWindow = ( ) => {
 
  mainWindow = new BrowserWindow( { width: 800, height: 600 } )
  mainWindow.loadURL( require( 'url' ).format( {
    pathname: path.join( __dirname, 'gui', 'index.html' ),
    protocol: 'file:',
    slashes: true
  } ) )
  
  mainWindow.webContents.openDevTools( )

  mainWindow.on( 'closed', ( ) => {
    
    mainWindow = null
  
  })

}



app.on( 'ready', createWindow )



app.on( 'window-all-closed', ( ) => {
  
  if ( process.platform !== 'darwin' ) {
  
    app.quit( )
  
  }

})



app.on( 'activate', ( ) => {
 
  if ( mainWindow === null ) {
    
    createWindow()
  
  }

})