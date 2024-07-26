var simple = {
    prop : "Hello",
    myMethod : function(){
        console.log("The myMethod was called");
    }
}

var myObj = {
    name : "Aman",
    greet : function(){
        console.log("Hello "+this.name);
    }
}

//excercises
//1

var employee = {
    name : "John Smith",
    job : "Programmer",
    age : 31,
    nameLength : function(){
        console.log(this.name.length)
    }
}
// var nameLen = employee['name'].length
// console.log("The length of name is: "+nameLen)

//2
var employee = {
    name : "John Smith",
    job : "Programmer",
    age : 31,
    report : function(){
        alert("Name is "+this.name+" Job is "+this.job+" Age is "+this.age)
    }
}

// for (const key in employee) {
//     alert(key+" is "+this.key)
// }

//3
var employee = {
    name : "John Smith",
    job : "Programmer",
    age : 31,
    lastName : function(){
        console.log(this.name.split(" ")[1]);
    }
}
