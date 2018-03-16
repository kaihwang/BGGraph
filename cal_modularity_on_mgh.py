#example script to run modularity analysis
import numpy as np
import bct as bct
from itertools import combinations
import glob
import os

def community_matrix(membership,min_community_size=5):
	membership = np.array(membership).reshape(-1)
	final_matrix = np.zeros((len(membership),len(membership)))
	final_matrix[:] = np.nan
	connected_nodes = []
	for i in np.unique(membership):
		if len(membership[membership==i]) >= min_community_size:
			for n in np.array(np.where(membership==i))[0]:
				connected_nodes.append(int(n))
	community_edges = []
	between_community_edges = []
	connected_nodes = np.array(connected_nodes)
	for edge in combinations(connected_nodes,2):
		if membership[edge[0]] == membership[edge[1]]:
			community_edges.append(edge)
		else:
			between_community_edges.append(edge)
	for edge in community_edges:
		final_matrix[edge[0],edge[1]] = 1
		final_matrix[edge[1],edge[0]] = 1
	for edge in between_community_edges:
		final_matrix[edge[0],edge[1]] = 0
		final_matrix[edge[1],edge[0]] = 0
	return final_matrix


## Loop through MGH subjects
MGH_subjects = glob.glob('/home/despoB/connectome-thalamus/MGH/Sub*')

MGH_CI = []
MGH_Left_CI = []
MGH_Right_CI = []
MGH_Q = []
MGH_LQ = []
MGH_RQ = []

for s, path in enumerate(MGH_subjects):

	path = path + '/MNINonLinear/'
	os.chdir(path)

	for run in np.arange(1,3):
		cmd = "3dNetCorr -prefix roi_correlation_run%s -inset rfMRI_REST%s.nii.gz -in_rois /home/despoB/kaihwang/Rest/BG/ROIs/400ROIs.nii.gz" %(run, run)
		os.system(cmd)

		fn = 'roi_correlation_run%s_000.netcc' %run
		
		try:
			matrix = np.loadtxt(fn)
		except:
			continue
		
		matrix = matrix[2:,:]
		#note, roi 1-200 is left, 201-400 is right
		right_matrix = matrix[200:,200:]
		left_matrix = matrix[0:200,0:200] 

		num_iter = 200
		consensus = np.zeros((200, matrix.shape[0], matrix.shape[1]))
		left_consensus = np.zeros((200, left_matrix.shape[0], left_matrix.shape[1]))
		right_consensus = np.zeros((200, right_matrix.shape[0], right_matrix.shape[1]))

		qs = np.zeros(200)
		left_qs = np.zeros(200)
		right_qs = np.zeros(200)

		for i in np.arange(0,num_iter):
	
			ci, qs[i] =bct.modularity_louvain_und_sign(matrix, qtype='sta')
			consensus[i, :,:] = community_matrix(ci)

			ci, left_qs[i] =bct.modularity_louvain_und_sign(left_matrix, qtype='sta')
			left_consensus[i, :,:] = community_matrix(ci)

			ci, right_qs[i] =bct.modularity_louvain_und_sign(right_matrix, qtype='sta')
			right_consensus[i, :,:] = community_matrix(ci)		


		mean_matrix = np.mean(consensus, axis=0)	
		mean_matrix[np.isnan(mean_matrix)]=0

		mean_left_matrix = np.mean(left_consensus, axis=0)	
		mean_left_matrix[np.isnan(mean_left_matrix)]=0

		mean_right_matrix = np.mean(right_consensus, axis=0)	
		mean_right_matrix[np.isnan(mean_right_matrix)]=0

		CI, _ = bct.modularity_louvain_und_sign(mean_matrix, qtype='sta')
		meanQ = np.mean(qs)

		LCI, _ = bct.modularity_louvain_und_sign(mean_left_matrix, qtype='sta')
		LmeanQ = np.mean(left_qs)

		RCI, _ = bct.modularity_louvain_und_sign(mean_right_matrix, qtype='sta')
		RmeanQ = np.mean(right_qs)


		MGH_CI = MGH_CI + [CI]
		MGH_Left_CI = MGH_Left_CI + [LCI]
		MGH_Right_CI = MGH_Right_CI + [RCI]

		MGH_CI = MGH_CI + [CI]
		MGH_Left_CI = MGH_Left_CI + [LCI]
		MGH_Right_CI = MGH_Right_CI + [RCI]
		

		MGH_Q = MGH_Q + [meanQ]
		MGH_LQ = MGH_LQ + [LmeanQ]
		MGH_RQ = MGH_RQ + [RmeanQ]
		

		#np.save('144_Modular_Partition', CI)
		#np.save('144_meanQ', meanQ)
		#np.save('144_Modular_Partition_Left', LCI)
		#np.save('144_meanQ_Left', LmeanQ)
		#np.save('144_Modular_Partition_Right', RCI)
		#np.save('144_meanQ_Right', RmeanQ)







