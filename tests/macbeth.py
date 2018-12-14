from scripter import Script

my_script = Script("Macbeth", "Shakespeare")

act1 = my_script.add_act()

act1.add_scene("A Desert Place. Thunder and lightning. Enter three Witches.")

# A1S1 Dialogue
act1.add_dialogue("When shall we three meet again\nIn thunder lightning, or in rain?", author="First Witch")
act1.add_dialogue("When the hurlyburly's done,\nWhen the battle's lost and won.", author="Second Witch")
act1.add_dialogue("That will be ere the set of sun.", author="Third Witch")
act1.add_dialogue("Where the place?", author="First Witch")
act1.add_dialogue("Upon the heath", author="Second Witch")
act1.add_dialogue("There to meet with Macbeth.", author="Third Witch")
act1.add_dialogue("I come, Graymalkin!", author="First Witch")
act1.add_dialogue("Paddock calls.", author="Second Witch")
act1.add_dialogue("Anon.", author="Third Witch")
act1.add_dialogue("Fair is foul, foul is fair:\nHover through the fog and filthy air.", author="ALL")
act1.add_direction("Exeunt.")


if __name__ == '__main__':
    my_script.create("Macbeth")
