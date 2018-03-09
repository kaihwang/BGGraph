#!/bin/sh


for s in 116 118 120 121 122 138 143 144 146 154 189; do

	#mkdir /home/despoB/kaihwang/Rest/BG/${s}
	cd /home/despoB/kaihwang/Rest/BG/${s}
	#ln -s /home/despoB/azhu/Lesion\ Masks/sub_${s}_mask_agnes.nii.gz /home/despoB/kaihwang/Rest/BG/${s}/sub-${s}_mask_agnes.nii.gz
	#ln -s /home/despoB/lesion/data/original/nifti/sub_${s}/anat/t1mprage.nii.gz /home/despoB/kaihwang/Rest/BG/${s}/sub-${s}_T1w.nii.gz
	#ln -s /home/despoB/lesion/data/original/nifti/sub_${s}/anat/sub-${s}_acq-TSE_T2w.nii.gz /home/despoB/kaihwang/Rest/BG/${s}/sub-${s}_acq-TSE_T2w.nii.gz
	#ln -s /home/despoB/lesion/data/original/nifti/sub_${s}/anat/sub-${s}_acq-TIRM_FLAIR.nii.gz /home/despoB/kaihwang/Rest/BG/${s}/sub-${s}_acq-TIRM_FLAIR.nii.gz

	ln -s /home/despoB/dlurie/Projects/despolab_lesion/data/patients/preproc/out/fmriprep/sub-${s}/func/sub-${s}_task-rest_acq-128px_run-01_bold_space-MNI152NLin2009cAsym_preproc.nii.gz .
	ln -s /home/despoB/dlurie/Projects/despolab_lesion/data/patients/preproc/out/fmriprep/sub-${s}/func/sub-${s}_task-rest_acq-128px_run-02_bold_space-MNI152NLin2009cAsym_preproc.nii.gz .
	ln -s /home/despoB/dlurie/Projects/despolab_lesion/data/patients/preproc/out/fmriprep/sub-${s}/func/sub-${s}_task-rest_acq-128px_run-01_bold_space-T1w_preproc.nii.gz .
	ln -s /home/despoB/dlurie/Projects/despolab_lesion/data/patients/preproc/out/fmriprep/sub-${s}/func/sub-${s}_task-rest_acq-128px_run-02_bold_space-T1w_preproc.nii.gz .
	ln -s /home/despoB/dlurie/Projects/despolab_lesion/data/patients/preproc/out/fmriprep/sub-${s}/func/sub-${s}_task-rest_acq-128px_run-01_bold_confounds.tsv .
	ln -s /home/despoB/dlurie/Projects/despolab_lesion/data/patients/preproc/out/fmriprep/sub-${s}/func/sub-${s}_task-rest_acq-128px_run-02_bold_confounds.tsv .
	ln -s /home/despoB/dlurie/Projects/despolab_lesion/data/patients/preproc/out/fmriprep/sub-${s}/anat/sub-${s}_T1w_space-MNI152NLin2009cAsym_preproc.nii.gz .

	ln -s /home/despoB/lesion/anat_preproc/${s}/${s}_mask_mni.nii.gz .

done