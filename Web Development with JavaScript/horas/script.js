let temp
function tempo(){
    let relogio = document.querySelector('#main')
    let hora = new Date()    // toLocaleString pega o relogio para estados unidos
    relogio.innerHTML = (hora.toLocaleString()).slice(-11) // ate 8 digitos
}
document.querySelector('#ligar').addEventListener('click', () =>{
    temp = setInterval(tempo,1000)
})
document.querySelector('#desligar').addEventListener('click', () =>{
    clearInterval(temp) // esse comando faz parar 
})