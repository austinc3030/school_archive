// Require jquery
const jquery = require( 'jquery' )
window.$ = window.jQuery=jquery;

// Create the client for the server
const zerorpc = require( "zerorpc" )
let client = new zerorpc.Client( )

// Get a reference to the formula and result elements
let formula = document.querySelector( '#formula' )
let result  = document.querySelector( '#result'  )



// Connect to the rpc server
client.connect( "tcp://127.0.0.1:4242" )



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