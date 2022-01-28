document.addEventListener("DOMContentLoaded", function () {
	var errorClass = 'invalid';
	var validClass = 'success';

	var highlightRules = function (element, errorClass, validClass) {
		$(element).addClass(errorClass).removeClass(validClass);
		$(element).closest(".input-wrap").addClass(errorClass).removeClass(validClass);
	}

	var unhighlightRules = function (element, errorClass, validClass) {
		$(element).removeClass(errorClass).addClass(validClass);
		$(element).closest(".input-wrap").removeClass(errorClass).addClass(validClass);
	}

	var errorTarget = function (error, element) {
		error.appendTo(element.closest('.input-wrap').find('.input-error'));
	}

	$.validator.addMethod("email", function (value, element) {
		return this.optional(element) || /^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,5}$/i.test(value);
	});

	$(".js-form").each(function () {
		var $this = $(this);

		$this.validate({
			errorClass: errorClass,
			validClass: validClass,
			errorElement: 'span',
			ignore: ':hidden:not(:checkbox)',
			errorPlacement: errorTarget,
			highlight: highlightRules,
			unhighlight: unhighlightRules,

			rules: {

				email: {
					required: true,
					email: true
				},
			},

			submitHandler: function (form) {
				var submitButton = $this.find('button[type=submit]');
				submitButton.prop('disabled', true);

				$.ajax({
					url: form.action,
					type: form.method,
					data: $(form).serializeArray(),
					success: function() {
						showFormSuccess($this);
						setTimeout(function () {
							resetForm($(form));
							submitButton.prop('disabled', false);
						}, 10000);
					},
					error: function () {
						showFormError($this);
						setTimeout(function () {
							resetForm($(form));
							submitButton.prop('disabled', false);
						}, 7000);
					}
				});
			}
		});
	});
});


function showFormSuccess(form) {
	form.hide(0, function () {
		form.closest('.form-wrap').find('.form-success').fadeIn(600);
	});
}

function showFormError(form) {
	form.closest('.form-wrap').find('.form-error').fadeIn(600);
}

function resetForm(form) {
	form.removeAttr('style');
	form.parent().find('.form-success').removeAttr('style');
	form.parent().find('.form-error').removeAttr('style');
	form[0].reset();
}