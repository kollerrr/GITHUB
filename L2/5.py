
def login_extraction(login_w_at):
    login = login_w_at.split('@')
    return login[0]

login_w_at = str(input())
print(login_extraction(login_w_at))