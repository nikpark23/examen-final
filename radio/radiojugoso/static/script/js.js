document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var nombre = document.getElementById('nombre').value;
    var apellido = document.getElementById('apellido').value;
    var correo = document.getElementById('correo').value;
    var pais = document.getElementById('pais').value;
    var mensaje = document.getElementById('mensaje').value;

    if(nombre === "" || apellido === "" || correo === "" || pais === "" || mensaje === "") {
        alert("Todos los campos son obligatorios.");
        return false;
    }

    if(!correo.includes("@")) {
        alert("Por favor, introduce una dirección de correo electrónico válida.");
        return false;
    }

    alert("Formulario enviado exitosamente.");
    return true;
});

