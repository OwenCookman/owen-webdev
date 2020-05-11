$(document).ready(function () {

    // Print page function
    $('#PrintPage').click(function () {
        window.print();
    });

    // Click function for Tailored Website modal
    $('#TailoredWebsite').click(function () {
        $('#TailoredWebsiteModal').modal('show');
    });

    // Click function for Targeted design modal
    $('#TargetedDesign').click(function () {
        $('#TargetedDesignModal').modal('show');
    });

    // Click function for Modern languages modal
    $('#ModernLanguages').click(function () {
        $('#ModernLanguagesModal').modal('show');
    });

    // Click function for Responsive modal
    $('#Responsive').click(function () {
        $('#ResponsiveModal').modal('show');
    });

    // Click functions to toggle animation classes
    $('.rotateClick1').click(function () {
        $('.rotate1').toggleClass('down');
    });

    $('.rotateClick2').click(function () {
        $('.rotate2').toggleClass('down');
    });


});