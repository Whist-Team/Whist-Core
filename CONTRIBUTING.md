# How to contribute to Whist Core

First off contributions are very welcomed regardless of your level of expertise.

## Reporting a bug

We only follow up on bugs that are reported via a GitHub issue. So if you find a bug please create
an issue and use our issue template.

## Contribute to source code

### General specification

The name of the branch shall be `type/description`, where the description should be as short as
possible and the type one of the following.

- `feature`: For new additions
- `fix`: For fixes of a bug
- `doc`: Additional or rewritten documentation
- `refactor`: Rewritten source code. This includes typos and optimizations.
- `ci`: Changes made to the GitHub actions regardless of the type.

There are also some requirements for the title and the descriptions of a PR. They shall have one of
the following prefixes:

- `ADD:` completely new additions
- `UPDATE:`: extending existing code or documentation
- `FIX:`: bug fixes
- `REMOVE`: removal of code or documentation
- `REFACTOR:`: rewritten code

### Choosing a base

There are three types of contributions.

1. Adding breaking changes
2. Adding no breaking changes, fixes, cosmetics or refactors, etc.

Keep this in mind while choosing a base for your PR. For **breaking changes** the base is next
release candidate for the next major version. The second type shall be based against the main
branch.

The RC branches are named `rc/vM.0.0-nn`, where `M` is the next major version and `nn` the number of
the next RC of that major version.

## Contributing to documentation

This can always be based against the main branch.

