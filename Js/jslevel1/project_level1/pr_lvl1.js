var fname = prompt("Enter your first name : ")
var lname = prompt("Enter your last name : ")
var height = prompt("Enter your height in cm : ")
var age = prompt("Enter your age : ")
var petname = prompt("Enter your petname : ")
alert("Thank you for ur response")


var namecon = null;
var agecon = null;
var heightcon = null;
var petcond = null;


//namecond
if(fname[0]===lname[0]){
    namecon = true;
}
else{
    namecon = false;
}

//agecond
if(age > 20 && age < 30){
    agecon = true;
}
else{
    agecon = false;
}

//heightcon
if(height >= 170){
    heightcon = true;
}
else{
    heightcon = false;
}

//petcond
if(petname[petname.length - 1]){
    petcond = true;
}
else{
    petcond = false;
}


// count = false
if(namecon && agecon && heightcon && petcond){
    console.log("This is a secrete message")
}
else{
    console.log("Sorry Nothing to see here");
}