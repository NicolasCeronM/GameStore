function agregarAlCarro(productoId) {
    $.ajax({
        url: "{% url 'carro:agregar' producto_id=0 %}".replace('0', productoId),
        type: 'GET',
        success: function(response) {
            Swal.fire({
                position: "top-end",
                icon: "success",
                title: "Agregado al carro",
                showConfirmButton: false,
                timer: 1500
            });
        },
        error: function(error) {
            alert("Hubo un error al agregar el producto al carro.");
        }
    });
}