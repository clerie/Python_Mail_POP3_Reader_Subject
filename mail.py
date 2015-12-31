import poplib
import string

mailServer = 'pop.gmail.com'
emailID    = 'info@gamil.com'
emailPass  = 'xxxx'


## open connection to mail server (Secured using SSL)
POP = poplib.POP3_SSL(mailServer)

## print the response message from server
print POP.getwelcome()

## set email address
POP.user(emailID)

## set password 
POP.pass_(emailPass)

## get information about the email address
EmailInformation = POP.stat()
print EmailInformation

## Reading an email
print "\n\n===\nRead messages\n===\n\n"
 
## Read all emails
numberOfMails = EmailInformation[0]
for mailNumber in range(numberOfMails):
    for email in POP.top(mailNumber+1, 0)[1]:
        emailSplit = string.split(email, '\n')
	for line in emailSplit:
		find = string.find(line, 'Subject: ')
		if find != -1:
			lineShow = string.replace(line, 'Subject: ', '')
			print lineShow

print ''

## Close Connection
POP.quit()
quit()
