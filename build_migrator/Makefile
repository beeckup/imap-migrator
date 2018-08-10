build:
	rm -rf rootfs || true
	cp -r ../code rootfs
	docker build -t nutellinoit/imap-migrator:latest .
	rm -rf rootfs || true
push:
	docker push nutellinoit/imap-migrator:latest