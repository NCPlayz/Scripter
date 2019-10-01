from scripter import Script

my_script = Script("Macbeth", "Shakespeare")

act3 = my_script.add_act()

act3.add_scene("Rome. Before the Capitol; the Senate sitting above..")

# A3S1 Dialogue
act3.add_dialogue("[To the Soothsayer] The ides of March are come.", author="Caesar")
act3.add_dialogue("Ay, Caesar; but not gone.", author="Soothsayer")
act3.add_dialogue("Hail, Caesar! read this schedule.", author="ARTEMIDORUS")
act3.add_dialogue("Trebonius doth desire you to o'erread,", author="DECIUS BRUTUS")
act3.add_dialogue("At your best leisure, this his humble suit.", author="DECIUS BRUTUS")
act3.add_dialogue("O Caesar, read mine first; for mine's a suit", author="ARTEMIDORUS")
act3.add_dialogue("That touches Caesar nearer: read it, great Caesar.", author="ARTEMIDORUS")
act3.add_dialogue("What touches us ourself shall be last served.", author="CAESAR")
act3.add_dialogue("Delay not, Caesar; read it instantly.", author="ARTEMIDORUS")
act3.add_dialogue("What, is the fellow mad?", author="CAESAR")
act3.add_dialogue("Sirrah, give place.", author="PUBLIUS")
act3.add_dialogue("What, urge you your petitions in the street?", author="CAESAR")
act3.add_dialogue("Come to the Capitol.", author="CAESAR")
act3.add_direction("CAESAR goes up to the Senate-House, the rest following")


if __name__ == '__main__':
    my_script.create("Macbeth")
