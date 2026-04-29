.RECIPEPREFIX = >
all:
>pdflatex report.tex
>pdflatex report.tex # Run twice for references to be updated correctly.
cleantemp:
>rm -f *.aux *.log *.out *.toc # to delete all created files except the pdf file
clean:
>rm -f *.aux *.log *.out *.toc *.pdf # to delete all files created including the output pdf file