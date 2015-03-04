# A Makefile for commands I run frequently:
clean:
	rm -f .build

# Build GitHub Page from docs
build:
	cactus build ; \
	git checkout gh-pages ; \
	cp -r .build/* . ; \
	rm -rf .build
	git add -A ; \
	git commit -m "Updated page from master" ; \
	git push -u origin gh-pages ; \
	git checkout master
