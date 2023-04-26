$(document).load(function() {
    // Hide all desktops except the first one
    $('.desktop').not(':first').hide();

    // Handle desktop click event
    $('.desktop').on('click', function() {
        // Check if the clicked desktop is the last one
        if (!$(this).next().length) {
            $(this).slideUp('slow');
            $('.desktop').first().slideDown('slow');
        }
        else {
            // Slide down the current desktop
            $(this).slideUp('slow');
            // Slide up the next desktop
            $(this).next().slideDown('slow');
        }
    });
});