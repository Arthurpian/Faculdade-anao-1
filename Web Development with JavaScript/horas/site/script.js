//Retornado hora

let horas = new Date() // isso e istancia
document.write(horas.getHours());
document.write("<br><br>");

//Retornado minutos

let minutos = new Date()
document.write(minutos.getMinutes());
document.write("<br><br>");

//Retornado segundos

let segundos = new Date()
document.write(segundos.getSeconds());
document.write("<br><br>");

//Setando horas

let horas1 = new Date()
horas1.setHours(horas1.getHours()+3);
document.write(horas1.getHours());
document.write("<br><br>");

//Setando minutos

let minutos1 = new Date()
minutos1.setMinutes(minutos1.getMinutes()+8);
document.write(minutos1.getMinutes());
document.write("<br><br>");

//Setando segundos

let segundos1 = new Date()
segundos1.setSeconds(segundos1.getSeconds()+20);
document.write(segundos1.getSeconds());
document.write("<br><br>");

//Usando o setTimeout

function BemVindo(){
    alert("Seja bem vindo")
}
setTimeout(BemVindo,1000)