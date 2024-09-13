function agregarAlCarro(productoId) {
  $.ajax({
    url: `/carro/agregar/${productoId}`,
    type: "GET",
    success: function (response) {
      Swal.fire({
        position: "top-end",
        icon: "success",
        title: "Agregado al carro",
        showConfirmButton: false,
        timer: 1500,
      });
    },
    error: function (error) {
      Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Hubo un error al agregar el producto al carro.",
        footer: '<a href="#">Why do I have this issue?</a>'
      });
    },
  });
}
