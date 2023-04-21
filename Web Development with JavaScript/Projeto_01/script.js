function validar(){

    let usuario = document.getElementById("usuario").value
    let senha = document.getElementById("senha") .value

    if(usuario == "" && senha == ""){  /*Se não tiver nada escrito faça*/ 
        alert("Preencha todos os campos")
    }else{
        alert("Acesso permitido")
        window.open('menu.html') /*chama o arquivo*/
    }
}

function cal(){
    let num1 = Number(prompt("Digite o primeiro número"))
    let num2 = Number(prompt("Digite o segundo número"))
    let op = Number(prompt(' Escolha uma opção: ${num1} e ${num2}. \n [1]somar '))
    
    let msg = document.getElementById('msg')
    msg.innerHTML = '<h2>Resultado...</h2>'

    switch(op){
        case 1:
            msg.innerHTML += ' <p>${num1} + ${num2} = <strong> ${num1+num2} </strong> </p>'
            break
        case 2:
            msg.innerHTML += ' <p>${num1} - ${num2} = <strong> ${num1-num2} </strong> </p>'
            break
        case 3:
            msg.innerHTML += ' <p>${num1} * ${num2} = <strong> ${num1*num2} </strong> </p>'
            break
        case 4:
            msg.innerHTML += ' <p> ${num1} / ${num2} = <strong> ${num1/num2} </strong> </p>'
            break
        
        default:
            msg.innerHTML += '<p>Opção invailida</p>'
    }
}