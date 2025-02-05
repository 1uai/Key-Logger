def Decode_the_text(file_name):
        # Strips the newline character
    lists=[]
    with open(f"{file_name}","r")as file:
        Lines = file.readlines()
        for line in Lines:
            # recreate the object from the json dict by loading the json and
            # use as keyword parameters to KeyboardEvent
            lists.append(keyboard.KeyboardEvent(**json.loads(line)))
    keyboard.play(lists, speed_factor=1)
