#!/usr/bin/apl --script
x←⎕
⍞←{⍵[↑⍋⍵]}{+/{(⍵×(⍵+1))÷2}|x-⍵}¨⍳x[↑⍒x]
)OFF
