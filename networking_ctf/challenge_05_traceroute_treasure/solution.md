# Traceroute Treasure — Solution & Walkthrough

**Goal:** Assemble flag fragments from traceroute hop metadata.

**Step-by-step:**
1. View hops:
   ```
   cat traceroute/hops.txt
   ```
2. Read the `info:` values per hop and concatenate:
   ```
   part1='falcon{r0' + part2='ut3_' + part3='hunt3r}' => falcon{r0ut3_hunt3r}
   ```
**Flag:** `falcon{r0ut3_hunt3r}`
