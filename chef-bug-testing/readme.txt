This section covers the bug testing of chef. Rubocop was used as a primary bug-finding and code-smell detection tool.
Tested on:
	Ruby: 2.4.4
	OS: Windows 7

Dependencies and Procedure:
Clone the chef code on your local machine.
We first need to download and install the gem for rubocop. For this we run the command 'gem install rubocop'.
This will install rubocop onto your system.

Then we run the following commands to get a report of the code offences and the types of errors:
1) rubocop --only Syntax : This command will list out the E,W offences.
2) rubocop : This command will list out the E,W,C offences.
The results and information regarding the offences can be found int the result folder.