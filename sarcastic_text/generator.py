import pyperclip
import os
import platform
plat=platform.platform()
if(plat=='Windows'):
    clear_command='cls'
else:
    clear_command='clear'
def main():
	list2=[]
	sentence= input('Enter the sentence: ')
	l=len(sentence)
	list1= list(sentence)
	for i in range(l):
		if(i==0):
			list1[i]=list1[i].lower()
			list2.append(list1[i])
		elif(i%2==0 and i!=0):
			list1[i]=list1[i].lower()
			list2.append(list1[i])
		elif(i%2!=0):
			list1[i]=list1[i].upper()
			list2.append(list1[i])
	new= ''
	for i in range(l):
		new+=list2[i]
	print()
	pyperclip.copy(new)
	print('This sentence has been copied to your clipboard!: ', new)
while 1==1:
	os.system(clear_command)
	main()
	input()
