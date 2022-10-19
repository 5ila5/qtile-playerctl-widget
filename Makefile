FILE ?= /lib/python3.10/site-packages/libqtile/widget/__init__.py
TEXT ?= \"Playerctl\": \"playerctl\",
LINES ?= $(shell wc -l < $(FILE))
LINE ?= $(shell echo ${LINES} -2 | bc)


install:
	@if ! [ "$(shell id -u)" = 0 ]; then\
			echo "You are not root, run this target as root please";\
			exit 1;\
	fi
	echo "copiing widget to widgets"
	cp -f playerctl.py /lib/python3.10/site-packages/libqtile/widget/playerctl.py
	echo "${FILE}"
	echo "vairables assinged"
	echo "$(( $( wc -l < $(FILE)) -4 )) i ${TEXT}"
	echo $(LINES)
	echo $(LINE)

	$(shell sed -i "${LINE} i \ \ \ \ ${TEXT}" ${FILE})