CRACK  = crack_attack
SERVER = attack_server

CRACK_FILE  = crack_attack.py
SERVER_FILE = attack_server.py

all: $(CRACK) $(SERVER)

$(CRACK): $(CRACK_FILE)
	cp $< $@ && chmod +x $@

$(SERVER): $(SERVER_FILE)
	cp $< $@ && chmod +x $@

clean:
	rm $(CRACK) $(SERVER)