$(document).ready(function ($) {
    $('form').submit(function () {
        if ($('input').val() !== '') { // don't add empty tasks
            var userInput = $('input').val(); // get what user entered
            $('ol').prepend('<li>' + userInput + '</li>'); // put new item at the top of list

            $('ol').click(function (e) { // thank you S.O.
                $(e.target).remove();
            });

            // reset form field
            $('form')[0].reset();
        }
        return false; // outside "if" bc will fail if input is empty       
    });
});
