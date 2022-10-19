#!/bin/sh
FILE="/lib/python3.10/site-packages/libqtile/widget/__init__.py"
TEXT="\"Playerctl\": \"playerctl\","
LINES=$(wc -l < $FILE)
LINE=$(echo "$LINES -2" | bc)


if ! [ "$(id -u)" = 0 ]; then\
	echo "You are not root, run this target as root please";\
	exit 1;\
fi
echo "copiing widget to widgets"
cp -f /home/silas/.config/qtile/mywidget/playerctl/playerctl.py /lib/python3.10/site-packages/libqtile/widget/playerctl.py
echo "adding Widget to __init__.py"
sed -i "${LINE} i \ \ \ \ ${TEXT}" ${FILE}

