This file sets down signs, and rules for writing with them. The signs mean nothing beyond what the rules say about them. The words next to each sign are only a way to read it aloud: a reader who skips them and follows the rules loses nothing.

The language is written in expressions. The simplest expression is a name: a word such as n, zero or Bool, possibly with a small number below it, such as x₁. Every other expression is built from smaller expressions, in one of the forms given below. Since the smaller expressions can be built the same way, forms can be put inside forms, to any depth.

In this file, a single letter, such as a, b, A, B, f or r, stands for any expression, and is not part of the language. The same letter stands for the same expression everywhere it appears in one rule. A list written a₁, a₂, ... has one or more expressions, unless it is said to have none.

a : A is a statement, read "a is of type A". A statement is true or not, and only rules make one true. A rule is written

    P₁,  P₂,  ...   ⟹   C          read: if the statements P₁, P₂, ... are true, the statement C is true

and a rule with nothing before ⟹ is written as just C: C is true. The true statements are exactly the ones the rules make true, in finitely many steps.

When a : A is true, a is called a value of A, and A is called a type.

Type is an expression. The first two rules:

    Type : Type                    Type is a type
    a : A   ⟹   A : Type           the type of any value is a value of Type

Text in the language is a list of lines. A line is not a statement: it gives a name, and makes statements about that name true. The first two kinds of line:

    n : A          n is a new name: it appears in no line before. Allowed only when A : Type is true. Makes n : A true.
    n = v          comes after n : A, and v can use n and any name that appears before. Allowed only when v : A is true.

a >> b is a statement, read "a works out to b". a ≡ b is a statement, read "a is the same as b". A line n = v makes n >> v true, and:

    a >> a
    a >> b,  b >> d   ⟹   a >> d
    a >> d,  b >> d   ⟹   a ≡ b
    a : A,  A ≡ B   ⟹   a : B

A function type is written

    (x₁ : A₁, x₂ : A₂, ...) → B          read: the type of functions that take an x₁ of type A₁, an x₂ of type A₂, ..., and give back a value of type B

Each xᵢ is a new name, called a variable: no line gives it a value, and it stands for whichever input is given. xᵢ can appear only in Aᵢ₊₁, Aᵢ₊₂, ... and B, and while they are checked, xᵢ : Aᵢ is true. Then:

    A₁ : Type,  A₂ : Type,  ...,  B : Type   ⟹   (x₁ : A₁, x₂ : A₂, ...) → B : Type

A value of a function type is called a function.

r[x₁ := a₁, x₂ := a₂, ...] is r with each xᵢ replaced by aᵢ, everywhere it appears in r. A part of r that brings in its own xᵢ, as a function type or a pattern below does, keeps its own xᵢ. A name that a part of r brings in, and that appears in some aᵢ, is first changed to a new name, so that aᵢ keeps its meaning.

A call is written

    f(a₁, a₂, ...)          read: f given the inputs a₁, a₂, ...

    f : (x₁ : A₁, x₂ : A₂, ...) → B,  a₁ : A₁,  a₂ : A₂[x₁ := a₁],  ...   ⟹   f(a₁, a₂, ...) : B[x₁ := a₁, x₂ := a₂, ...]

The inputs of a call can be worked out, and so can what is called:

    f >> g   ⟹   f(a₁, a₂, ...) >> g(a₁, a₂, ...)
    aᵢ >> bᵢ   ⟹   f(a₁, ..., aᵢ, ...) >> f(a₁, ..., bᵢ, ...)

A type made of constructors is given in two lines:

    T : Type                         or, if T takes inputs, T : (y₁ : B₁, y₂ : B₂, ...) → Type
    T = c₁ : T₁ | c₂ : T₂ | ...      | is read "or"; the list can have any number of cᵢ, none included

Each cᵢ is a new name, called a constructor: no line gives it a value, and it stands for nothing else. Each Tᵢ is either T, or a function type (x₁ : A₁, x₂ : A₂, ...) → T. If T takes inputs, each cᵢ takes y₁, y₂, ... first, and T here means T(y₁, y₂, ...). The second line makes each cᵢ : Tᵢ true.

An expression is finished when it is Type, a function type, a function made of cases (below), a constructor, or a name given by a line T = c₁ : T₁ | ...; and c(a₁, a₂, ...) or T(a₁, a₂, ...) is finished when each aᵢ is. A finished expression works out only to itself, so two finished expressions are the same only if they are written the same way, except for the names of their variables.

The finished values of T are exactly the cᵢ with Tᵢ = T, and the cᵢ(a₁, a₂, ...) with each aⱼ finished, built in finitely many steps.

All the types these rules allow, with examples: [example-types.md](example-types.md)

A function made of cases is written

    (p₁, p₂, ...) ↦ r | ...          read: for inputs that match p₁, p₂, ..., give back r; ...

The list can have any number of cases, none included, and each case has its own p₁, p₂, ... and r.

Each pᵢ is a pattern. A pattern of type A is one of:

    x                    a new variable, written without a type: matches any finished a : A, and stands for it
    c                    for a constructor c : A: matches only c
    c(q₁, q₂, ...)       for a constructor c : (z₁ : C₁, z₂ : C₂, ...) → A, with each qⱼ a pattern of type Cⱼ[z₁ := q₁, ..., zⱼ₋₁ := qⱼ₋₁]

Each c is one of the cᵢ in T = c₁ : T₁ | c₂ : T₂ | ..., where A is T, or T(e₁, e₂, ...). Each variable appears only once in p₁, p₂, ....

Finished a₁, a₂, ... match p₁, p₂, ... when there are b₁, b₂, ... for the variables w₁, w₂, ... of p₁, p₂, ... with each aᵢ written as pᵢ[w₁ := b₁, w₂ := b₂, ...].

Let F be (p₁, p₂, ...) ↦ r | .... F : (x₁ : A₁, x₂ : A₂, ...) → B is true when, for each case:

- each pᵢ is a pattern of type Aᵢ[x₁ := p₁, ..., xᵢ₋₁ := pᵢ₋₁];
- r : B[x₁ := p₁, x₂ := p₂, ...], while w : C is true for each variable w of a pattern of type C;

and every finished a₁ : A₁, a₂ : A₂, ... match the patterns of exactly one case.

A call of F works out once its inputs are finished:

    a₁, a₂, ... finished, and match p₁, p₂, ... of a case (p₁, p₂, ...) ↦ r of F, with b₁, b₂, ...   ⟹   F(a₁, a₂, ...) >> r[w₁ := b₁, w₂ := b₂, ...]

Nothing inside F is worked out before F is called. Working out can go on without end.

All the functions these rules allow, with examples: [example-functions.md](example-functions.md)
