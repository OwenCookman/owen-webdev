$(document).ready(function () {

    $('#PrintPage').click(function(){
        window.print();
    });

    $('#TailoredWebsite').click(function() {
        $('#TailoredWebsiteModal').modal('show');
    });

    $('#TargetedDesign').click(function() {
        $('#TargetedDesignModal').modal('show');
    });

    $('#ModernLanguages').click(function() {
        $('#ModernLanguagesModal').modal('show');
    });

    $('#Responsive').click(function() {
        $('#ResponsiveModal').modal('show');
    });


});