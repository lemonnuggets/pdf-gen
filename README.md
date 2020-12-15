# pdf-gen
Script to automatically make pdf's from images in any folders

## Prerequisites
* **Image Magick**

	install both
	
	`pip install wand`
	
	https://docs.wand-py.org/en/latest/guide/install.html#install-imagemagick-windows
	
	
* **Img2pdf**
	
	`pip install img2pdf`

## How To Use
Call pdf_gen.py with flag -o to mark desired output file and every file or folder that you want to look for images in (recursively searches subfolders automatically). Note that files are added to pdf in the order of their file names.

## Example
`pdf_gen.py -o {output-file-name}.pdf assets/ image-name.png`

Will look for files in assets folder and also add image-name.png to pdf with name {output-file-name}.pdf

## Usage Example
#### Directories and Subdirectories
![1](https://github.com/lemonnuggets/pdf-gen/blob/master/github-assets/1.png?raw=true)
![2](https://github.com/lemonnuggets/pdf-gen/blob/master/github-assets/2.png?raw=true)
![3](https://github.com/lemonnuggets/pdf-gen/blob/master/github-assets/3.png?raw=true)

#### Command and Output
![4](https://github.com/lemonnuggets/pdf-gen/blob/master/github-assets/4.png?raw=true)
![5](https://github.com/lemonnuggets/pdf-gen/blob/master/github-assets/5.png?raw=true)

## TODO
- [ ] Make it interactive
- [x] Use img2pdf as a library instead
- [x] Somehow get rid of imagemagick as a dependancy as well, so that only python script needs to be there
