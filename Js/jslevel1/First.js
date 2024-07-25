// var ham = 10;
// var cheese = 10;

// var report = "Blank";

// if(ham >= 10 && cheese >= 10){
//     report = "Strong sales of both ham and cheese!"
// }
// else if(ham == 0 && cheese == 0){
//     report = "Nothing Sold!"
// }
// else{
//     report = "We had some sales of items"
// }

// console.log(report)


//while loop in js

// var x = 0;

// while (x < 5){
//     console.log("x is currently: "+x)
//     if(x === 3){
//         console.log("x is equal to three!")
//     }
//     console.log("x is still less than 5, Adding 1 to x")
//     x=x+1
// }
// console.log("task complete")


// var num = 0;

// while (num <= 10){
//     if(num%2 === 0){
//         console.log(num)
//     }
//     num = num+1
// }




// for loop
// var word = "ABCDEFGHI";

// for (let i = 0; i < word.length; i++) {
//     console.log(word[i]);
// }



//loop excercise
// problem 1

word1 = "hello"
var j = 0;
for (let i = 0; i < 5; i++) {
    console.log(word1+" with for loop")
}


while(j < 5){
    console.log(word1)
    j++;
}


// problem 2

var x = 1
while(x < 26){
    if(x%2 != 0){
        console.log(x+" with while")
    }
    x++
}

for(var y=0;y<26;y++){
    if(x%2 != 0){
        console.log(x+" with for")
    }
}