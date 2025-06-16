// ini adalah komen

/*
  ini juga komen

*/


//console log digunakan untuk memprint out. console ini bisa jadi tiga : console.log("halo"), console.log('ehlo'), console.log(`hola`)
console.log(`halo dunia`);

console.log(`saya suka bubur`);

/*untuk pop up notifikasi

window.alert(`ini adalah peringatan`);

window.alert(`saya suka tahu bulat`)

*/

//untuk menampilkan text dengan js dengan id html, perhatikan huruf kapitalnya 
document.getElementById("judula").textContent = `Halo`;

document.getElementById("para1").textContent = `saya belajar js di brocode`;

//variable menyimpan data
//declaration             let x;  atau  let x = 100;
//assignment              x = 10;
let x;
x = 100;

console.log(x);

let nama = `sans`;
let makan = `tahu`;
let email = `fake@mail.com`;

//untuk mengetahui jenis variable
console.log(typeof nama);

//untuk mengabungkan string dan variable, string perlu `tanda`
console.log(`makanan favoritmu ${makan}`);
console.log(`email kamu adalah ${email}`);

//boolean true; or false;
let online = true;
let offline = false;

console.log(`bro is offline ${offline}`)
console.log(`bro is online ${online}`);

//penggunaan string dan variable untuk di print out di console
let negara = `wakanda`;
let pejabat = `dewan korupsi`;
let sdm = true;

document.getElementById("v1").textContent = `kamu orang ${negara}`;
document.getElementById("v2").textContent = `negaramu penuh ${pejabat}`;
document.getElementById("v3").textContent = `sdm rendah : ${sdm}`;

//operasi aritmatik

//pengurangan
let suap = 1000;

suap = suap - 200;

console.log(suap);

//pertambahan
let tam = 100;

tam = tam + suap;

console.log(tam);

//perkalian
let dikal = 2;
dikal = tam * dikal;

console.log(dikal);

//pembagian
let bagihasil = 8;
bagihasil = dikal / bagihasil;

console.log(bagihasil);

//perpangkatan
let warga = 50;
warga = warga ** 2;

console.log(warga);

// % = 9:9 = 1
let rakyat = warga - 2450;

rakyatbaru = rakyat % 3;

console.log(rakyatbaru);

//shortcut atau single penggunaan
pelanggar = 30;

pelanggar += 1;
pelanggar -= 5;
pelanggar *= 2;
pelanggar %= 4;
pelanggar /= 2;
pelanggar **= 2;

pelanggar ++;
pelanggar --;

console.log(pelanggar);

//user input

//easy way

//let username;
//username = window.prompt("what is your name?");

//console.log(username);


//prof way

let username;

document.getElementById("b1").onclick = function(){
  username = document.getElementById("mt1").value;
  document.getElementById("mh1").textContent = `hello ${username}`;

}

//data conversion

let nami = window.prompt("umur?");
nami = Number(nami);
nami+=1;

console.log(nami, typeof nami);


let q = "pizza";
let w = "rois";
let r = "riki";

q = Number(q);
w = String(w);
r = Boolean(r);

console.log(q, typeof q);
console.log(w, typeof w);
console.log(r, typeof r);

//const = variable yang tidak bisa berubah

const PI = 3.14159;
let radius;
let circumference;

PI = 1233333

radius = window.prompt('enter radius of a circle');
radius = Number(radius);

circumference = 2 * PI * radius;

console.log(circumference);










