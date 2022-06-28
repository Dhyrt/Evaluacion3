function confirmDelete(codigo) {
  Swal.fire({
    icon: 'warning',
    title: '¿Estas seguro?',
    text: 'No podras deshacer esta accion',
    showCancelButton: true,
    confirmButtonText: 'Confirmar',
    cancelButtonText: 'Cancelar',
  }).then((result) => {
    if (result.value) {
      Swal.fire(
        'Producto eliminado',
        '', 'success'
        ).then(function() {
            window.location.href = "/eliminarProducto/" + codigo + "/";
        })
    }
  })
}

function fallo(){
  Swal.fire({
    title: '<strong>NO PUEDES USAR ESTA OPCION</u></strong>',
    icon: 'info',
    html:
      'Primero debes</b> ' +
      '<a href="/accounts/login/">iniciar sesión</a> o',
    showCloseButton: true,
    showCancelButton: true,
    focusConfirm: true,
    confirmButtonColor:'#d33',
    confirmButtonText:
      '<a href="/registro/" style="color:white" "background-color:red"> Registrate </a>',
    confirmButtonAriaLabel: '',
    cancelButtonText:
      'Cancelar',
    cancelButtonAriaLabel: ''
  })
}

function agregado(){
  Swal.fire({
    position: 'top-end',
    icon: 'success',
    title: 'Guardado correctamente',
    showConfirmButton: false,
    timer: 50000,
  })
}