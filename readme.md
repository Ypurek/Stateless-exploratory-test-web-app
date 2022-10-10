# Stateless web app for exploratory testing
Developed for [Dev Challenge 19](https://www.devchallenge.it/)

## Tasks
### Easy - find input string validations and issues (10 point each)
- String 6-14 chars
- Allowed chars a-zA-Z0-9!@#
- At least 1 letter capital
- Exactly 2 digits, but not next to each other
- !@# not more than 2 any special chars
- Issue with entering non-unicode chars (cyrillic) - fixed 
- Hint on enter empty string
- Spaces before/after are stripped
### Medium - find out checkbox switch logic
- State switch 0 -> 1 -> 2 -> 35 -> 467 -> 26 -> 1 (30 points)
- All other states moves to -> 1 (10 points)
- Checkbox 8 is checked, if within checkboxes 1-7 even number were checked, unchecked if odd (30 points)
### Hard - find key (50 points)
- Part 1 - in cookies
- Part 2 - in css
- Part 3 - in hidden endpoint /task3 (there are api calls task1 and task2. should be deducted)
- 3 parts of key - base64 encoded string, should be placed in correct order and decoded
