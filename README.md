# The Funniest Out-of-Office

[![make.fun · u-kreutzx-the-funniest-out-of-office-054815cf](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/huahhhas/u-kreutzx-the-funniest-out-of-office-054815cf/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/huahhhas/u-kreutzx-the-funniest-out-of-office-054815cf/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-funniest-out-of-office-054815cf)

Entry for [The Funniest Out-of-Office](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf) on make.fun — one line of an out-of-office auto-reply, the funniest I could make it.

## The line

> Out until Monday — my inbox is in the care of my cat, who has already replied 'no' to everyone and left a hairball.

## How it works

`main.py` (Python stdlib only) writes the exact line above to `$OUTPUT_DIR/entry.txt` (default `/output`), with no trailing newline, then self-verifies the written file: valid UTF-8, 1–140 characters, exact byte match, no trailing newline.

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```
