# A universal medium of expression

Nothing here is new. Each layer writes down, as simply as possible, a theory that already exists:

    extension.md    dependent type theory: Martin-Löf type theory, with universes and inductive families
         ↑
    base.md         a typed lambda calculus: with types made with |, functions on types, and recursion
         ↓
    primitive.md    the untyped lambda calculus: Church's, where every value is a function

## Examples

Each theory file holds only its rules. Its examples are in separate files, ordered so that each section uses only what comes before it:

- [example-types.md](example-types.md): every kind of type base allows
- [example-functions.md](example-functions.md): every kind of function base allows
- [example-claims.md](example-claims.md): claims and their evidence
