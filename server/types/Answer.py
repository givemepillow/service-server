class Answer:
    UNDEFINED_REQUEST = {
        'type': 1,
        'message': 'Undefined request.'
    }

    UNEXPECTED_ERROR = {
        'type': 1,
        'message': 'Unexpected error.'
    }

    REGISTRATION_ACCEPTED = {
        'type': 2,
        'message': ''
    }

    REGISTRATION_VERIFICATION = {
        'type': 4,
        'message': ''
    }

    AUTHENTICATION_ACCEPTED = {
        'answer_type': 3,
        'message': ''
    }
