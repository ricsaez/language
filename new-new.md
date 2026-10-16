    Type : Type

`Type` is a value of type `Type`

    ((<a> : <A : Type>) -> <B : Type, <a> : <A>>) : Type

`((<a> : <A : Type>) -> <B : Type, <a> : <A>>)`, the type of functions that take a value `<a>` of type `<A>`, where `<A>` is filled with a value of type `Type`, and return a value of type `<B>`, where `<B>` is filled with a value of type `Type` and may use `<a>` as a value of type `<A>`, is a value of type `Type`

    (<a> ↦ <C : <B>, <a> : <A>>) : ((<a> : <A : Type>) -> <B : Type, <a> : <A>>)

`(<a> ↦ <C : <B>, <a> : <A>>)`, the function that takes `<a>` and gives back `<C>`, where `<C>` is filled with a value of type `<B>` and may use `<a>` as a value of type `<A>`, is a value of type `((<a> : <A : Type>) -> <B : Type, <a> : <A>>)`

    <F : ((<a> : <A : Type>) -> <B : Type, <a> : <A>>)>(<V : <A>>) : <B, <a> := <V>>

`<F>(<V>)`, the call of `<F>` with `<V>`, where `<F>` is filled with a value of type `((<a> : <A>) -> <B>)` and `<V>` is filled with a value of type `<A>`, is a value of type `<B, <a> := <V>>`, which is `<B>` with every `<a>` replaced by `<V>`
