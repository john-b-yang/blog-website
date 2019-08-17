server = sitebuilder.py

# usage: make preview
preview:
	python $(server)

# usage: make push m="commit message"
push:
	git add -A && \
	git commit -m "$(m)" && \
	git push origin master

# usage: make deploy m="commit message"
deploy:
	python $(server) build && \
	cd ../Website && \
	git pull origin master && \
	cp -r ../build/* . && \
	cp -r ../build/*.gitignore . && \
	git add -A && \
	git commit -m 'deploy: $(m)' && \
	git push origin master	
