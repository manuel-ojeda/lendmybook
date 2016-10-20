$(document).ready(function() {
	console.log('whats up');
	$('#add-book-button').on('click', function() {
		$('#add-book-modal').modal('show');
	});
})