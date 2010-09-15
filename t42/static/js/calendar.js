/* Show datepicker for 'id_birth' field
*/

$(document).ready(function(){
    $("#id_birth").datepicker({minDate: '-70y', maxDate: '-10y'});
});

