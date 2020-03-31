// Require jquery
const jquery = require( 'jquery' )
window.$ = window.jQuery=jquery;

// Create the client for the server
const zerorpc = require( "zerorpc" )
let client = new zerorpc.Client( )

// Get a reference to the letsgetstarted
let letsgetstarted = document.querySelector( '#letsgetstarted' )



// Connect to the rpc server
client.connect( "tcp://127.0.0.1:4242" )



// ****************************************************************************
// Name: fletsgetstarted
// Abstract: Move to the next page
// ****************************************************************************
const fletsgetstarted = ( ) => {
  
    window.location.href = 'login.html'

} // End letsgetstarted( )



// Add an event listener to letsgetstarted
letsgetstarted.addEventListener( 'click', fletsgetstarted ) // End EventListener