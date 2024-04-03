def cat(food, state='still hungry', action='meow', breed='Siamese'):
    print(f"-- This cat wouldn't {action}", end=' if you gave it soup')
    print(f"if you gave it {food}")
    print(f"-- Lovely fur, the {breed}")
    print(f"-- It's {state}!")


cat(action='growl', food='soup', breed='Sphinx', state='still hungry')
cat('soup', 'still hungry', 'growl', 'Sphinx')