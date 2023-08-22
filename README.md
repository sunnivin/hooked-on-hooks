# Slides with marp 
This repo contains a NGI-template for slides written in markdown wu


### Convert to html with a template file
Pure markdown files can (currently) not split a slide in column without html. 

To convert the slidedeck into a *.html file: 

    # Server mode (Serve current directory in http://localhost:8080/)
    marp --theme-set ngi-theme.css --html -w model-validation-sexy-again.md


### Local work with docker
Use the presentation in local mode with the `watch` command 

    docker run --rm --init -v $PWD:/home/marp/app -e LANG=$LANG -p 8080:8080 -p 37717:37717 marpteam/marp-cli:v3.2.0 --theme-set ngi-theme.css -s .

Convert slide deck into pdf 
     docker run --rm -v $PWD:/home/marp/app/ -e MARP_USER="$(id -u):$(id -g)" -e LANG=$LANG marpteam/marp-cli:v3.2.0 --theme ngi-theme.css model-validation-sexy-again.md --pdf

Convert slide deck into html 

    docker run --rm -v $PWD:/home/marp/app/ -e MARP_USER="$(id -u):$(id -g)" -e LANG=$LANG marpteam/marp-cli:v3.2.0 --theme ngi-theme.css model-validation-sexy-again.md --html



### Some nice issues to pay attention to 

- [Import document](https://github.com/marp-team/marpit/issues/135) style. 


