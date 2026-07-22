Parking Lot

- Strategy selection
- Batch execution
- Operation optimizer
- Parallel planners
- Diff engine
- Resource dependency graph

1. Strategy selection. The initial slice of functionality always generates RACF commands in the same way. For the user object, it creates an ADDUSER command fllowed by one ALTUSER command for each additional user segment and one to define the DFLTGRP, as well as a CONNECT. That approach offers fine-grained visibility into every action on the z/OS managed node, but at the cost of execution time. Each command transmitted to z/OS via ibm.ibm\_zos\_core takes significant time. 

It would be useful to adjust the "strategy" for issuing RACF commands based on some simple criteria, such as "minimize network traffic," "batch related groups of commands," or whatever. We could have the tool generate a single ADDUSER command that includes all segments and the default group value. We could have it generate a list of commands that the Ansible playbook could include in batch JCL. Other useful strategies may be discovered going forward.

2. Organizations will probably not want to specify profiles individually by hand. It's more likely they will have similar security profiles for people who work in particular roles and/or work with particular software product lines or related groups of applications. For example, they may have a common security profile for software developers who work on Asset Management applications, and one for software testers who work on Loan Origination, and one for system programmers who administer production LPARs, etc. 

In many cases, the only data item that would be different for profiles within the same category is the userid. All other security-related values would be the same for all userids in a given category. To support that, we may want to implement templates that can be copied and modified programmatically to produce numerous yaml files that define various RACF elements like users, groups, and resources. Alternatively, we could change the functionality so that it needs only one yaml file but outputs many RACF commands with different userids having the same attributes as the one example.

3. A company that uses z/OS and is serious about Infrastructure as Code for system management will undoubtedly want a "one-stop shop" for system configuration and provisioning. Since we are building this solution for Ansible, we can assume the "one-stop shop" will be Ansible. 

In that case, platform engineers will use Ansible to manage other types of managed nodes besides z/OS, and will probably manage multiple z/OS instances, as well. They will probably want a person or application to have the same userid across the board, for all platforms in the estate. Our solution pertains only to RACF on z/OS, but z/OS will not be the only game in town. 

We can't assume our solution will be the "boss" when it comes to defining or generating userids. That means we need not and should not build any functionality to generate userids or to manage their creation. We take whatever userids are given to us and ensure the RACF profiles align with them according to the company's standards. 
