const myModule = function() {
  let myArray = [12,233,3,24,511,6322]
  let myObject = {
    "foo": "bar",
    "baz": "boo"
  }
  let blocks = []

  let arr = document.getElementById("array")
  arr.onclick = printArray

  let obj = document.getElementById("object")
  obj.onclick = printObject

  let json = document.getElementById('json')
  json.onclick = outputJson

  let divbuilder = document.getElementById("divbuilder")
  divbuilder.onclick = buildDiv

  let req = document.getElementById("request")
  req.onclick = getRequest

  function getRequest() {
    clientIdButton = document.getElementById("clientId")
    id = clientIdButton.value
    clientIdButton.value = ""
    axios.get(`http://localhost:5000/clients/${id}`, {
      headers: {'credentials': 'include'},
    })
    .then(function (response) {
      buildDiv(response.data)
    })
  }

  function buildDiv(data) {
    let container = document.getElementById("divHolder")
    container.onclick = removeBlock

    let div = document.createElement('DIV')

    let overlay = document.createElement('DIV')
    overlay.classList.add("over")

    const card = createCard(data)

    div.id = "block"
    div.classList.add('individualBlock')
    div.appendChild(overlay)
    div.appendChild(card)

    container.appendChild(div)
  }

  function createCard(data) {
    let card = document.createElement('UL')
    card.classList.add('card')

    for(let i = 0; i < data.length; i++) {
      let listItem = document.createElement('LI')
      listItem.innerHTML = data[i]
      card.appendChild(listItem)
    }

    return card
  }

  function removeBlock(e) {
    e.target.parentNode.remove()
  }

  function outputJson() {
    let html = ""
    let textareaInput = document.getElementById("top-input")
    let bottom = document.querySelector(".bottom")
    let input = JSON.parse(textareaInput.value)

    if (Array.isArray(input)) {
      html = "Array<br/>"
      bottom.innerHTML = html + printArray(null, input)
    } else {
      html = "Object<br/>"
      bottom.innerHTML = html + printObject(null, input)
    }
  }

  function printObject(e, obj = {}) {
    let tempString = "";

    if(Object.keys(obj).length === 0) {
      for (let value in myObject) {
        console.log(value + " : " + myObject[value]);
      }
      return;
    } else {
      for (let value in obj) {
        tempString += value + " : " + obj[value] + "<br/>";
      }
      return tempString;
    }
  }

  function printArray(e, arr = []) {
    let temp = "";
    let min = document.getElementById("min")
    let max = document.getElementById("max")

    if(arr.length === 0) {
      myArray.forEach((x, y) => {
        console.log("key: " + y + " value: " + x);
        temp += "key: " + y + " value: " + x + "<br/>";
      })
    } else {
      for(let i = 0; i < arr.length; i++) {
        temp += (arr[i] + "<br/>");
      }

      max.innerHTML = Math.max(...arr)
      min.innerHTML = Math.min(...arr)
    }

    return temp;
  }

  return {
    
  }
}();