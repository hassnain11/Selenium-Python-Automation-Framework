VALID_LOGIN = [
    (
        "standard_user",
        "secret_sauce"
    )
]


INVALID_LOGIN = [

    (
        "standard_user",
        "wrong_password",
        "Epic sadface: Username and password do not match any user in this service"
    ),

    (
        "wrong_user",
        "secret_sauce",
        "Epic sadface: Username and password do not match any user in this service"
    ),

    (
        "",
        "",
        "Epic sadface: Username is required"
    ),

]