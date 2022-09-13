import os
import requests==2.19.0

file_location = input('\n/Users/christophervandermade/area51.txt ') # 

# open and read file
file = open(file_location, "r")
print(file.read())


# -*- coding: utf-8 -*-
# set variable to assert:
var_to_assert = "hello"

# if condition returns True, then nothing happens:
assert var_to_assert == "hello"

# if condition returns False, AssertionError is raised (comment out to test the next one):
#assert var_to_assert == "goodbye"

# if condition returns False, custom AssertionError is raised: 
assert var_to_assert == "goodbye", f"var_to_assert should be '{var_to_assert}'"

# run like this to disable assert statements: python3 -O py_vuln03.py
print("When you run code with -O, assert statements are skipped...")


def update_details(request, acc_id): 
  user = Account.objects.get(acc=acc_id) 
  if request.user.id == user.id: 
    # ALLOW ACTION 
    # VALIDATE REQUEST DATA 
    form = AccountForm(instance=user,request=request) 
    ... 
  else: 
    # DENY ACTION
