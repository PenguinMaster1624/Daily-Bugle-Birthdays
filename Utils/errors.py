class OutdatedPackageError(Exception):
    '''
    Error raised when there is at least one outdated package found
    '''
    def __init__(self, packages: list[str]) -> None:
        self.packages = packages

    def __str__(self) -> str:
        return f'{len(self.packages)} Packages Require Attention: {self.packages}'
    
    def __repr__(self) -> str:
        return f'<OutdatedPackagesError({self.packages})>'
    
class UserNotFoundError(Exception):
    '''
    Error raised when a given user's birthday
    is not found in the database when updating/deleting
    '''
    def __init__(self, username: str) -> None:
        self.username = username

    def __str__(self):
        return f'{self.username}\'s birthday is not found in the database'
    
    def __repr__(self):
        return f'<UserNotFoundError({self.username})>'
    
class UserExistsError(Exception):
    '''
    Error raised when a given user's birthday
    is not found in the database when updating/deleting
    '''
    def __init__(self, username: str) -> None:
        self.username = username

    def __str__(self):
        return f'{self.username} exists within the database! Use my `/update`command to update your entry!'
    
    def __repr__(self):
        return f'<UserExistsError({self.username})>'