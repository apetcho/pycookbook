#!/usr/bin/env python3
from operator import attrgetter


class User:
    def __init__(self, uid):
        self.uid = uid
    
    def __repr__(self) -> str:
        return f"User({self.uid})"
    

def main():
    """Main entry."""
    users = [User(23), User(3), User(99)]
    print(users)
    # -*- Sort users by uid
    print(sorted(users, key=attrgetter("uid")))


if __name__ == "__main__":
    main()
