## Installing:
1. Include this folder (with these executables) in your path.

2. Run in terminal: `pip install requests` (needed for git b-fetch python script)

3. Create `.fetch-auth` file with your JIRA credentials

## Running:

**-create branch:**

`git cb BL-12345 "this is the description"`

Or, if you omit the description it will be fetched from JIRA if there is an existing ticket

**-edit branch description:**

`git eb BL-12345 "new description"`

**-list branches**

`git b`

**-fetch ticket description from JIRA**

`git b-fetch BL-12345`

*NOTE:* This will not overwrite an existing label, so if you have an existing label and you want to replace it with the JIRA ticket title, then you must `git eb BL-12345 ''`

### Other Notes:

 - You can use the git branch printing with labels for any branch listing:

  **example:** print all branches not merged into master

  `git branch --no-merged master | git b-parse-and-print`


 - The branch descriptions are located in &lt;project folder&gt;/.git/branch_names

 - You can do bulk labelling from JIRA tickets by running 
 
 	`git branch | git-b-parse-and-fetch`
 	
 	or, something like 
 	
 	`git branch --no-merged master | git b-parse-and-fetch`
