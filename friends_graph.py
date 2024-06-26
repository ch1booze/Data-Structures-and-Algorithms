from collections import deque


class FriendsGraph:
    def __init__(self) -> None:
        self.users = dict()

    def does_user_exist(self, user: str):
        return user in self.users.keys()

    def do_users_exist(self, user, friend):
        is_user = self.does_user_exist(user)
        is_friend = self.does_user_exist(friend)

        if is_user and is_friend:
            return True
        else:
            print(f"User `{user}` and/or User `{friend}` not registered.")
            return False

    def register_user(self, user: str):
        if not self.does_user_exist(user):
            self.users[user] = set()
            print(f"Created `{user}` profile.")
        else:
            print(f"User `{user}` already exists.")

    def add_friend(self, user: str, friend: str):
        if self.do_users_exist(user, friend):
            if friend in self.users[user]:
                print(f"User `{user}` and User `{friend}` are already friends.")
            else:
                self.users[user].add(friend)
                print(f"User `{user}` and User `{friend}` are now friends.")

    def remove_friend(self, user: str, friend: str):
        if self.do_users_exist(user, friend):
            if friend in self.users[user]:
                self.users[user].remove(friend)
                print(f"User `{user}` and User `{friend}` are no longer friends.")

    def are_friends(self, user, friend):
        if not self.do_users_exist(user, friend):
            print(f"User `{user}` and/or User `{friend}` not registered.")
            return

        to_search = deque()
        to_search += self.users[user]
        already_searched = list()
        while to_search:
            person = to_search.popleft()
            already_searched.append(person)
            if person == friend:
                message = f"{user} "
                for p in already_searched:
                    message += f"-> {p} "
                print(message)
                return
            else:
                neighbors = self.users[person]
                for n in neighbors:
                    if n not in already_searched:
                        to_search.append(n)

        print(f"User `{user}` and User `{friend}` are not friends.")


if __name__ == "__main__":
    social_network = FriendsGraph()
    social_network.register_user("John")
    social_network.register_user("Khalid")
    social_network.register_user("Catherine")
    social_network.register_user("Caleb")
    social_network.register_user("Nikita")
    social_network.register_user("Boris")
    social_network.register_user("Billy")
    social_network.register_user("Eugene")
    social_network.register_user("Peter")
    social_network.register_user("Gina")
    social_network.register_user("Bernstein")
    social_network.register_user("Jonah")
    social_network.register_user("Beatrice")
    social_network.register_user("Dan")
    social_network.register_user("Hank")
    social_network.register_user("Clara")

    print()

    social_network.add_friend("John", "Khalid")
    social_network.add_friend("Khalid", "Catherine")
    social_network.add_friend("Catherine", "Caleb")
    social_network.add_friend("Beatrice", "Nikita")
    social_network.add_friend("Gina", "Khalid")
    social_network.add_friend("Khalid", "Jonah")
    social_network.add_friend("Jonah", "Beatrice")
    social_network.add_friend("Jonah", "John")
    social_network.add_friend("Jonah", "Clara")
    social_network.add_friend("Billy", "Clara")
    social_network.add_friend("Billy", "Peter")

    print()

    social_network.are_friends("John", "Khalid")
    social_network.are_friends("John", "Clara")
