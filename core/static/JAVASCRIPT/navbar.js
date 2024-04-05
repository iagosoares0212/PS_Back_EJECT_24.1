let mostrar = true;

const menuBarra = document.querySelector(".menu_barra");
const menuInteragir = menuBarra.querySelector(".hamburger");

menuInteragir.addEventListener("click", () =>{
    document.body.style.overflow = mostrar ? "hidden" : "initial"
    menuBarra.classList.toggle("ativo", mostrar);
    mostrar = !mostrar;
})
//testar com display none e block
