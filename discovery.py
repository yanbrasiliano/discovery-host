
"""

Created by: Yan Brasiliano Silva Penalva
Objective: discover hosts - addres ip of the websites.

"""

print()
print('Author: Yan Brasiliano Silva Penalva - hiyan')
print()



import socket as s
from time import sleep
while True: 
	# host #
	host = str(input('Enter a valid host: '))

	# ping #
	ip = s.gethostbyname(host)

	print('Searching...')	
	sleep(1)
	print()
	# result #
	print(f'The host IP {host} is {ip}')

	while True:
			print()
			resp = str(input('New discovery?[Y/N]: ')).upper().split()[0]
			if resp in 'YN':
					break
			print('ERROR! ANSWER ONLY Y or N!')
	if resp == 'N':
				break
