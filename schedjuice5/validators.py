from django.core.validators import RegexValidator

nameValidation = RegexValidator(
    regex=r"[a-zA-Z ]",
    message="Field must only contain basic Latin characters and spaces.",
)
nameWithNumberValidation = RegexValidator(
    regex=r"[a-zA-Z0-9 ]",
    message="Field must only contain basic Latin characters, numbers and spaces.",
)
usernameValidation = RegexValidator(
    regex=r"[a-zA-Z0-9_]{8,32}",
    message="Username must match this: '[a-zA-Z0-9_]{8,32}'",
)
phoneNumberValidation = RegexValidator(
    regex=r"(\+)?[0-9 ]{8,20}",
    message="Phone number must match this: '(\\+)?[0-9 ]{8,20}'",
)
strictNumberValidation = RegexValidator(
    regex=r"[0-9]", message="Field must contain only number and no white spaces."
)
bankAccountNumberValidation = RegexValidator(
    regex=r"[\d ]{6,20}", message="Bank account number must match this: '[\\d ]{6,20}'"
)
nameWithUnderscoreValidation = RegexValidator(
    regex=r"[a-zA-Z _]", message="Field must match this: '[a-zA-Z _]'"
)
englishAndSomeSpecialValidation = RegexValidator(
    regex=r"[a-zA-Z0-9_\-\(\) ]",
    message="Field must match this: '[a-zA-Z0-9_\\-\\(\\) ]'",
)
colorCodeValidation = RegexValidator(
    regex=r"^#[a-zA-Z0-9]{6}$",
    message="Color code must match this: '#[a-zA-Z0-9]{6}'"
)