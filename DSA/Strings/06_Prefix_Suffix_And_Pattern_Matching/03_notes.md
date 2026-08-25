# Prefix Suffix And Pattern Matching Pattern Notes

## Revision in 5 minutes

- LPS means longest proper prefix that is also suffix for each prefix.
- On mismatch in KMP, move pattern pointer to `lps[j - 1]`.
- For prefix/suffix problems, build `pattern + separator + text`.
- Use a separator character that cannot collide with input.
- Repeated substring pattern can be solved by LPS or string trick.

## Common mistakes

- Letting the separator appear in the input.
- Confusing LPS value with match start index.
- Resetting KMP pointer to zero too aggressively.
- Forgetting repeated string match may need one extra repeat.

## Revision in 1 minute

- Reuse matched prefix after mismatch. LPS tells where to resume.

