Type is a type.

A new name n can be given a type A, if A is a type: then n : A.
After that, n can be given a value v, if v : A; v can use n. Then n works out to v.

If A is a type, and B is a type when x : A,
then (x : A) → B is a type.

If A is a type, and b : B when x : A,
then (x ↦ b) : (x : A) → B.

If f : (x : A) → B and a : A,
then f(a) : B, with x replaced by a.

(x ↦ b)(a) works out to b, with x replaced by a.
Working out also happens as part of something larger, and step after step.

If a : A, B is a type, and A and B work out to the same thing,
then a : B.
