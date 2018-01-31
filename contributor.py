
class Contributor:
    personal_field = "author"


    def __init__(self, data):
        self.login = data[self.personal_field]["login"]


        self.id = data[self.personal_field]["id"]
        self.avatar_url = data[self.personal_field]["avatar_url"]
        self.gravatar_id = data[self.personal_field]["gravatar_id"]
        self.url = data[self.personal_field]["url"]
        self.html_url = data[self.personal_field]["html_url"]
        self.followers_url = data[self.personal_field]["followers_url"]
        self.following_url = data[self.personal_field]["following_url"]
        self.gists_url = data[self.personal_field]["gists_url"]
        self.starred_url = data[self.personal_field]["starred_url"]
        self.subscriptions_url = data[self.personal_field]["subscriptions_url"]
        self.organizations_url = data[self.personal_field]["organizations_url"]
        self.repos_url = data[self.personal_field]["repos_url"]
        self.events_url = data[self.personal_field]["events_url"]
        self.received_events_url = data[self.personal_field]["received_events_url"]
        self.type = data[self.personal_field]["type"]
        self.site_admin = data[self.personal_field]["site_admin"]
        
        self.commit_list = [commit for commit in data['weeks'] if commit['c'] != 0]

        self.total = data['total']


