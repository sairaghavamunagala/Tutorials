| Operation            | Examples              | Complexity Class | Average Case  | Amortised Worst Case |
|----------------------|-----------------------|------------------|---------------|----------------------|
| Append               | `l.append(item)`      | O(1)             | O(1)          | O(1)                 |
| Clear                | `l.clear()`           | O(1)             | O(1)          | O(1)                 |
| Containment          | `item in/not in l`    | O(N)             | O(N)          | O(N)                 |
| Copy                 | `l.copy()`            | O(N)             | O(N)          | O(N)                 |
| Delete               | `del l[i]`            | O(N)             | O(N)          | O(N)                 |
| Extend               | `l.extend(…)`         | O(N)             | O(N)          | O(N)                 |
| Equality             | `l1 == l2`, `l1 != l2`| O(N)             | O(N)          | O(N)                 |
| Index                | `l[i]`                | O(1)             | O(1)          | O(1)                 |
| Iteration            | `for item in l:`      | O(N)             | O(N)          | O(N)                 |
| Length               | `len(l)`              | O(1)             | O(1)          | O(1)                 |
| Multiply             | `k*l`                 | O(k*N)           | O(k*N)        | O(k*N)               |
| Min, Max             | `min(l)`, `max(l)`    | O(N)             | O(N)          | O(N)                 |
| Pop from end         | `l.pop(-1)`           | O(1)             | O(1)          | O(1)                 |
| Pop intermediate     | `l.pop(item)`         | O(N)             | O(N)          | O(N)                 |
| Remove               | `l.remove(…)`         | O(N)             | O(N)          | O(N)                 |
| Reverse              | `l.reverse()`         | O(N)             | O(N)          | O(N)                 |
| Slice                | `l[x:y]`              | O(y-x)           | O(y-x)        | O(y-x)               |
| Sort                 | `l.sort()`            | O(N*log(N))      | O(N*log(N))   | O(N*log(N))          |
| Store                | `l[i] = item`         | O(1)             | O(1)          | O(1)                 |
