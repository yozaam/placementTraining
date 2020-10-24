# Required concepts: https://www.w3schools.com/python/python_intro.asp strings

print('Question: Shoot your neighbours, Josephus Problem')

n = int(input('how many ppl stand in circle: '))

kills = 0
cur_gun_holder = 0
to_shoot = -1
dead = set()

while cur_gun_holder != to_shoot:
  # who to shoot? 
  # whoever is alive and next to me!!!!
  to_shoot = (cur_gun_holder+1)%n
  while to_shoot in dead:
    to_shoot = (to_shoot+1)%n
  print(cur_gun_holder+1,'shoots',to_shoot+1)
  if cur_gun_holder == to_shoot:
    break
  # now we kill him
  dead.add(to_shoot)
  kills += 1

  # who gets the gun ?
  # next alive guy
  cur_gun_holder = (cur_gun_holder+1)%n
  while cur_gun_holder in dead:
    cur_gun_holder = (cur_gun_holder+1)%n

print('Answer:')
print(cur_gun_holder, 'is alive')

"""
# Superb Circular Linked List Solution!

while node.next:

  node.next = node.next.next # kill your next!
  node = node.next # pass the gun
"""