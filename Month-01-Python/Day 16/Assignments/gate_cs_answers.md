# Day 16 - GATE CS Assignments

## 1. Why is dictionary lookup O(1) on average?
A Python dictionary is a hash table. To look up a key, Python:
1. Computes `hash(key)`, an integer.
2. Maps it to a slot index in the table (using the hash and the table size).
3. Goes directly to that slot and compares the key stored there.

No scanning through other elements is needed, so the cost does not grow with the number
of items `n`. The table is resized as it fills (keeping the load factor low) and the hash
function spreads keys well, so collisions are few and each probe sequence is short on
average. Hence the **expected (average) cost is O(1)**. This is an average-case
guarantee, not an unconditional one.

## 2. Worst-case complexity of searching in a Python set?
**O(n).** Sets are hash tables too. Average membership test is O(1), but if many elements
collide, the search may have to probe through up to all `n` elements.

## 3. n dictionary lookups, average-case lookup?
Each lookup is O(1) on average, so n lookups take n x O(1) = **O(n) expected total time**.
(Worst case would be O(n^2) if every lookup degraded to O(n).)
