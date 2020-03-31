// Require jquery
const jquery = require( 'jquery' )
window.$ = window.jQuery=jquery;

// Create the client for the server
const zerorpc = require( "zerorpc" )
let client = new zerorpc.Client( )

// Get a reference to the signin
let signin = document.querySelector( '#signin' )
let goback = document.querySelector( '#goback' )


// Connect to the rpc server
client.connect( "tcp://127.0.0.1:4242" )



// ****************************************************************************
// Name: fsignin
// Abstract: Move to the next page
// ****************************************************************************
const fsignin = ( ) => {

    window.location.href = 'loginnew.html'

} // End fsignin( )



// ****************************************************************************
// Name: fgoback
// Abstract: Move to the next page
// ****************************************************************************
const fgoback = ( ) => {

    window.location.href = 'index.html'

} // End fgoback( )



// Add an event listener to signin
signin.addEventListener( 'click', fsignin ) // End EventListener

// Add an event listener to goback
goback.addEventListener( 'click', fgoback ) // End EventListener