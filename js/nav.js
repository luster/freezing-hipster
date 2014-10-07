// enable mobile nav
$(function(){
    $('#menu').slicknav({
        label: '',
        prependTo: 'body',
        closeOnClick: true,
        init: function(){
            $('.slicknav_menu').prepend('<div id="mobile-logo" class="logodiv"></div>');
        }
    });
});

// navigation links are anchor links, smooth scroll accordingly
function scroll_if_anchor(href) {
    href = typeof(href) == "string" ? href : $(this).attr("href");

    // If href missing, ignore
    if(!href) return;

    // You could easily calculate this dynamically if you prefer
    var fromTop = $(window).width() >= 1024 ? 79 : 46;
    // If our Href points to a valid, non-empty anchor, and is on the same page (e.g. #foo)
    // Legacy jQuery and IE7 may have issues: http://stackoverflow.com/q/1593174
    if(href.charAt(0) == "#") {
        var $target = $(href);

        // Older browsers without pushState might flicker here, as they momentarily
        // jump to the wrong position (IE < 10)
        if($target.length) {
            $('html, body').animate({ scrollTop: $target.offset().top - fromTop });
            if(history && "pushState" in history) {
                //history.pushState({}, document.title, window.location.pathname + href);
                return false;
            }
        }
    }
}

// When our page loads, check to see if it contains and anchor
scroll_if_anchor(window.location.hash);

// Intercept all anchor clicks
$("body").on("click", "a", scroll_if_anchor);