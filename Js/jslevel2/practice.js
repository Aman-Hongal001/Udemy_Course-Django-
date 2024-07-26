// function helloYou(name){
//     console.log("Hello "+name);
// }

// function addNum(num1,num2){
//     console.log(num1+num2);
// }

// function names(name = "Aman"){
//     console.log(name);
// }

// function formal(name="Sam", title="Sir"){
//     return title+" "+name
// }

// //scope

// var v = "Global V"
// var stuff = "Global Staff"

// function fun(stuff){
//     console.log(v);
//     stuff = "Reassign stuff inside fun"
//     console.log(stuff);
// }

// fun()
// console.log(stuff);


//exercises
//1
function sleepIn(weekday, vacation){
    return (!weekday || vacation)
}

//2

function monkeytrouble(aSmile,bSmile){
    return ((aSmile && bSmile)||(!aSmile && !bSmile))
}

//3
function stringTimes(str,n){
    var returnstr = "";
    var i = 0;
    while(i<n){
        returnStr += str
        i++
    }
}

//4

function luckuSum(a,b,c){
    if(a == 13){
        return 0
    }
    else if(b == 13){
        return a
    }
    else if(c == 13){
        return a+b
    }
    else{
        return a+b+c
    }
}
