// Require jquery
const jquery = require( 'jquery' )
window.$ = window.jQuery=jquery;

// Create the client for the server
const zerorpc = require( "zerorpc" )
let client = new zerorpc.Client( )

// Get a reference to the signin
let next = document.querySelector( '#next' )
let goback = document.querySelector( '#goback' )


// Connect to the rpc server
client.connect( "tcp://127.0.0.1:4242" )



// ****************************************************************************
// Name: fnext
// Abstract: Move to the next page
// ****************************************************************************
const fnext = ( ) => {

    window.location.href = 'thankyou.html'

} // End fsignin( )



// ****************************************************************************
// Name: fgoback
// Abstract: Move to the next page
// ****************************************************************************
const fgoback = ( ) => {

    window.location.href = 'feature.html'

} // End fgoback( )



// Add an event listener to signin
next.addEventListener( 'click', fnext ) // End EventListener

// Add an event listener to goback
goback.addEventListener( 'click', fgoback ) // End EventListener