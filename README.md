# Image Binarization Project

## I. THE PROBLEM

Image binarization is the process of taking a grayscale image and converting it to black-and-white, essentially reducing the information contained within the image from 256 shades of gray to 2: black and white, a binary image. This is sometimes known as image thresholding, although thresholding may produce images with more than 2 levels of gray. It is a form of segmentation, whereby an image is divided into constituent objects. This is a task commonly performed when trying to extract an object from an image. However, like many image processing operations, it is not trivial and is solely dependent on the content within the image. The trick is that images that may *seem* easy to convert to B&W are often not.

The process of binarization works by finding a threshold value in the histogram – a value that effectively divides the histogram into two parts, each representing one of two objects (or the object and the background). In this context, it is known as global thresholding.

## II. EASE OF USE

### A. Global Binarization

Global thresholding is based on the assumption that the image has a bimodal histogram and, therefore, the object can be extracted from the background by a simple operation that compares image values with a threshold value T [32, 132]. Global thresholding is computationally simple and fast. It works well on images that contain objects with uniform intensity values on a contrasting background. However, it fails if there is low contrast between the object and the background, if the image is noisy, or if the background intensity varies significantly across the image.

### B. Local Binarization

Local adaptive thresholding is used to convert an image consisting of grayscale pixels to just black and white pixels. Usually, a pixel value of 0 represents white, and the value 255 represents black, with the numbers from 1 to 254 representing different gray levels. Unlike the global thresholding technique, local adaptive thresholding chooses different threshold values for every pixel in the image based on an analysis of its neighboring pixels. This is to allow images with varying contrast levels where a global thresholding technique will not work satisfactorily. There are a number of different forms of adaptive thresholding algorithms reported in the image processing literature.

## III. SOLUTION

Input data is offered as a series of different binarization algorithm results for a certain image. Each image has an optimal value to be reached from these values. For global binarization, there are also interval measures. For local binarization, each pixel has a real value that belongs to a category (1 or 0). The next columns contain values resulted from different algorithms applied to that pixel. From these different solutions, the optimal value must be reached.

### A. Approach

To find the optimal value, a method of generating trees was proposed. Each leaf represents a value of an algorithm, whereas each node represents an operator. Operators are represented by algorithmic operators (+, -, /, *). Nodes, as well as trees, are randomly generated, and a tree’s root is the value obtained with all the operations. If it is close to the optimal value, the tree will be saved in a file and then tried on the next input. If it is not, a new tree will be generated. When a tree from a previous input is not close to the optimal value of a new input, a tree is generated from the new input, and then compared to the current one. If it has a better value, the new tree will replace the current one, being the best tree generated.
