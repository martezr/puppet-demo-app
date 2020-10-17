function myFunction() {
  var request = new XMLHttpRequest()
  request.open('GET', 'http://passwordservice:8001/api/password', true)
  request.onload = function () {
    // Begin accessing JSON data here
    var data = JSON.parse(this.response)
    if (request.status >= 200 && request.status < 400) {
      console.log(data)
      document.getElementById('generated-password').innerHTML = data.password
    } else {
      document.getElementById('generated-password').innerHTML = "Unable to reach service"
    }
  }
  request.send()

  var nameRequest = new XMLHttpRequest()
  nameRequest.open('GET', 'http://nameservice:8000/api/name', true)
  nameRequest.onload = function () {
    // Begin accessing JSON data here
    var data = JSON.parse(this.response)
    if (nameRequest.status >= 200 && nameRequest.status < 400) {
      console.log(data.name)
      document.getElementById('generated-name').innerHTML = data.name
    } else {
      document.getElementById('generated-name').innerHTML = "Unable to reach service"
    }
  }
  nameRequest.send()


}