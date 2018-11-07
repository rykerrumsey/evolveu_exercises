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
    axios.get('http://www.google.ca')
      .then(function (response) {
        console.log(response)
      });
  }

  function buildDiv() {
    let container = document.getElementById("divHolder")
    let div = document.createElement('DIV')
    let text = document.createTextNode(blocks.length)

    div.id = blocks.length
    div.classList.add('individualBlock')
    div.onclick = removeBlock
    div.appendChild(text)

    container.appendChild(div)

    blocks.push(blocks.length)
  }

  function removeBlock(e) {
    let block = e.target
    block.remove()
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
    if(arr.length === 0) {
      myArray.forEach((x, y) => {
        console.log("key: " + y + " value: " + x);
        temp += "key: " + y + " value: " + x + "<br/>";
      })
    } else {
      for(let i = 0; i < arr.length; i++) {
        temp += (arr[i] + "<br/>");
      }
    }

    return temp;
  }

  return {
    
  }
}();