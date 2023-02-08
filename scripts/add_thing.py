import sys
import thngs

if len(sys.argv) < 4:
    print(f"Usage: {sys.argv[0]} <category> <uid> <name>")
    sys.exit(1)

category = thngs.Category(sys.argv[1])
if sys.argv[2] in category.things:
    print("Thing already exists")
    sys.exit(1)

category.things[sys.argv[2]] = thngs.Thing(sys.argv[3])
category.save()
