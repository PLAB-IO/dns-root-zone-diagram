root.zone:
	curl -Ss -o root.zone https://www.internic.net/domain/root.zone

zone.csv: root.zone
	cat root.zone | awk '{print $$1";"$$4";"$$5}' > zone.csv

