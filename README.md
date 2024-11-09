Prerequisites:

1. DeepMD software installed and the path added to the system environment variable.
2. Numpy and Matplotlib installed.
3. Cuda installed in compatible version.

To run the code:

1. prepare the DeepMD data(.npy) in 3 directory: train/ test/ validate/
2. python3 dp2xyz.py (you'll get 3 file named: train.xyz, test.xyz, validate.xyz in the same directory)
3. gather the .xyz file and nep.in and run_nep.sh in the neptraindir/

Remind: Don't forget to modify the nep.in according to your model system(element type and number, training parameters, etc).

