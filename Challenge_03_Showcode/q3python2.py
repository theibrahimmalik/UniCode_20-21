class Solution:

    def get_recipient(self, message, position):
        import re
        reg = "(?<!\w)@[A-Za-z0-9-_]+"
        users = re.findall(reg, message)
        if position > len(users) or position == 0:
            return ""
        return users[position-1].replace("@", "")
