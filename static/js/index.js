function crear_producto(){
    document.getElementById("carrusel").style.display="none";
    document.getElementById("mostrar-producto").style.display="none";
    document.getElementById("agregar-producto").style.display= "flex";   
}

function mostrar_producto(){
    document.getElementById("carrusel").style.display="none";
    document.getElementById("mostrar-producto").style.display="flex";
    document.getElementById("agregar-producto").style.display= "none";   
}

function home(){
    document.getElementById("carrusel").style.display="flex";
    document.getElementById("mostrar-producto").style.display="none";
    document.getElementById("agregar-producto").style.display= "none";   
}