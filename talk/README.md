# Slides with marp
This repo contains a template for slides written in markdown.

### Convert to html with a template file
Pure markdown files can (currently) not split a slide in column without html.

To convert the slidedeck into a *.html file with marp

    hooked-on-hooks/talk$ marp --theme-set ngi-theme.css --html -w slides.md

Open http://localhost:8080/


### Local work with docker
Use the presentation in local mode with the `watch` command

    hooked-on-hooks/talk$ docker run --rm --init -v $PWD:/home/marp/app -e LANG=$LANG -p 8080:8080 -p 37717:37717 marpteam/marp-cli:v3.2.0 --theme ngi-theme.css --watch -s .

Convert slide deck into pdf
    hooked-on-hooks/talk$ docker run --rm -v $PWD:/home/marp/app/ -e MARP_USER="$(id -u):$(id -g)" -e LANG=$LANG marpteam/marp-cli:v3.2.0 --theme ngi-theme.css slides.md --pdf

Convert slide deck into html

    hooked-on-hooks/talk$ docker run --rm -v $PWD:/home/marp/app/ -e MARP_USER="$(id -u):$(id -g)" -e LANG=$LANG marpteam/marp-cli:v3.2.0 --theme ngi-theme.css slides.md --html

### Some issues to pay attention to

- [Import document](https://github.com/marp-team/marpit/issues/135) style.
