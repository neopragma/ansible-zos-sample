Parking Lot

1. Architectural improvement.

Right now the pipeline is

YAML
 ↓
loader
 ↓
validator
 ↓
planner
 ↓
dispatcher
 ↓
strategy
 ↓
commands

The validator is validating the raw dictionary.

Evolve it toward:

YAML
 ↓
loader
 ↓
validator
 ↓
model
 ↓
planner
 ↓
dispatcher
 ↓
strategy

where load\_yaml() returns a UserModel dataclass instead of a dictionary. Then everything after validation works with typed objects instead of nested dicts and string keys like "base" and "omvs". That would eliminate an entire class of bugs caused by typos in dictionary keys.


2. Organizations will probably not want to specify profiles individually by hand. It's more likely they will have similar security profiles for people who work in particular roles and/or work with particular software product lines or related groups of applications. For example, they may have a common security profile for software developers who work on Asset Management applications, and one for software testers who work on Loan Origination, and one for system programmers who administer production LPARs, etc. 

In many cases, the only data item that would be different for profiles within the same category is the userid. All other security-related values would be the same for all userids in a given category. 

A common scenario:

- Group A is a parent group for the role, "application developer". Group A may have some access authority defined that is meant to apply to all software developers in the organizatin.

- Groups B, C, D are groups for different application development teams. These groups belong to Group A. Each has access authority defined for resources that pertain to the particular application development area. These groups are the default groups for user profiles in each application development area. 

- A user whose role is "application developer" has UPDATE on datasets whose high-level qualifiers match the user's TSO id. They also have the same access to resources defined for their respective group. 

The organization will want to tell us the userids that belong in each application development area and have the tool generate the necessary RACF commands to provision this. It would be desirable to avoid having to replicate the same profile schemas when the only difference between them is the userid. 

To support that, we may want to implement templates that can be copied and modified programmatically to produce numerous yaml files that define various RACF elements like users, groups, and resources. Alternatively, we could change the functionality so that it needs only one yaml file but outputs many RACF commands with different userids having the same attributes as the one example.

3. In many cases, userids in certain categories always have UPDATE authority on datasets whose high-level qualifiers match their TSO userids. Consider implementing an option to set this as a default behavior when creating userids for a given category (or given categories) of users. That is, when such a userid is processed with state: "present", the tool automatically generates a database resource command and a PERMIT command. Then it would be unnecessary to specify these separately. This does not apply to all userids (and it may not be the policy in a given organization), so there needs to be an appropriate way to manage it as an optional setting. 
