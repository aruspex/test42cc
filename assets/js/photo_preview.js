function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('#imgprv').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}

$('#id_photo').on('change', function() {
    readURL(this);
});