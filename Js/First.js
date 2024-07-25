var ham = 10;
var cheese = 10;

var report = "Blank";

if(ham >= 10 && cheese >= 10){
    report = "Strong sales of both ham and cheese!"
}
else if(ham == 0 && cheese == 0){
    report = "Nothing Sold!"
}
else{
    report = "We had some sales of items"
}

console.log(report)