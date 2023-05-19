function CalcQuadrado(){
    let numeros = document.getElementById("numeros").value;
    numeros = numeros.split(",");
    for(i=0;i<numeros.length;i++){
        quadrado = parseInt(numeros[i]) * parseInt(numeros[i]);
        document.write("O quadrao de" +numeros[i]+" é " + quadrado+"<br>") 
    }
}