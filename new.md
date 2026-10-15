T, c, f, x and y are names you pick; after n = v, n >> v
A, B, a, b, g, n, p, q, r, s and v stand for anything of the shape their block gives

    Type : Type

    A₁ : Type
    A₂ : Type      with x₁ : A₁
    ...
    B : Type       with x₁ : A₁,  x₂ : A₂,  ...
then
    (x₁ : A₁, x₂ : A₂, ...) → B  :  Type

    g : (x₁ : A₁, x₂ : A₂, ...) → B
    a₁ : A₁
    a₂ : A₂        with x₁ = a₁
    ...
then
    g(a₁, a₂, ...) : B      with x₁ = a₁,  x₂ = a₂,  ...

    aᵢ >> bᵢ
then
    g(a₁, ..., aᵢ, ...) >> g(a₁, ..., bᵢ, ...)

    T : Type     or     T : (y₁ : B₁, y₂ : B₂, ...) → Type
    T = c₁ : T₁  |  c₂ : T₂  |  ...       any number of cᵢ, none included
where each Tᵢ is
    T     or     (x₁ : A₁, x₂ : A₂, ...) → T
then
    c₁ : T₁,  c₂ : T₂,  ...
and every value of T works out to some cᵢ, or some cᵢ(a₁, a₂, ...)

p is a pattern of type A when p is
    x                 with x : A
    c                 with c : A
    c(p₁, p₂, ...)    with c : (x₁ : A₁, x₂ : A₂, ...) → A,  and each pᵢ a pattern of type Aᵢ
where each c is one of the cᵢ above, and each x appears once

a matches p when, for some v,
    x = v     for each x in p
makes
    p >> a

    f : (x₁ : A₁, x₂ : A₂, ...) → B
    f = (p₁, p₂, ...) ↦ r  |  (q₁, q₂, ...) ↦ s  |  ...       any number of cases, none included
where
    each pᵢ is a pattern of type Aᵢ
    r : B          with x₁ = p₁,  x₂ = p₂,  ...
    every a₁ : A₁,  a₂ : A₂,  ... matches exactly one case

    f = ...  |  (p₁, p₂, ...) ↦ r  |  ...
    a₁, a₂, ... match p₁, p₂, ...
then
    f(a₁, a₂, ...) >> r      with the same x = v
