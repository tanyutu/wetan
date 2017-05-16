import ConfigParser,os

class TestConfig:
    """
    configuration
    """
    def __init__(self, env):
        self.env = env
        self.conf = ConfigParser.ConfigParser()
        self.conf.read(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)), 'conf.txt'))

    def get_portal(self):
        return self.conf.get(self.env, 'portal_url')


    def get_url(self):
        return self.conf.get(self.env, 'url')

    def get_rhcert_url(self):
        return self.conf.get(self.env, 'rhcert_url')

    def get_username(self):
        return self.conf.get(self.env, 'partner_sso_username')

    def get_passwd(self):
        return self.conf.get(self.env, 'partner_sso_password')

    def get_review_url(self):
        return self.conf.get(self.env, 'review_url')

    def get_review_user(self):
        return self.conf.get(self.env, 'reviewer_bz_username')

    def get_review_passw(self):
        return self.conf.get(self.env, 'reviewer_bz_password')



