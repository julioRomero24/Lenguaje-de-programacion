
$('#formulario').on('submit', function (e) {
    e.preventDefault();
    $.ajax({
        url: '/',
        data: $('form').serialize(),
        type: 'POST',
        success: function (texto) {
            if(texto) {
                document.getElementById('salida').innerHTML = texto;
                document.getElementById('txt').innerHTML = 'Compilación éxitosa';
                document.getElementById('txt').style.color="#001bff";
            } else {
                document.getElementById('salida').innerHTML = '';
                document.getElementById('txt').innerHTML = 'Error de sintaxis';
                document.getElementById('txt').style.color="red";
            }
        },
        error: function (texto) {
            cdocument.getElementById('salida').innerHTML = 'Debe ingresar una expresión gramatical' + texto;
        }
    })
});