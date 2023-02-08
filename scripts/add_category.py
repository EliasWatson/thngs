import sys
import thngs

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <name>")
    sys.exit(1)

category = thngs.Category(sys.argv[1], should_exist=False)
category.save()
