

function fuckMyAss(){
    confirm("you just fucked my ass!!?!")
}

function fuckMe(x){
    confirm("you just fucked me in the ass!!!");
}

let topTen= ['Volkswagen',
 'Opel',
 'Ford',
 'Skoda',
 'Renault',
 'Audi',
 'BMW',
 'Mercedes-Benz',
 'SEAT',
 'Hyundai']
// let list =document.getElementById('topTen')
//
// for (i=0; i<topTen.length,++i){
//     let li= document.createElement('li');
//     li.innerText=topTen[i]
//     list.appendChild(li)
// }



for (i=0; i<topTen.length;i++){
 var li = document.createElement('li')
 var text =document.createTextNode(topTen[i])
 li.appendChild(text)
 document.getElementById('topTenner').appendChild(li)
}