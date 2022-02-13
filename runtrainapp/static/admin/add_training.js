//Alert should be able to reappear
$(function() {
   $(document).on('click', '.close', function() {
       $(this).parent().hide();
   })
});