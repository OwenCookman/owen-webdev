$(document).ready(function () {

    $('#PrintPage').click(function(){
        window.print();
    });
    

    $('#DeleteBtn').click(function(){
         $("#delete").modal("show");
    });

});