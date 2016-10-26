import sima
import sima.motion
from sima.motion import HiddenMarkov2D
from shutil import copy, copytree
import argparse
import sys

def motion(datadir):
	
	sequences = [sima.Sequence.create('TIFF', datadir)]
	mc_approach = sima.motion.PlaneTranslation2D(max_displacement=[15, 30])
	dataset = mc_approach.correct(sequences, 'example_translation2D.sima')
	mc_approach2 = sima.motion.HiddenMarkov2D(granularity='row', max_displacement=[80, 100], verbose=False)
	dataset2=mc_approach2.correct(sequences, 'example_HM.sima')
	dataset.export_frames([[['frames.tif']]], fmt='TIFF16')
	#dataset2.export_frames([['frames_HM2D.tif']],fmt='TIFF16')
	dataset.export_averages(['avgs.tif'],fmt='TIFF16')
	dataset2.export_averages(['avgsMC.tif'],fmt='TIFF16')



def main(argv):
	argParser=argparse.ArgumentParser()
	argParser.add_argument('-d',"--signalFile", action="store", type=str, default='',
 	   help="the signal pickle file to plot")


	args = argParser.parse_args()
	
	motion(args.signalFile)






if __name__=="__main__":
        main(sys.argv[1:])
