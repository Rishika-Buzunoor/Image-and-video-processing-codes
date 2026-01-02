------------Image-Enhancement Algorithms------------
openCV uses BGR to scan the image ,but matplot lib used RGB to print the image so,after image scanned by CV2 image is converted to RGB(for matplotlib.
For Histogram equalization , it works on gray scale intensity values so convert into gray and store in other image variable.
HISTOGRAM_EQUALIZATION:Stretches frequent values and compress the rare values.It redistributes the intensity values and enhances global contrast.Dark images get brighter.-non-linear enhancement
CONTRAST STRETCHING:lineraly maps the intensity values in the range[0,255] converts back into valid image format(uint8)-linear-enhancement 
UNSHARP MASKING:Applies gaussian blur with kernel size (5,5) 10.0 is standard deviation,enhances the edges and increase the fine details.
GAMMA CORRECTION:if gamma>1 image becomes darker and brighter otherwise.LUT lookuptable makes it fast.
