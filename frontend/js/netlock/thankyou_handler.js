// Require jquery
const jquery = require( 'jquery' )
window.$ = window.jQuery=jquery;

// Create the client for the server
const zerorpc = require( "zerorpc" )
let client = new zerorpc.Client( )

// Get a reference to the elements
let gobacktologinnew = document.querySelector( '#gobacktologinnew' )
let gobacktossid = document.querySelector( '#gobacktossid' )
let gobacktofeature = document.querySelector( '#gobacktofeature' )
let gobacktoencryption = document.querySelector( '#gobacktoencryption' )



// Connect to the rpc server
client.connect( "tcp://127.0.0.1:4242" )



// ****************************************************************************
// Name: fgobacktologinnew
// Abstract: Go back to the loginnew screen
// ****************************************************************************
const fgobacktologinnew = ( ) => {
  
    window.location.href = 'loginnew.html'

} // End fgobacktologinnew( )

// ****************************************************************************
// Name: fgobacktossid
// Abstract: Go back to the ssid screen
// ****************************************************************************
const fgobacktossid = ( ) => {

    window.location.href = 'ssid.html'

} // End fgobacktossid( )

// ****************************************************************************
// Name: fgobacktofeature
// Abstract: Go back to the feature screen
// ****************************************************************************
const fgobacktofeature = ( ) => {

    window.location.href = 'feature.html'

} // End fgobacktofeature( )

// ****************************************************************************
// Name: fgobacktoencryption
// Abstract: Go back to the encryption screen
// ****************************************************************************
const fgobacktoencryption = ( ) => {

    window.location.href = 'encryption.html'

} // End fgobacktoencryption( )



// Add an event listener to formula
gobacktologinnew.addEventListener( 'click', fgobacktologinnew ) // End EventListener
gobacktossid.addEventListener( 'click', fgobacktossid ) // End EventListener
gobacktofeature.addEventListener( 'click', fgobacktofeature ) // End EventListener
gobacktoencryption.addEventListener( 'click', fgobacktoencryption ) // End EventListener