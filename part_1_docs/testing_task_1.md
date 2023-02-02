### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  #self shouldnt be in the function variables
  def check_for_ace(self, card):
    if card.value = 1: #needs to be a double ==
      return True
    else # else needs a :
      return False
   
  # spelling error on line 27, dif
  dif highest_card(self, card1 card2): # missing a coma
  if card1.value > card2.value: # line 28 - 31 not indented properly
    return card # should be card1
  else:
    return card2
  

# all this indentation is wrong
def cards_total(self, cards):
  total #total is not defined so will error
  for card in cards:
    total += card.value
    return "You have a total of" + total # need to concatonate the int
  # the return is indented one too far
```
