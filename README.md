# pdf-gen
Script to automatically make pdf's from images in any folders

## Prerequisites
* Image Magick
	`choco install imagemagick`
* Img2pdf
	`pip3 install img2pdf`

## How To Use
Call pdf_gen.py with flag -o to mark desired output file and every file or folder that you want to look for images in (recursively searches subfolders automatically).
Keep in that mind that files are added to pdf in the order of their file names.

## Example
`pdf_gen.py -o {output-file-name}.pdf assets/ image-name.png`

Will look for files in assets folder and also add image-name.png to pdf with name {output-file-name}.pdf

## Usage Example


## TODO
- [ ] Make it interactive
- [ ] Use img2pdf as a library instead
- [ ] Somehow get rid of imagemai=gick as a dependancy as well, so that only python script needs to be there
