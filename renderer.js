// Require jquery
const jquery = require( 'jquery' )
window.$ = window.jQuery=jquery;

// Create the client for the server
const zerorpc = require( "zerorpc" )
let client = new zerorpc.Client( )

// Get a reference to the formula and result elements
let formula = document.querySelector( '#formula' )
let result  = document.querySelector( '#result'  )

// Require some chromium things
const chromium = require( "chromium" )
//const chrome_driver = require( "electron-chromedriver" )




// Connect to the rpc server
client.connect( "tcp://127.0.0.1:4242" )



// Check if the server is ready
client.invoke( "echo", "server ready", ( error, res ) => {

  if( error || res !== 'server ready' ) {

    console.error( error ) 

  } else {

    console.log( "server is ready" )

  } // End if

}) // End invoke( "echo" )



// Check if the server is ready
client.invoke( "startChromiumBackend", ( error, res ) => {

  if( error || res !== 'success' ) {

    console.error( error ) 

  } else {

    console.log( "Chromium Backend Started" )

  } // End if

}) // End invoke( "echo" )



// ****************************************************************************
// Name: calculate
// Abstract: Send the formula to the server to calculate it
// ****************************************************************************
const calculate = ( ) => {
  
  client.invoke( "calc", formula.value, ( error, res ) => {
  
    if( error ) {
  
      console.error( error )
  
    } else {
  
      result.textContent = res
  
    } // End if
  
  }) // End invoke( "calc" )

} // End getScriptPath( )



// Add an event listener to formula
formula.addEventListener( 'input', calculate ) // End EventListener

// Calculate the default prefilled equation
formula.dispatchEvent( new Event( 'input' ) )