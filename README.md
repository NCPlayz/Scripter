# Scripter

Make a script using Python!

```python
from scripter import Script

my_script = Script("Macbeth", "Shakespeare")

act1 = my_script.add_act()

act1.add_scene("A Desert Place. Thunder and lightning. Enter three Witches.")

act1.add_dialogue("When shall we three meet again\nIn thunder lightning, or in rain?", author="First Witch")
# Rest of Act 1 Scene 1

if __name__ == '__main__':
    my_script.create("Macbeth")
    # Result in ./tests
```

## Dependencies
###### *They should be in `requirements.txt`*