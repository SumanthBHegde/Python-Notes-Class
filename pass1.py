import re
def check_password_strength(password):
    score = 0
    suggestions = []
    if len(password) >= 8:
        score +=1
    else:
        suggestions.append("should be 8 char")
    if re.search(r"[A-Z]",password):
        score += 1
    else:
        suggestions.append("at least one upper case")
    if re.search(r"[a-z]",password):
        score +=1
    else:
        suggestions.append("at least one lower case")
    if re.search(r"\d",password):
        score +=1
    else:
        suggestions.append("at least one digit")
    if re.search(r"[!@#$%^&*(),.?\":{{}|<>]",password):
        score +=1
    else:
        suggestions.append("one special char")
    return score,suggestions
password = input("input password:")
print(check_password_strength(password))
