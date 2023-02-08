import sys
import thngs

if len(sys.argv) < 5:
    print(f"Usage: {sys.argv[0]} <category> <uid> <type> <value>")
    sys.exit(1)

[_, category_name, uid, info_type, info_value] = sys.argv
category = thngs.Category(category_name)

if uid not in category.things:
    print("Thing doesn't exist")
    sys.exit(1)

thing = category.things[uid]

if info_type not in thing.info:
    thing.info[info_type] = info_value
else:
    info = thing.info[info_type]
    if isinstance(info, list):
        info.append(info_value)
    else:
        thing.info[info_type] = [info, info_value]

category.save()
