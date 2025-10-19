def demonstrate_mutability():
    userA = {
        "alias": "IronMan"
    }
    userB = {
        "alias": "Captain"
    }

    userA["alias"] = "Vision"
    userB["alias"] = "Falcon"
    
    userB = {
        "realName": "Sam Wilson"
    }
