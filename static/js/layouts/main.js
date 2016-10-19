$(document).ready(function() {
	$('#login-link').on('click', function() {
		console.log('Muestra el modal de iniciar sesión');
		$('#login-modal').modal('show');
	});
});