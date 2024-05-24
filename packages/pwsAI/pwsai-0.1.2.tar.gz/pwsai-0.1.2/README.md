Welcome to PWS_AI
-------------------
This code is incomplete in that the gui is not completely finished.
Coming up on the gui is the ability to check the results for the threshold so
the segmentation is optimized by the user before going to check it on 
pwspy analysis software. 

As it stands, you will go through 5 main steps. 

Step 0) Run analysis on dataset of interest, that means running it on the pws 
	 analysis software 

Step 1) Select folder with cell data where you just ran your analysis (same way its
	done on the pwspy software) 

Step 2) Access rms images from analysis. This is done automatically when you click
	the button "Get RMS Images" 

Step 3) Use PWS_AI to generate the ROIs automatically and save them as TIF File in
        Corresponding Folder 

Step 4) Conver the PWS_AI output into the pwspy compatible format. Done by clicking 
	"Push ROI TO PWSPY" 


Once this is done you can go to the pws analysis software where you can now use the 
AI generated ROIs. This is a beta version and not ready for release but thank you for 
testing it out! 

- Nico 6/15/23

### Building
PIP can be used to build a "wheel" for distribution by navigating to the root directory (where "setup.py" is located) and running `python -m build`. The produced files will be placed into the "dist" folder. You can distribute the .whl file yourself and install using PIP or you can upload the .whl to the PyPi repository online for easy download access (`pip install pwsAI`). To upload to PyPi you will need "twine" (`pip install twine`) and you will need to configure twine with the proper credentials to log into your PyPi account. Then upload with `python -m twine upload ./dist/*`.

Once pwsAI has been installed you can run the GUI either by running `python -m pwsAI` or by using the `PwsAiGui` alias.