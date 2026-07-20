# Architectural rationale and overview 

The project aims to support RACF provisioning through declaratively-defined specifications of RACF profiles. The project has a layered architecture in which each layer has specific responsibilities.

## Main functions 

### Define and validate RACF definitions 

- Model
- Schema
- Validator

### Respond to user requests to generate RACF commands and other inputs to the z/OS node to achieve users' goals

- Planner 
- Renderer

### Parse and format output returned from the z/OS node

- Parser


### Model

Each RACF profile type is modeled in yaml. Instances of model templates are declarative specifications of the desired state of RACF definitions. Each type of template corresponds to a RACF profile type, such as user, group, and resource. The specifications do not map directly to RACF command syntax.

The intent is to make it relatively easy to define the desired state of RACF definitions and to provide a consistent structure for the definitions so that future tooling can generate model instances for specific configurations.

### Schema

The schema layer defines a domain-specific language (DSL) based on the yaml definitions to express the desired state of RACF security configurations. 

### Validator

The validator checks that the syntax and semantics of model instances conform to the DSL.

### Planner

The planner interprets the DSL and determines a strategy or plan for realizing the desired state of the RACF configuration. The plan may be influenced by factors such as

- number of resources of a given type to be defined (users, generic database resources, etc.)
- relative importance of minimizing execution time vs. managing groups of related resource definitions, etc.

### Renderer

The renderer converts the operations specified in the plan into sequences of RACF commands and other z/OS commands as needed to realize the desired state on the target z/OS system. Clients, such as Ansible playbooks, interact with the renderer.

### Parser 

The parser converts the responses from z/OS to individual commands and the spooler output from TSO/RACF batch jobs into a consistent format that is easy for Linux/UNIX-based tools to work with. Clients, such as Ansible playbooks, interact with the parser.

## Design principles

General principles:

- Declarative models — Profile files describe the desired RACF state, not the commands needed to achieve it.

- Separation of concerns — Schema definition, validation, planning, and command rendering are implemented independently.

- Schema-driven development — The schema is the authoritative definition of the language. Validators, documentation, and tooling are derived from it whenever practical.

- Operation-oriented planning — Provisioning is planned as a sequence of RACF operations rather than a one-to-one mapping to RACF commands.

- Extensibility — Each RACF object type (users, groups, datasets, started tasks, etc.) follows the same architecture and can evolve independently.

 
