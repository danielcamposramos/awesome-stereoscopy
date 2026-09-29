# Federated evidence reference

[`pointers.md`](pointers.md) is the generated map from this list to the
canonical Bravia hardware and standards claims it consumes. Each pointer pins
one semantic claim hash and its expected authority state; the claim body and
original evidence remain upstream.

The verifier fails if an upstream claim changes, disappears, is corrected or
superseded, or changes authority without an explicit downstream update.
