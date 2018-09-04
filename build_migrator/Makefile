build:
	rm -rf rootfs || true
	cp -r ../code rootfs
	docker build -t beeckup/imap-migrator:dev .
	rm -rf rootfs || true