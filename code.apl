⍝ the check function in apl
⍝ takes the universe on the left and the word to check as a character vector on the right
check ← {0=≢⍵:1 ⋄ ∨/⍺∘∇¨(⍺∩(⍳≢⍵)∘.↑⊂⍵)∘.{(≢⍺)↓⍵}⊂⍵}