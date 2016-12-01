// Edit Profile User
$('#edit-profile-user-form').on('submit', function(event){
    event.preventDefault();
    console.log("User form submitted"); // sanity check
    ajax_edit_profile_user_form();
});

function ajax_edit_profile_user_form() {
    $('#edit-profile-user-success-alert').hide();
    $('.edit-profile-user-form-error').remove();
    var fields  = {
        username: $('input[name=username]'),
        first_name: $('input[name=first_name]'),
        last_name: $('input[name=last_name]')
    };
    for (var field in fields) {
        fields[field].parent().removeClass('has-error');
    }
    //noinspection JSUnresolvedVariable
    $.ajax({
        url : edit_profile_user_form_endpoint, // the endpoint
        type : "POST", // http method
        data : {
            username: fields.username.val(),
            first_name: fields.first_name.val(),
            last_name: fields.last_name.val(),
            csrfmiddlewaretoken: django_csrf
        }, // data sent with the post request

        // handle a successful response
        statusCode: {
            200: function(data, textStatus) {
                console.log(textStatus);
                $('#edit-profile-user-success-alert').show();
            },
            400: function(xhr) {
                console.log(xhr.statusText);
                var data = JSON.parse(xhr.responseText);
                $.each(data, function(name, value) {
                    $("input[name="+ name +"]").parent().addClass('has-error');
                    $.each(value, function(i, error_value) {
                        $("input[name="+ name +"]").after('<p class="text-danger edit-profile-user-form-error">' + error_value + '</p>');
                    });
                });
            }
        }
    });
}

// Edit Profile Password
$('#edit-profile-password-form').on('submit', function(event){
    event.preventDefault();
    console.log("Password form submitted"); // sanity check
    ajax_edit_profile_password_form();
});

function ajax_edit_profile_password_form() {
    $('#edit-profile-password-success-alert').hide();
    $('.edit-profile-password-form-error').remove();
    var fields  = {
        old_password: $('input[name=old_password]'),
        new_password1: $('input[name=new_password1]'),
        new_password2: $('input[name=new_password2]')
    };
    for (var field in fields) {
        fields[field].parent().removeClass('has-error');
    }
    //noinspection JSUnresolvedVariable
    $.ajax({
        url : edit_profile_password_form_endpoint, // the endpoint
        type : "POST", // http method
        data : {
            old_password: fields.old_password.val(),
            new_password1: fields.new_password1.val(),
            new_password2: fields.new_password2.val(),
            csrfmiddlewaretoken: django_csrf
        }, // data sent with the post request

        // handle a successful response
        statusCode: {
            200: function(data, textStatus) {
                console.log(textStatus);
                $('#edit-profile-password-success-alert').show();
                for (var field in fields) {
                    fields[field].val("");
                }
            },
            400: function(xhr) {
                console.log(xhr.statusText);
                var data = JSON.parse(xhr.responseText);
                $.each(data, function(name, value) {
                    $("input[name="+ name +"]").parent().addClass('has-error');
                    $.each(value, function(i, error_value) {
                        $("input[name="+ name +"]").after('<p class="text-danger edit-profile-password-form-error" >' + error_value + '</p>');
                    });
                });
                for (var field in fields) {
                    fields[field].val("");
                }
            }
        }
    });
}

// Edit Profile e-mail
$('#edit-profile-email-form').on('submit', function(event){
    event.preventDefault();
    console.log("E-mail form submitted"); // sanity check
    ajax_edit_profile_email_form();
});

function ajax_edit_profile_email_form() {
    $('#edit-profile-email-success-alert').hide();
    $('.edit-profile-email-form-error').remove();
    var fields  = {
        new_email1: $('input[name=new_email1]'),
        new_email2: $('input[name=new_email2]')
    };
    for (var field in fields) {
        fields[field].parent().removeClass('has-error');
    }
    //noinspection JSUnresolvedVariable
    $.ajax({
        url : edit_profile_email_form_endpoint, // the endpoint
        type : "POST", // http method
        data : {
            new_email1: fields.new_email1.val(),
            new_email2: fields.new_email2.val(),
            csrfmiddlewaretoken: django_csrf
        }, // data sent with the post request

        // handle a successful response
        statusCode: {
            200: function(data, textStatus) {
                console.log(textStatus);
                $('#edit-profile-email-success-alert').show();
                for (var field in fields) {
                    fields[field].val("");
                }
            },
            400: function(xhr) {
                console.log(xhr.statusText);
                var data = JSON.parse(xhr.responseText);
                $.each(data, function(name, value) {
                    $("input[name="+ name +"]").parent().addClass('has-error');
                    $.each(value, function(i, error_value) {
                        $("input[name="+ name +"]").after('<p class="text-danger edit-profile-email-form-error" >' + error_value + '</p>');
                    });
                });
            }
        }
    });
}

// Edit Profile Extended
$('#edit-profile-extended-form').on('submit', function(event){
    event.preventDefault();
    console.log("Extended form submitted"); // sanity check
    ajax_edit_profile_extended_form();
});

function ajax_edit_profile_extended_form() {
    $('#edit-profile-extended-success-alert').hide();
    $('.edit-profile-extended-form-error').remove();
    var fields  = {
        date_of_birth: $('input[name=date_of_birth]'),
        mobile_phone: $('input[name=mobile_phone]'),
        address: $('input[name=address]'),
        academic_qualifications: $('input[name=academic_qualifications]'),
        profession: $('input[name=profession]'),
        volunteer_experience: $('textarea[name=volunteer_experience]'),
        observations: $('textarea[name=observations]')
    };
    for (var field in fields) {
        fields[field].parent().removeClass('has-error');
    }

    //noinspection JSUnresolvedVariable
    $.ajax({
        url : edit_profile_extended_form_endpoint, // the endpoint
        type : "POST", // http method
        data : {
            date_of_birth: fields.date_of_birth.val(),
            mobile_phone: fields.mobile_phone.val(),
            address: fields.address.val(),
            academic_qualifications: fields.academic_qualifications.val(),
            profession: fields.profession.val(),
            volunteer_experience: fields.volunteer_experience.val(),
            observations: fields.observations.val(),
            csrfmiddlewaretoken: django_csrf
        }, // data sent with the post request

        // handle a successful response
        statusCode: {
            200: function(data, textStatus) {
                console.log(textStatus);
                $('#edit-profile-extended-success-alert').show();
            },
            400: function(xhr) {
                console.log(xhr.statusText);
                var data = JSON.parse(xhr.responseText);
                $.each(data, function(name, value) {
                    $("input[name="+ name +"]").parent().addClass('has-error');
                    $.each(value, function(i, error_value) {
                        $("input[name="+ name +"]").after('<p  class="text-danger edit-profile-extended-form-error">' + error_value + '</p>');
                    });
                });
            }
        }
    });
}
