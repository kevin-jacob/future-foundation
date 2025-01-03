import instaloader

# Function to check who is not following back for a specific friend
def get_non_follow_back(friend_username):
    print(f"Checking {friend_username}...")
    
    # Load the friend's profile
    friend_profile = instaloader.Profile.from_username(L.context, friend_username)
    
    # Create lists for followees and followers
    followees = [user.username for user in friend_profile.get_followees()]  # Who your friend follows
    followers = [user.username for user in friend_profile.get_followers()]  # Who follows your friend
    
    # Create a set of followers for fast lookup
    followers_set = set(followers)
    
    # List to store users who are following your friend but aren't following them back
    non_follow_back = []
    
    # Iterate through followees and check if they are in the followers list
    for followee in followees:
        if followee not in followers_set:
            non_follow_back.append(followee)
    
    return non_follow_back


# Instantiate the instaloader object
L = instaloader.Instaloader()

# Log into Instagram (Replace with your credentials or use session file)
username = ''
password = ''
L.login(username, password)

# Specify the friend's username to check
friend_username = input()

# Get the non-follow backs for the specified friend
non_follow_back = get_non_follow_back(friend_username)

# Print the results
if non_follow_back:
    print(f"\n{friend_username} has the following users not following them back:")
    for user in non_follow_back:
        print(user)
else:
    print(f"\n{friend_username} has no users not following them back.")
