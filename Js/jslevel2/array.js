//arr with strings are immutable means cannot change
//numbers can be mutable 
var arr = [];

function addNew(){
    var newName = prompt("Enter the name to add")
    arr.push(newName)
}

function remove(){
    var remName = prompt("Enter the name to remove")
    var index = arr.indexOf(remName)
    arr.splice(index,1)
}

function display(){
    console.log(arr);
}

var start = prompt("Would u like to start? y/n ")
var select = "empty"
if (start=='y'){
    while(select !== "quit"){
         select = prompt("Enter the operation: add, remove, display or quit")
        if(select === "add"){
            addNew()
        }
        else if(select === "remove"){
            remove()
        }
        else if(select === "display"){
            display()
        }
        else{
            alert("not recongnised")
        }
    }
    
}