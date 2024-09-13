function eliminarCarro(productoId) {
  $.ajax({
    url: `/carro/eliminar/${productoId}`,
    type: "GET",
    success: function (response) {
      Swal.fire({
        position: "top-end",
        icon: "success",
        title: "Eliminado",
        showConfirmButton: false,
        timer: 1500,
      });
    },
    error: function (error) {
      alert(
        "Hubo un error al eliminar el producto al carro." + error + productoId
      );
    },
  });
}
