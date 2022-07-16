list = [5, "текст", 555, 13.6, None, True, {1,10}, TypeError, (20, 20)]
for i, object in enumerate(list, 1):
    print(f"{i} {object} - {type(object)}")