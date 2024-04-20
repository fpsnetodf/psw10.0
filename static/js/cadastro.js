nome = document.querySelector('span.color-dark')
      
console.log("O nome encontrado foi:",nome.textContent)
let estilo = {
    color: "blue", 
    fontSize: "24px",
}
Object.assign(nome.style, estilo)