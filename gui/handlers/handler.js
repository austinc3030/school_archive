let {PythonShell} = require('python-shell')
var path = require("path")


function handler() {

  var result = document.getElementById("result").value
  
  var options = {
    scriptPath : path.join(__dirname, '/../python/'),
    args : [result]
  }

  let pyshell = new PythonShell('python.py', options);


  pyshell.on('message', function(message) {
      document.getElementById("result").value = message;
  })
}
