# Python 3
# Password Manager

import sys, pyperclip

PASSWORDS = {'gmail': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'netid': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'rutgers_email': 'SADFASDFSDFSFSsdfdsfsd',
             'hotmail': 'asdfasdfsadfasdfasdfasdfasdf',
             'facebook': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt'}

if len(sys.argv) != 2:
	print("Usage: python pw.py [account name] - copy account password to clipboard")
	sys.exit()

input = sys.argv[1]


# Print all name of accounts
if input == "all_account":
	for i in PASSWORDS:
		print(i)
	sys.exit()	

if input in PASSWORDS:
	pyperclip.copy(PASSWORDS[input])
	print("Successfully copied password for "+input)
else:
	print("FAILED: There is no account named "+ input)










