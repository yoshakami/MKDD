# MKDD
all pyhon scripts and C# Launchers I programmed to mod Mario Kart Double Dash

you can use the Launchers executables to assign bmd/bco/dae/obj/bol/bti files to various applications used to mod mario kart double dash
the apps are just launchers, they contain no app content, you need to get them separately.
you will also need to edit the .txt file created by the launcher if it can't find python executable or the .py file location (put the launcher in the app directory)
I tried to make a smart detection of python's base path, but if you installed python elsewhere it won't detect it, you'll have to put it manually in the .txt file


you can download exe versions in the exe folder, but be sure to have python39.dll alongside them

edit: those exe were .py files compiled with nuitka, and may be unstable/won't run at all without python.... better run from source code

bti info.py ---------- Show info from all bti files in current directory

bti mkdd custom track fix.py - Fix all files ending with extension .bti in current directory (editing wrapping to "clamp" remove corrupted looking on read console for 2d layout bti)

bti-fix-recursive.py --------- Same as above but also look down to 9 subdirectories and autodetect bti files (no need to have .bti extension to ne recognizable)

mkdd_checkpoint_swap.py ------ Given a bol file, it swap all left and right coordinates of all checkpoints between the two offsets entered

patcher-fix.py --------------- Browse from your current directory to max 9 subdirectories, and rename all file types used in custom track to their name in <a href="https://github.com/RenolY2/mkdd-track-patcher/releases">Yoshi2's patcher</a>


.
### The scripts below need <a href="https://szs.wiimm.de/download.html#vers">Wiimms SZS Tools</a>

BTI.py -------- Drag and Drop some png files into this script and it will convert all of them to BTI.CMPR

PNG.py -------- Drag and Drop X bti to recieve X png

jpaeffect editor.py --- A Command Line Script used to manipulate, dump, edit, replace, or view all bti images inside /MRAM.arc/effect/jpaeffect.jpc  remember to make a copy of your vanilla file if you're going to replace some bti as it will overwrite on the file.
the easiest way to use it would be : copy jpaeffect.jpc in the same directory as the script, then launch it
-choose mode 4 to dump all bti
-press enter to convert all dumped bti to png
-navigate to ./jpaeffect Dumped Textures/png
-edit the png files you want to edit (without resizing them)
-choose mode 6 to convert back png to bti with wiimms szs tools and replace them into the file.

the alt folder contains not working - alternative versions for the scripts going into subfolders.
the recursive function didn't worked, the one with blob was missing some rename conditions, and I made some other attempts whose ended up not working.
