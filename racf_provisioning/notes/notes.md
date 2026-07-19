
# Ansible z/OS RACF provisioning - rough notes for documentation

## Purpose 

The purpose of the Ansible z/OS RACF provisioning framework is to help bring the z/OS platform into the world of DevOps and Infrastructure as Codeby making it easy (for some definition of "easy") to define the _desired state_ of RACF profiles in a platform-independent way, and to parse and format the output returned from RACF (TSO) commands into a form easily consumable by Linux/UNIX-based tooling and by people familiar with Linux/UNIX conventions. 

## Limitations

There is no intention to abstract the details of RACF and z/OS away from platform engineers so that they need not learn about that environment. It is only meant to facilitate the automation of security provisioning for z/OS using Ansible. No one wants people ignorant of RACF and z/OS to define security profiles. 

## License 

(TBD)

## Versioning

[Semantic Versioning](https://semver.org)

## Architecture

The RACF provisioning framework is organized as a pipeline of independent components, each with a single responsibility.

- The YAML model expresses the desired RACF configuration in a declarative language. It describes what state is desired, not how to achieve it.

- The schema defines the language. It specifies the valid objects, attributes, data types, required fields, and other structural constraints that a model may contain. This is python code.

- The validator verifies that a model conforms to the schema. It validates structure, types, and generic constraints without any knowledge of RACF semantics. This is python code.

- The planner interprets a valid model as a set of desired RACF operations. It applies RACF-specific rules, determines dependencies, sequences operations, and produces an implementation plan. This is the outermost layer that is aware of RACF. It consists of python code.

- The renderer converts the implementation plan into executable RACF commands (for example, ADDUSER, ALTUSER, CONNECT, PERMIT, and others). Renderers are responsible only for formatting commands; they do not make provisioning decisions. This layer also provides helpers to format the output returned from TSO into a consistent format. This is useful because the exact values returned and the shape of the data vary by release of RACF, release of z/OS, and some configuration details of the z/OS managed node. This layer consists of Ansible modules. This is the "user" or "client" interface.

## Design principles 

General principles:

- Declarative models — Profile files describe the desired RACF state, not the commands needed to achieve it.

- Separation of concerns — Schema definition, validation, planning, and command rendering are implemented independently.

- Schema-driven development — The schema is the authoritative definition of the language. Validators, documentation, and tooling are derived from it whenever practical.

- Operation-oriented planning — Provisioning is planned as a sequence of RACF operations rather than a one-to-one mapping to RACF commands.

- Extensibility — Each RACF object type (users, groups, datasets, started tasks, etc.) follows the same architecture and can evolve independently.

## Team organization 

A core group of people may be interested in investing significant personal time in developing, caretaking, and maintaining the project. We call them _active team members_. There is no official team lead. There are few rules and little formality. The team operates on the basis of trust. Members are expected to use good judgment and "do the right thing" while maintaining the standards and guidelines agreed on for the project.

Individuals may join and withdraw over time as their personal interest, priorities, and availability change. When a person is engaged as an active team member, they have the responsibility to see that the standards are followed (unless a genuine need to change them arises) and guidelines are respected (or violated thoughtfully), both in their own contributions and when reviewing pull requests submitted by others.

The preference is for active team members to use _mainline development_ (also known as [trunk-based development](https://trunkbaseddevelopment.com/)). Changes are made to the main branch, except for short-lived branches for bug-fixes or experiments. This requires self-discipline to ensure all tests are passing (and possibly more than that, depending on circumstances) before finalizing changes. 

If mainline development proves infeasible, the team can revert to multiple branches and a pull request system. Mainline development has worked well on some open source projects and not others. Its success depends on the level of collaboration, mutual trust, and individual self-discipline on the team.

People who do not want to serve as active team members may have an interest in contributing changes or enhancements because they need the framework to support particular functionality that isn't implemented, or because they see opportunities for refactoring, extending the test suite, or improving the documentation. 

They are encouraged to submit pull requests for review by an active team member. All active team members are authorized to review and approve pull requests. The team member working on the pull request is responsible for ensuring any changes adhere to the project's standards and guidelines. They might make changes to the submission themselves, work with the submitter to make any necessary adjustments, or a combination.

The active team is largely self-governing. Anyone can join by expressing interest. Anyone can leave with no hard feelings. However, when it is discovered that an active team member has used their access to the code to carry out malicious acts (injecting malware, capturing private information, etc.), they can be removed from the team immediately.

## Standards and guidelines for contributing

_Standards_ are relatively strong, in the nature of "rules." When standards have to change, a more-or-less formal change process has to be carried out by the active team members, and significant testing has to be done to ensure no regressions are introduced, no security holes are opened, and breaking changes are clearly communicated to the user community and included in the documentation for the first version that employs the new standards.

_Guidelines_ are meant to provide guardrails against issues that can make the project harder to understand and maintain. Guidelines can be violated, given good reasons.

Many Internet-based standards documents use the terms MUST, SHOULD, and MAY. Standards are at the MUST level and guidelines are at the SHOULD level.  

### Standards 

1. **Thou shalt pay attention to well-known and emergent security risks.** Follow generally-known good practices to avoid exposing vulnerabilities in the code. As you learn more about security threats and defensive code, apply those lessons. When new exploits are discovered and documented, for instance from [CISA](https://www.cisa.gov/), [ENISA](https://www.enisa.europa.eu/), [ITSEC](https://www.itsec.gov.cn/), [METI](https://www.meti.go.jp/english/policy/safety_security/cybersecurity/index.html), [ASD](https://www.cyber.gov.au/), the [FBI](https://www.fbi.gov/investigate/cyber/alerts), the [NSA](https://www.nsa.gov/), [The Hacker News](https://thehackernews.com/), or any other source, immediately communicate the risk to the user community and make any necessary changes to the code to avoid problems. The z/OS platform hosts systems of record for the largest financial institutions and government agencies around the world. Anything that touches one of these systems in any way has to be as secure as is practical. As this project directly relates to security management on z/OS, security has to be our number one concern.

2. **Thou shalt not introduce regressions.** There are no mandatory development or testing practices, but however you choose to work you must not allow any regressions. We will not debate you on the merits of exploratory testing, regression testing, approval testing, or test-driven development. If you use some other approach or methods that guarantee no regressions will be introduced, that's fine. It would be wonderful to learn about a new method that out-performs those...provided it really does so. One way or another, you must not introduce regressions.

3. **Thou shalt not make breaking changes, excepting when the top-level version number is incremented.** IBM has a long history of assuring backwared compatibility for customers of its mainframe product line. As that product line embraces newer technologies, the commitment to backward compatibility must be upheld across the board. The project uses [Semantic Versioning](https://semver.org). The Semantic Versioning guidelines state that every system must clearly document the public API, either in code or as documentation. In this case, the API is the boundary between the planner and the renderer. The renderer will be Ansible playbook code written by users of the framework. The API consists of the Ansible roles and filter functions exposed by the planner.

4. **Thou shalt maintain clear separation of concerns.** When adding or enhancing functionality, do not cross the responsibility boundaries between the layers or stages of the process: model, schema, validator, planner, renderer.

5. **Thou shalt not leave code in place that lacks test coverage.** While this is useful for most projects, it is particularly important here because we will not always have a z/OS system available for testing. Thorough executable checks at each stage of the process, combined with thoughtful and careful exploratory testing, provide a partial safety net during periods when we are not able to test against a live z/OS system.

6. **Thou shalt fail early and noisily.** In the production code, validate what is appropriate to validate at each stage of the process and do not allow errors to propagate to the next stage. The implications for test code relate to standard No. 5. "Noisily" in this context means to provide as much meaningful and useful diagnostic information as is available as of the time the error is detected. (This is one of Eric Raymond's guidelines from _The Art of UNIX Programming_.)

7. **Thou shalt deprecate before removing.** When an API or any functionality is to be removed or modified in a way that breaks existing clients, we will first mark it as _deprecated_ and maintain support for it until the next major version level increment. Deprecation warnings will be enabled by default, and users can disable them by setting an Ansible variable. Deprecation warnings appear at the renderer layer.

8. **Thou shalt use English for formal project-related communication.** English is the _de facto_ common language in the information technology field. Documentaton, source comments, version control commit messages, and publicly-documented issues are to be written in English. Informal communication among team members and external contributors may be done in any language the participants understand. In case of misunderstanding due to translation between languages, the English-language version of the information prevails.

