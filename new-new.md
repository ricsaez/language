    Type : Type

`Type` is a value of type `Type`

    ((<a> : <A : Type>) -> <B : Type, <a> : <A>>) : Type

`((<a> : <A : Type>) -> <B : Type, <a> : <A>>)`, the type of functions that take a value `<a>` of type `<A>`, where `<A>` is filled with a value of type `Type`, and return a value of type `<B>`, where `<B>` is filled with a value of type `Type` and may use `<a>` as a value of type `<A>`, is a value of type `Type`

    (<a> ↦ <C : <B>, <a> : <A>>) : ((<a> : <A : Type>) -> <B : Type, <a> : <A>>)

`(<a> ↦ <C : <B>, <a> : <A>>)`, the function that takes `<a>` and gives back `<C>`, where `<C>` is filled with a value of type `<B>` and may use `<a>` as a value of type `<A>`, is a value of type `((<a> : <A : Type>) -> <B : Type, <a> : <A>>)`

    <F : ((<a> : <A : Type>) -> <B : Type, <a> : <A>>)>(<V : <A>>) : <B, <a> := <V>>

`<F>(<V>)`, the call of `<F>` with `<V>`, where `<F>` is filled with a value of type `((<a> : <A>) -> <B>)` and `<V>` is filled with a value of type `<A>`, is a value of type `<B, <a> := <V>>`, which is `<B>` with every `<a>` replaced by `<V>`

    (<a> ↦ <C>)(<V>) >> <C, <a> := <V>>

`(<a> ↦ <C>)(<V>)` works out to `<C>` with every `<a>` replaced by `<V>`

    (<a> ↦ <C>) >> (<b> ↦ <C, <a> := <b>>)
    ((<a> : <A>) -> <B>) >> ((<b> : <A>) -> <B, <a> := <b>>)

an input can be renamed to any `<b>` that does not appear in `<C>` or `<B>`

    <X> >> <X>

    <X> >> <Y>,
    <Y> >> <Z>
  =>
    <X> >> <Z>

    <X> >> <Y>
  =>
    (<a> ↦ <X>) >> (<a> ↦ <Y>)
    ((<a> : <X>) -> <B>) >> ((<a> : <Y>) -> <B>)
    ((<a> : <A>) -> <X>) >> ((<a> : <A>) -> <Y>)
    <X>(<V>) >> <Y>(<V>)
    <F>(<X>) >> <F>(<Y>)

working out goes in any number of steps, and inside any part of an expression

    <X> >> <Z>,
    <Y> >> <Z>
  =>
    <X> ≡ <Y>

`<X>` and `<Y>` are the same when they work out to the same thing

    <V : <A>>,
    <A> ≡ <B : Type>
  =>
    <V> : <B>

a value of a type is a value of any type that is the same
