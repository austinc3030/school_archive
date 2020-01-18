const path = require('path');
var child = require('child_process').execFile;

function handler() {

  var current_dir = __dirname;
  var python_dir = path.join( current_dir, '..', 'py_out' );
  var python_file = path.join( python_dir, 'pytest1' );

  var executablePath = python_file;

  var result = document.getElementById("result").value;
  var parameters = [result];   
 
  child(executablePath, parameters, function(err, data) {
  //child(executablePath, function(err, data) {
       console.log(err)
       //console.log(data.toString());
       document.getElementById("result").value = data.toString();
  });

}
