class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        mails = set()
        i = 0
        for mail in emails:
            temp, domain, add = "", False, True
            for i, char in enumerate(mail):
                if char == '@':
                    domain = True
                    temp += char
                else:
                    if domain: temp += char
                    else:
                        if char == '+': add = False
                        if char not in ['.', '+'] and add: temp += char
            mails.add(temp)
        return len(mails)