// Hide Header on on scroll down
var didScroll;
var lastScrollTop = 0;
var delta = 5;
var navbarHeight = $('.fnb').outerHeight();

$(window).scroll(function(event){
	didScroll = true;
});

setInterval(function() {
	if (didScroll) {
		hasScrolled();
		didScroll = false;
	}
}, 250);

function hasScrolled() {
	var st = $(this).scrollTop();
	// Make sure they scroll more than delta
	if(Math.abs(lastScrollTop - st) <= delta)
		return;
	// If they scrolled down and are past the navbar, add class .nav-up.
	// This is necessary so you never see what is "behind" the navbar.
	if (st > lastScrollTop && st > navbarHeight){
		// Scroll Down
		$('.fnb').removeClass('fnb-down').addClass('fnb-up');
		$('.gnb').removeClass('gnb-up').addClass('gnb-down');
	} else {
		// Scroll Up
		if(st + $(window).height() < $(document).height()) {
			$('.fnb').removeClass('fnb-up').addClass('fnb-down');
			$('.gnb').removeClass('gnb-down').addClass('gnb-up');
		}
	}

	lastScrollTop = st;
}