# Ansible sample setup for learning.

This directory contains a directory tree and files representative of a corporate Ansible setup for managing z/OS nodes. The playbooks and associated files demonstrate Ansible coding techniques and the use of IBM Ansible collections relevant to managing z/OS nodes.

## Playbooks 

### zos\_active\_started\_tasks 

Demonstrates the use of ibm.ibm\_zos\_core.zos\_job\_query to
list all the active started tasks on z/OS hosts.
  
Recent versions of Ansible support a simpler way to do 
this than it offered originally, but many installations
are still using older versions. This playbook shows both
ways of doing it.

### zos\_fetch\_dataset\_from\_host

Demonstrates

1. The use of ibm.ibm\_zos\_core.zos\_dataset\_fetch to copy an 
    MVS data set to a local file. 

2. The use of user-defined environment variables and "-e" 
   command-line arguments.

3. The use of ansible.builtin.assert to check for required 
   externally-provided values, in this case the z/OS dataset 
 name and local filename for the copy.

4. The use of include\_role to bring in a Role so that 
   variable expansion and other Ansible preliminary steps 
   happen in the right order.

### zos\_get\_master\_catalog\_info

Demonstrates the use of ibm.ibmi\_zos\_core.zos\_gather\_facts
to collect information about the Master Catalog.

### zos\_pds\_member\_list

Demonstrates how to issue a TSO command through Ansible.
This example does a LISTDS to get a list of members in
the Partitioned Data Set named in command line argument

-e "pds=ZOS.DATASET.NAME"

 It also demonstrates how to handle the yaml+TSO quotes and
 apostrophes when the name of the PDS is passed in as a
 variable.

### zos\_ping 

Pings a z/OS host to see if Ansible can communicate with it.

### zos\_provision\_developer\_libraries

Demonstrates how to set up a playbook as an orchestrator
to invoke one or more roles repeatedly to carry out a
series of similar operations. 
  
In this case, the operation is to delete and (re)allocate
z/OS source libraries such as an application developer
would normally use in their work, such as:
  
USER55.DEV.COBOL
USER55.DEV.COPYLIB
USER55.DEV.JCL
USER55.DEV.PROCLIB

### zos\_seed\_libraries  

Copy default members for developer source libraries to a
z/OS managed node.

Demonstrates

1. Checking for a required command-line argument and
   displaying a helpful message when it is missing.

2. A workaround for earlier versions of ibm\_zos\_core that
   don't fully initialize the connection until you hit
   the managed node with a command.
     
3. How to use Roles in a playbook.

4. How to process nested loops in playbooks and Roles.
  
5. How to write a data-driven automation playbook based on
   a specific directory structure and file naming convention.

### zos\_submit\_jcl\_from\_local

Demonstrates how to submit JCL stored on localhost to a z/OS host.

Demonstrates how to use a jinja2 template for the JCL, and
provide values for variables in the template to complete
the JCL statements. 

### zos\_submit\_jcl\_inline

Demonstrates how to submit inline JCL in a playbook.

## Directory tree

```shell
.
├── README.md                       This file.  
├── ansible.cfg                     Ansible configuration.
├── data                            Data used in some playbooks.
│   ├── provdev.jcl  
│   │   └── zoslab  
│   │       └── PROVDEV  
│   └── tmp  
│       └── zoslab  
│           └── JOB  
├── inventory                       ansible.cfg points here for inventory.                                        
│   ├── group\_vars  
│   │   └── all  
│   │       ├── all.yml  
│   │       └── vault.yml  
│   ├── host\_vars  
│   │   └── zoslab.yml  
│   └── hosts.yml  
├── play                             wrapper script for ansible-playbook.
├── playbooks                        Ansible Playbooks are here.
│   ├── roles                        Ansible Roles are here.
│   │   ├── submit\_library\_provisioning\_job  
│   │   │   └── tasks  
│   │   │       └── main.yml  
│   │   ├── zos\_dataset\_fetch  
│   │   │   └── tasks  
│   │   │       └── main.yml  
│   │   ├── zos\_job\_run  
│   │   │   └── tasks  
│   │   │       └── main.yml  
│   │   ├── zos\_local\_fs  
│   │   │   └── tasks  
│   │   │       └── main.yml  
│   │   └── zos\_seed\_library  
│   │       └── tasks  
│   │           ├── copy\_members.yml  
│   │           └── main.yml  
│   ├── seed\_files                 Seed files for playbook zos_seed_libraries
│   │   ├── ASM  
│   │   │   └── HELLO  
│   │   ├── COBOL  
│   │   │   ├── BTCHESDS  
│   │   │   ├── BTCHKSDS  
│   │   │   ├── BTCHRRDS  
│   │   │   ├── BTCHSKEL  
│   │   │   ├── CURREPOS  
│   │   │   ├── CURSCROL  
│   │   │   ├── CURUPDAT  
│   │   │   └── DATES  
│   │   ├── JCL  
│   │   │   ├── ASM.jcl  
│   │   │   └── HELLO.jcl  
│   │   ├── PROCLIB  
│   │   │   └── ASMBIND  
│   │   └── REXX  
│   │       ├── DATETIME  
│   │       ├── FACTORIA  
│   │       └── REXLIST  
│   ├── templates                  JCL templates for z/OS job submission  
│   │   └── provdev.jcl.j2  
│   ├── tmp\_jcl  
│   │   └── rendered.jcl  
│   ├── zos\_active\_started\_tasks.yml  
│   ├── zos\_fetch\_dataset\_from\_host.yml  
│   ├── zos\_master\_catalog\_info.yml  
│   ├── zos\_pds\_member\_list.yml  
│   ├── zos\_ping.yml  
│   ├── zos\_provision\_developer\_libraries.yml  
│   ├── zos\_seed\_libraries.yml  
│   ├── zos\_submit\_jcl\_from\_local.yml  
│   └── zos\_submit\_jcl\_inline.yml  
└── tmp                            Used for intermediate step in file transfers.
```


