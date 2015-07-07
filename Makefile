# A Makefile for commands I run frequently:

# Build GitHub Page from docs
build:
	git checkout summer ; \
	cactus build ; \
	mkdir /tmp/knot63-build ;\
	cp -r .build/*  /tmp/knot63-build/
	git checkout master ; \
	cp -r /tmp/knot63-build/* .
	rm -rf /tmp/knot63-build
	git add -A ; \
	git commit -m "Updated build from summer" ; \
	git push
