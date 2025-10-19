contact_list = [
    {"firstName": "Vanya", "phone": "+380971234567"},
    {"firstName": "Sasha", "phone": "+380669876543"},
    {"firstName": "Dima", "phone": "+380501112233"},
]

def find_contact_in_list(name):
    for contact in contact_list:
        if contact["firstName"] == name:
            return contact["phone"]
    return None
