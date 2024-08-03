let greeting = document.getElementById("text")
let container = document.getElementById("data-container")

// 'click me' button that should dislay the data
let button = document.getElementById('myButton')
button.onclick = displaystuff

// 'whoa another one' button to call the coolapi to make sure it works
let button2 = document.getElementById('secondButton')
button2.onclick = checkItWorks

// to complete
function displaystuff() {
  greeting.textContent = ''
  container.innerHTML = ''
  fetch('/api/data')
    .then(response => response.json())
    .then(data => {
    for (let i=0; i<4; i++) {
        let item = data[i]
        let p = document.createElement('p')
        p.textContent = 'Name: ' + item["name"] + ', Age: ' + (item["age"]).toString()
        container.appendChild(p)
    }
    })
}

// to check it works
function checkItWorks() {
  console.log("function called")
  fetch('/coolapi')
    .then(response => response.json())
}