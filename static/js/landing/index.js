$(document).ready(function() {

	$('.book-cover').on('click', function() {
		$('#book-information-modal').modal('show');
	});

	$('#book-search').addClass('hidden');
})