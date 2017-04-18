# Image filter
### Task #3
[[pptx]](https://www.dropbox.com/s/cpjm9szra28zm1y/Task%203.pptx?dl=0) [[repository]](https://github.com/Andrew414/filtertask) [[russian]](https://github.com/Andrew414/filtertask/blob/master/README.rus.md)

### Description
You should implement a program that can apply different graphic filters to some images and measure its performance. Filters should be parallelized with MAP paradigm, which means that each pixel of the output image should be calculated independently based on one or several pixels from the input image. 

You should measure performance and show its statistics in CLI or GUI. You shoud print how many megapixels and how many megabytes are processed in one second.

You need to choose one or more filters and put them to `README.md` file in your local folder in repository. 

Examples of filters:
* Color channels modification
  * Filters that modify (add/remove) color channels in images
  * Filters that convert color images to black and white images
  * Filters that binarize images based on different thresholds
  * Filters that change pixel brightness with bijective functions
* Linear filters
  * Low pass filters (blur)
  * High pass filters (sharpening)
* Non-linear filters
  * Median filter
  * Max (morphology dilation) filter
  * Min (morphology erosion) filter
* Histogram processing
  * Histogram equalization
  * Histogram building *(not actually a filter, but you can choose it)*
 
 
### Additional tasks
There are three additional tasks:
* Implement 3 or more different filters
  * You should choose several filters of different kinds, for example, you can't implement Median, Dilation and Erosion non-linear filters because their implementations are too similar. Filters should be chosen in CLI, GUI or passed via parameters
* Implement filters as GPU kernels (subprograms)
  * The part that applies the filter should be written in `CUDA` language or some close low-level alternative (`OpenCL` kernels, shaders) with explicit CPU and GPU code blocks, explicit GPU memory management and explicit GPU-part execution, and it should run on real GPU device or on its simulation. 
* Add GUI to your task
  * GUI should allow you to choose the input and output images, filters (if you implemented more than one filter), also it should show the progress and stats of filter application

### Github repository
[Github repository](https://github.com/Andrew414/filtertask) consists of one main [`README.md`](https://github.com/Andrew414/filtertask/blob/master/README.md) page and fourteen personal folders. You need to fork the repository and make changes in your local folder only. All local folders contain an empty `.gitignore` file that you need to fill in with your project's temp files. Also, for this task, you need to create your own `README.md` and list the selected filters in it. The rest of the files should be your code and project files.

### Passing the task
You can choose any programming language, IDE and framework(s) for implementing this task. If some uncommon configurations or installations are required, please provide some instructions for setting up the test environment. 

You can't use libraries or frameworks that do a very similar job that task requires. For example, you can use some tool that performs format-to-bitmap conversion (reads image file and provides an interface to read/modify each single pixel), but can't use libs like OpenCV that can apply a filter multithreadingly with GPU by calling one function.

You should create a **pull request** from your forked repository to the task repository. Your pull request should contain **only code, project files (including maybe test files) and informational files (.gitignore, README.md)**. You should not include build results and temp files.

### Score
You can earn up to **10 points** for this task.
- **4 points** for implementing the main task (filter + performance tests)
- **3 points** for finishing in time
- **1 point** for implementing *3 or more* different filters
- **1 point** for implementing filters as *GPU kernels*
- **1 point** for implementing *GUI*

### Time frames
You have four weeks (April 3 - May 1) to pass the task. The task is passed when your Pull Request gets approved. The days when your are waiting for my review are not counted. 
![ ](https://i.snag.gy/lPOzf7.jpg)

For example, if you pass the task 3 weeks after its start (April 24) and I provide my feedback one week after last day (May 8), you still have 1 week to fix all issues, all days after your commit and before my review are not counted.


### Good luck!
