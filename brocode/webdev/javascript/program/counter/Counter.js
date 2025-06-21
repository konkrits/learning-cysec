// program berhitung

const decrease = document.getElementById("Decrease");    //pertama buat variable dan ambil dulu id tiap tiap tombolnya
const increase = document.getElementById("Increase");
const reset = document.getElementById("Reset");
const countLabel = document.getElementById("count");     //buat variable untuk nom

let count = 0;                                          //membuat variable count untuk memberi angka dan menampilkan ke layar

Increase.onclick = function(){                          //ketika kita mengklik tombol increase 
    count ++;                                           //variable count akan bertambah 
    countLabel.textContent = count;                     //dan kita menampilkan angka yang ditambahkan dengan cara variable countLabel dan menggunakan .textContent menjadikan variable count
}

Decrease.onclick = function(){
    count --;
    countLabel.textContent = count;
}

Reset.onclick = function(){
    count = 0                                           //count = 0 artinya kita menjadikan variable count 0 ketika kita mengklik reset
    countLabel.textContent = count;                 
}
