let x = 5;
if (x == 4){
    console.log(`bravooo`)
};

const newObjectList = {
    'name':'test'
}

alert(newObjectList['name'])

const cars = ["BMW", "Volvo", "Saab", "Ford", "Fiat", "Audi"];

let text = "";
for (let i = 0; i < cars.length; i++) {
  text += cars[i] + "<br>";
}

document.getElementById("demo").innerHTML = text;