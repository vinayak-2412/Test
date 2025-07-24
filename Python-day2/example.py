# # def valid_email(email_list):
# #     valid_emails = []
# #     for email in email_list:
# #         if email.count('@') != 1:
# #             continue
# #         username, domain = email.split('@')
# #         if not username.isalnum():
# #             continue
# #         if not (domain.endswith('.com') or domain.endswith('.in')):
# #             continue
# #         valid_emails.append(email)
# #     return valid_emails
# #
# #
# # emails = [
# #     "user123@gmail.com",
# #     "user.name@yahoo.in",
# #     "user@site.org",
# #     "invalid@domain",
# #     "gooduser@domain.com",
# #     "user name@domain.com"
# # ]
# #
# # print(valid_email(emails))
# def top3words(para):
#      para=para.lower()
#      for p in ",.!?:'\"()-":
#          para=para.replace(p,"")
#
#      words = para.split()
#      freq={}
#      for word in words:
#          if word in freq:
#              freq[word]+=1
#          else:
#              freq[word]=1
#      sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
#
#
#      top_words = []
#      for i in range(min(3, len(sorted_words))):
#          top_words.append(sorted_words[i][0])
#
#      return top_words
#
#
#
#  text= "The cat and the dog played. The dog barked!"
#  print(top3words(text))
#
#
# def strip(name):
#      names=name.split(",")
#      new_names=[]
#      for name in names:
#          name = name.strip()
#          name= name.title()
#          new_names.append(name)
#
#      new_names.sort()
#      return new_names
#
#
# namess=" fohn,DOE, alice ,BOB,canny,elf "
# print(strip(namess))

# username=input('Enter your username')
# a=False
# b=False
# c=False
# d=False
# spcl='_.'
# for i in username:
#     if i.islower():
#         a=True
#     if
# import re
#
# def is_valid_username(username):
#     # Rule 3: Length check
#     if not (6 <= len(username) <= 20):
#         return False
#
#     # Rule 1 & 2: Valid characters and must start with a lowercase letter
#     if not re.match(r'^[a-z][a-z0-9._]*$', username):
#         return False
#
#     # Rule 4: No consecutive special characters
#     if '__' in username or '..' in username or '._' in username or '_.' in username:
#         return False
#
#     # Rule 5: Cannot start or end with special characters
#     if username[0] in '._' or username[-1] in '._':
#         return False
#
#     return True
#
# # Valid usernames
# print(is_valid_username("john_doe1"))      # True
# print(is_valid_username("a.b_c9"))         # True
#
# # Invalid usernames
# print(is_valid_username("JohnDoe"))        # False (starts with uppercase)
# print(is_valid_username("john..doe"))      # False (double dot)
# print(is_valid_username("john_doe_"))      # False (ends with _)
# print(is_valid_username("_johndoe"))       # False (starts with _)
# print(is_valid_username("jo"))             # False (too short)
# s='abcabcbb'
# res=''
#
# for i in range(0,len(s),max):
#     res=s[i:i+max]
#     print(res)
def length_of_longest_substring(s):
    start = 0
    max_len = 0
    seen = {}

    for end in range(len(s)):
        if s[end] in seen and seen[s[end]] >= start:
            start = seen[s[end]] + 1
        seen[s[end]] = end
        max_len = max(max_len, end - start + 1)

    return max_len
s='abcabcbb'
a=length_of_longest_substring(s)
print(a)