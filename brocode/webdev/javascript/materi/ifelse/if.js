//if statement

const mytext = document.getElementById("mytext");
const mysubmit = document.getElementById("mybutton");
const resulti = document.getElementById("result");

mysubmit.onclick = function() {
    let umur = Number(mytext.value); // Convert the input value to a number

    if (isNaN(umur)) {
        resulti.textContent = `Masukkan angka yang valid`; // Check if input is a number
    }
    else if (umur >= 100) {
        resulti.textContent = `Umur tidak masuk akal`; // If age is 100 or more
    }
    else if (umur === 0) {
        resulti.textContent = `Kamu baru lahir`; // If age is 0
    }
    else if (umur >= 18) {
        resulti.textContent = `Selamat datang`; // If age is 18 or more
    }
    else if (umur < 0) {
        resulti.textContent = `Umur tidak boleh negatif`; // If age is less than 0
    }
    else {
        resulti.textContent = `Kamu dibawah umur`; // If age is under 18 but above 0
    }
};



//contoh
/*

let umur = 11;

if(umur >= 18){
    console.log("you are old");
}
else{
    console.log("you are kid");
}

let jam = 10;

if(jam > 12 ){
    console.log("selamat siang");
}
else{
    console.log("selamat pagi");
}

let korupsi = false;

if(korupsi){
    console.log("pengkorup");
}
else{
    console.log("suci!")
}

let age = 18;
let korup = false;

if(age >= 18){
    console.log("kamu dewasa");
    if(korup){
        console.log("kamu pengkorup");
    }
    else{
        console.log("kamu bukan pengkorup")
    } 
}
else{
    console.log("kamu kid");
}

let umur = 0;
if(umur >= 100){
    console.log("umur tidak masuk akal");
}
else if(umur == 0){
    console.log("kamu baru lahir");
}
else if(umur >= 18){
    console.log("selamat datang");
}
else if(umur < 0){
    console.log("umur tidak boleh 0");
}
else{
    console.log("kamu dibawah umur");
}
*/ 