//Humburger menu
function db() {
	if($('#menubar_hdr').hasClass('ham')) {
		$('#menubar').addClass('db');
	} else {
		$('#menubar').removeClass('db');
	}
}


//Humburger menu
$(function() {
	$('#menubar_hdr').click(function() {
		$(this).toggleClass('ham');
		db();
	});
});


//remove Humburger menu
$(function() {
	$('#menubar a[href^="#"]').click(function() {
		$('#menubar').removeClass('db');
		$('#menubar_hdr').removeClass('ham');
	});
});


//line Under h2
$(function() {
	$('main h2').wrapInner('<span class="uline">');
});