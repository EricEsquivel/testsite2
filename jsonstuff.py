import json

######### This variable is what is temporarily used by registercheck to store all usernames after they were parsed so that they can be checked #########
usernames = []

######### Checking for already existing usernames before registering for main.py #########
def registercheck(newaccount):
    with open("accounts.json") as json_file:
        json_file = json.load(json_file)
        temp = json_file["accounts"]
        for i in json_file["accounts"]:
            usernames.append(i["username"])
        if newaccount["username"] in usernames:
            return False
        else:
            temp.append(newaccount)
            write_json(json_file)
            return "success"

######### After registercheck, this is run to write to "database" which is accounts.json #########
def write_json(data, filename="accounts.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


######### Check for login in main.py #########
def logincheck(loginaccount):
    with open("accounts.json") as json_file_login:
        json_file_login = json.load(json_file_login)
        accounts = json_file_login["accounts"]
        for account in accounts:
            if loginaccount["username"] == account["username"] and loginaccount["password"] == account["password"]:
                print("Signed in with " + loginaccount["username"],loginaccount["password"]) ######### Check to see who you sign in as! #########
                return "logged in"
            else:
                pass
        print("Attempted login as:",loginaccount["username"],loginaccount["password"]) ######### Attempted log in as... ###########
        print("No results match those credentials")


######### Run this app directly to test accounts.json for yourself. Manually input some credentials and test it out. #########
if __name__ == "__main__":
    test = {"username": "testusername", "password": "password"}
    registercheck(test)