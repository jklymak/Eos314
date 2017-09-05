build:
	bundle exec jekyll build --incremental

upload: build
	rsync -av _site/ unix.uvic.ca:www/Eos314

serve:
	bundle exec jekyll serve --config _config.yml,_debug.yml
