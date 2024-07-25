function helloYou(name){
    console.log("Hello "+name);
}

function addNum(num1,num2){
    console.log(num1+num2);
}

function names(name = "Aman"){
    console.log(name);
}

function formal(name="Sam", title="Sir"){
    return title+" "+name
}

//scope

var v = "Global V"
var stuff = "Global Staff"

function fun(stuff){
    console.log(v);
    stuff = "Reassign stuff inside fun"
    console.log(stuff);
}

fun()
console.log(stuff);
