var restart = document.querySelector('#bt');

var squares = document.querySelectorAll('td');

function clearBoard(){
    for (let i = 0; i < squares.length; i++) {
        squares[i].textContent = '';
    }
}

restart.addEventListener('click',clearBoard)

//basic solution
// var cellOne = document.querySelector('#one');

// cellOne.addEventListener('click',function(){
//     if(cellOne.textContent === ''){
//         cellOne.textContent = 'X';
//     }else if(cellOne.textContent === 'X'){
//         cellOne.textContent = 'O';
//     }else{
//         cellOne.textContent = '';
//     }
// })


//using this keyword

function changeMarker(){
    if(this.textContent === ''){
        this.textContent = 'X';
    }else if(this.textContent === 'X'){
        this.textContent = 'O';
    }else{
        this.textContent = '';
    }
}

for (let i = 0; i < squares.length; i++) {
    squares[i].addEventListener('click',changeMarker)
}