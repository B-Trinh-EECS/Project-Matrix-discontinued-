# SMTP Sleuth — Solution & Walkthrough

**Goal:** Find flag in email headers.

**Step-by-step:**
1. Open the message:
   ```
   cat smtp/email.eml
   ```
2. Inspect headers. `X-Flag` contains:
   ```
   X-Flag: falcon{m41l_1nspect0r}
   ```
**Flag:** `falcon{m41l_1nspect0r}`
