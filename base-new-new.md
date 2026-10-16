Type is a type.

A new name n can be given a type A, if A is a type: then n : A.
After that, n can be given a value v, if v : A; v can use n. Then n works out to v.
Or, if n : Type, n can be given constructors, n = c₁ : T₁ | c₂ : T₂ | ...,
where each cᵢ is a new name and each Tᵢ is a type that gives back n: then cᵢ : Tᵢ.

If A is a type, and B is a type when x : A,
then (x : A) → B is a type.

If A is a type, and b : B when x : A,
then (x ↦ b) : (x : A) → B.

If T = c₁ : T₁ | c₂ : T₂ | ..., and each rᵢ : B with x replaced by cᵢ(y)(z)...,
when y, z, ... have the types Tᵢ gives them,
then (c₁(y)(z)... ↦ r₁ | c₂(y)(z)... ↦ r₂ | ...) : (x : T) → B.

If f : (x : A) → B and a : A,
then f(a) : B, with x replaced by a.

(x ↦ b)(a) works out to b, with x replaced by a.
(... | c(y)(z)... ↦ r | ...)(c(a)(b)...) works out to r, with y replaced by a, z by b, ...
Working out also happens as part of something larger, and step after step.

If a : A, B is a type, and A and B work out to the same thing,
then a : B.
