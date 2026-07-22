BACKLOG.md

1. Renderer enhancements (in progress).

1.1. Don't add elements that have no value (value is None) to RACF commands.
1.2. Add helper functions to assemble parts of each command.
1.3. Introduce the idea of a "strategy" to control how commands are built (e.g., "combined" or "separate"). Define a variable for the strategy so that a default can be set in the Ansible environment, and so that invididual playbooks can set the value as needed. Later we can add logic to choose the strategy based on higher-level criteria such as "minimize traffic between the control node and the managed node" or "maximize granularity of commands and their output" or "transmit commands in batches and pause between batches, to avoid overloading the managed node".
1.4. Add test cases for missing values (None).
1.5. Ensure all tests pass - imports and assertions are likely to change.
1.6. Ensure test playbook runs correctly.

2. Support processing a directory instead of a single file.

2.1. Add support for directory and adjust APIs and test cases accordingly.
2.2. Sort filenames to ensure consistent command order across multiple invocations.
2.3. Adjust test cases so all tests pass. 
2.4. Adjust the test playbook to exercise this functionality and ensure it runs correctly. 

3. Improve error reporting.

3.1. Throughout the code, check for errors and provide meaningful messages for playbook authors as well as for developers who are debugging issues.
3.2. Consider adding an error message identifier or code to facilitate finding explanatory information in the documentation when debugging.
3.3. Begin preparing documentation of error messages that includes suggested corrective actions.
3.4. Expand the test suite to cover this functionality.
3.5. Adjust the test playbook to exercise this functionality and ensure it runs correctly. 
 
4. Add support for RACF groups.

Note: Groups must exist before users can be connected to them. This includes the default group, if specified on ADDUSER or ALTUSER.

The sequence of commands must be:

first
ADDGROUP x

then
ADDUSER DFLTGRP(x)
or
ADDUSER
ALTUSER DFLTGRP(x)

then
CONNECT userid GROUP(x)

Details TBD.

5. Add support for RACF database resources.

Details TBD.

6. Add support for state: absent.

Note: This will require removing users from groups before user profiles can be deleted.
Details TBD.

7. Add support for User CICS segment.

8. Parking lot items (parking\_lot.md).

Details TBD.
