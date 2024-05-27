# TODO: do we need this?
class URL:
    def __init__(self, url: str, profile_id: int):
        self.profile_id = profile_id
        self.url = url

    def __dict__(self) -> dict:
        return {
            'profile_id': self.profile_id,
            'url': self.url
        }
