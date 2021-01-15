from .bank_account import start_bank_account_service
from .favorite import start_favorite_service
from .whitelist import start_whitelist_service
from .profile import start_profile_emit

def start_all_servicers():
    start_bank_account_service()
    start_favorite_service()
    start_whitelist_service()

def start_all_emiters():
    start_profile_emit()
