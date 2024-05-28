/-
Copyright (c) 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Leonardo de Moura
-/
prelude
import Init.NotationExtra

namespace Lean.Parser
/--
A user-defined simplification procedure used by the `simp` tactic, and its variants.
Here is an example.
```lean
simproc reduce_add (_ + _) := fun e => do
  unless (e.isAppOfArity ``HAdd.hAdd 6) do return none
  let some n ← getNatValue? (e.getArg! 4) | return none
  let some m ← getNatValue? (e.getArg! 5) | return none
  return some (.done { expr := mkNatLit (n+m) })
```
The `simp` tactic invokes `reduce_add` whenever it finds a term of the form `_ + _`.
The simplification procedures are stored in an (imperfect) discrimination tree.
The procedure should **not** assume the term `e` perfectly matches the given pattern.
The body of a simplification procedure must have type `Simproc`, which is an alias for
`Expr → SimpM (Option Step)`.
You can instruct the simplifier to apply the procedure before its sub-expressions
have been simplified by using the modifier `↓` before the procedure name. Example.
```lean
simproc ↓ reduce_add (_ + _) := fun e => ...
```
Simplification procedures can be also scoped or local.
-/
syntax (docComment)? attrKind "simproc " (Tactic.simpPre <|> Tactic.simpPost)? ("[" ident,* "]")? ident " (" term ")" " := " term : command

/--
A user-defined simplification procedure declaration. To activate this procedure in `simp` tactic,
we must provide it as an argument, or use the command `attribute` to set its `[simproc]` attribute.
-/
syntax (docComment)? "simproc_decl " ident " (" term ")" " := " term : command

/--
A builtin simplification procedure.
-/
syntax (docComment)? attrKind "builtin_simproc " (Tactic.simpPre <|> Tactic.simpPost)? ("[" ident,* "]")? ident " (" term ")" " := " term : command

/--
A builtin simplification procedure declaration.
-/
syntax (docComment)? "builtin_simproc_decl " ident " (" term ")" " := " term : command

/--
Auxiliary command for associating a pattern with a simplification procedure.
-/
syntax (name := simprocPattern) "simproc_pattern% " term " => " ident : command

/--
Auxiliary command for associating a pattern with a builtin simplification procedure.
-/
syntax (name := simprocPatternBuiltin) "builtin_simproc_pattern% " term " => " ident : command

namespace Attr
/--
Auxiliary attribute for simplification procedures.
-/
syntax (name := simprocAttr) "simproc" (Tactic.simpPre <|> Tactic.simpPost)? : attr

/--
Auxiliary attribute for symbolic evaluation procedures.
-/
syntax (name := sevalprocAttr) "sevalproc" (Tactic.simpPre <|> Tactic.simpPost)? : attr

/--
Auxiliary attribute for builtin simplification procedures.
-/
syntax (name := simprocBuiltinAttr) "builtin_simproc" (Tactic.simpPre <|> Tactic.simpPost)? : attr

/--
Auxiliary attribute for builtin symbolic evaluation procedures.
-/
syntax (name := sevalprocBuiltinAttr) "builtin_sevalproc" (Tactic.simpPre <|> Tactic.simpPost)? : attr

end Attr

macro_rules
  | `($[$doc?:docComment]? simproc_decl $n:ident ($pattern:term) := $body) => do
    let simprocType := `Lean.Meta.Simp.Simproc
    `($[$doc?:docComment]? def $n:ident : $(mkIdent simprocType) := $body
      simproc_pattern% $pattern => $n)

macro_rules
  | `($[$doc?:docComment]? builtin_simproc_decl $n:ident ($pattern:term) := $body) => do
    let simprocType := `Lean.Meta.Simp.Simproc
    `($[$doc?:docComment]? def $n:ident : $(mkIdent simprocType) := $body
      builtin_simproc_pattern% $pattern => $n)

macro_rules
  | `($[$doc?:docComment]? $kind:attrKind simproc $[$pre?]? $[ [ $ids?:ident,* ] ]? $n:ident ($pattern:term) := $body) => do
     let mut cmds := #[(← `($[$doc?:docComment]? simproc_decl $n ($pattern) := $body))]
     let pushDefault (cmds : Array (TSyntax `command)) : MacroM (Array (TSyntax `command)) := do
       return cmds.push (← `(attribute [$kind simproc $[$pre?]?] $n))
     if let some ids := ids? then
       for id in ids.getElems do
         let idName := id.getId
         let (attrName, attrKey) :=
           if idName == `simp then
             (`simprocAttr, "simproc")
           else if idName == `seval then
             (`sevalprocAttr, "sevalproc")
           else
             let idName := idName.appendAfter "_proc"
             (`Parser.Attr ++ idName, idName.toString)
         let attrStx : TSyntax `attr := ⟨mkNode attrName #[mkAtom attrKey, mkOptionalNode pre?]⟩
         cmds := cmds.push (← `(attribute [$kind $attrStx] $n))
     else
       cmds ← pushDefault cmds
     return mkNullNode cmds

macro_rules
  | `($[$doc?:docComment]? $kind:attrKind builtin_simproc $[$pre?]? $n:ident ($pattern:term) := $body) => do
    `($[$doc?:docComment]? builtin_simproc_decl $n ($pattern) := $body
      attribute [$kind builtin_simproc $[$pre?]?] $n)
  | `($[$doc?:docComment]? $kind:attrKind builtin_simproc $[$pre?]? [seval] $n:ident ($pattern:term) := $body) => do
    `($[$doc?:docComment]? builtin_simproc_decl $n ($pattern) := $body
      attribute [$kind builtin_sevalproc $[$pre?]?] $n)
  | `($[$doc?:docComment]? $kind:attrKind builtin_simproc $[$pre?]? [simp, seval] $n:ident ($pattern:term) := $body) => do
    `($[$doc?:docComment]? builtin_simproc_decl $n ($pattern) := $body
      attribute [$kind builtin_simproc $[$pre?]?] $n
      attribute [$kind builtin_sevalproc $[$pre?]?] $n)

end Lean.Parser
