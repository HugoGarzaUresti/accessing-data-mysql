from app import setup_database, add_user, get_users

def main():
    engine = setup_database()
    add_user(engine, 'John Doe', 'john.doe@example.com')
    users = get_users(engine)
    for user in users:
        print(user)

if __name__ == "__main__":
    main()
