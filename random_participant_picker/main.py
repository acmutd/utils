import firebase_admin
from firebase_admin import credentials, firestore
from random import randint

# Enter id of event here
EVENT_ID = u'f21kickoff'

EVENT_COLLECTION = u'event_data'
PROFILE_COLLECTION = u'profile_data'

# Enter filename of private key JSON file here
CERTIFICATE_FILENAME = 'serviceKey.json'


def fetch_user_data(db, user):
    users = db.collection(PROFILE_COLLECTION).where(
        u'sub', '==', user['sub']).where(u'email', '==', user['email']).stream()

    for fetched_user in users:
        curr_user = fetched_user.to_dict()
        ret = {
            'email': user['email'],
            'first_name': "",
            'last_name': ''
        }
        if 'first_name' in curr_user:
            ret['first_name'] = curr_user['first_name']
        if 'last_name' in curr_user:
            ret['last_name'] = curr_user['last_name']

        return ret


def initialize_db():
    crd = credentials.Certificate(CERTIFICATE_FILENAME)
    firebase_admin.initialize_app(crd)
    db = firestore.client()

    return db


def fetch_participants_emails(db):
    event = db.collection(EVENT_COLLECTION).document(EVENT_ID).get()
    if not event.exists:
        print("Event does not exist")
        exit(0)

    participants_list = event.to_dict()['attendance']
    return participants_list


def print_user_info(lucky_user):
    print(f"Name: {lucky_user['first_name']} {lucky_user['last_name']}")
    print(f"Email: {lucky_user['email']}")


def main():
    db = initialize_db()
    participants_list = fetch_participants_emails(db)

    lucky_index = randint(0, len(participants_list) - 1)
    lucky_user = fetch_user_data(db, participants_list[lucky_index])

    print_user_info(lucky_user)


if __name__ == '__main__':
    main()
