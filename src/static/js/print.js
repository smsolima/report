$(document).ready(function(){
    $('#data').DataTable({
        dom:'Bfrtip' , 
        buttons: [
            'copy', 'excel', 'pdf'
        ]
    });
});