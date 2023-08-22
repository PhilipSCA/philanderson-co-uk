// var
    var favoriteFood = 'pizza'
    var numOfSlices = 8
    console.log(favoriteFood)
    console.log(numOfSlices)



// let
    let changeMe = true;
    changeMe = false;
    console.log(changeMe)

    let food;
    console.log(food)
    food = 50; // wrong

    console.log(food) // right



// const
// a const cannot be reassigned like let and var, you'll get a TypeError
    const entree = 'Enchiladas';
    console.log(entree)
    // entree = 'Tacos' // you cant do that, it will give you an error


let levelUp = 10;
let powerLevel = 9001;
let multiplyMe = 32;
let quarterMe = 1152;

levelUp += 5; // adding 5 to 'levelUp'
powerLevel -= 100; // subtracting 100 to 'powerLevel'
multiplyMe *= 11; // multiplying 11 to 'multiplyMe'
quarterMe /= 4; // dividing 4 to 'quarterMe'

console.log('The value of levelUp:', levelUp); 
console.log('The value of powerLevel:', powerLevel); 
console.log('The value of multiplyMe:', multiplyMe); 
console.log('The value of quarterMe:', quarterMe);

let gainedDollar = 3;
let lostDollar = 50;

gainedDollar++; // add 1 (++)
lostDollar--; // take away 1 (--)