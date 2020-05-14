





class msf_csv_extract():

	def __init__(self,file):

		self.file = file

		self.temp_lst = []

		self.msf_detail_dict = {}
		self.exploit_detail_dict = {}
		self.auxiliary_detail_dict = {}
		self.post_detail_dict = {}

		self.parse_msf_modules()

	def parse_msf_modules(self):
		with open(self.file) as fp:
			while True: 
				line = fp.readline() 
		 
				if not line: 
					break
				# print "*"*34
				self.temp_lst=  line.replace(" ","")
				self.temp_lst = self.temp_lst.split("CVE")
		
				temp_vr = 1
				temp_exploi_save = ''
				for i in self.temp_lst:
					if temp_vr == 1:
						# print i
						temp_exploi_save = i
					else:
						temp_cve_save = "CVE"+i
						temp_cve_save = temp_cve_save.replace("\n","")

						self.msf_detail_dict[temp_cve_save] = temp_exploi_save
					temp_vr +=1

	def msf_auxi_cve(self):

		for k,v in  self.msf_detail_dict.items():
			if v.startswith("auxiliary"):
				self.auxiliary_detail_dict[k] = v
				# print "*"*65
				# print k,v
		# print len(self.auxiliary_detail_dict)
		return self.auxiliary_detail_dict

	def msf_exploit_cve(self):

		for k,v in  self.msf_detail_dict.items():
			if v.startswith("exploit"):
				self.exploit_detail_dict[k] = v
				# a[k] = v
				# print "*"*65
				# print k,v	
		
		return self.exploit_detail_dict
		# print len(self.exploit_detail_dict)

	def msf_post_cve(self):

		for k,v in  self.msf_detail_dict.items():
			if v.startswith("post"):
				self.post_detail_dict[k] = v
				# print "*"*65
				# print k,v	

		return self.post_detail_dict
		


'''

use following command to get all info related to exploits and and their cve numbers 
test = subprocess.Popen(["ruby","/usr/share/metasploit-framework/tools/modules/module_reference.rb","-t","CVE", "-o", "/root/Desktop/celery_setup.txt/dj_file_upload/hicarser/msf_module_result/msf_module_cve.txt"], stdout=subprocess.PIPE)
>>> output = test.communicate()[0]




>>> output






raw script 




# temp_lst = []
# exploit_detail_dict = {}
# def par(file):
# 	with open(file) as fp:
# 		while True: 
# 			line = fp.readline() 
	 
# 			if not line: 
# 				break
# 			# print "*"*34
# 			temp_lst=  line.replace(" ","")
# 			temp_lst = temp_lst.split("CVE")
	
# 			temp_vr = 1
# 			temp_exploi_save = ''
# 			for i in temp_lst:
# 				if temp_vr == 1:
# 					# print i
# 					temp_exploi_save = i
# 				else:
# 					temp_cve_save = "CVE"+i
# 					temp_cve_save = temp_cve_save.replace("","")

# 					exploit_detail_dict[temp_cve_save] = temp_exploi_save
# 				temp_vr +=1

# 	for k,i in  exploit_detail_dict.items():
# 		print "*"*65
# 		print k,i



# par("resul.txt")









'''
				






















#!/usr/bin/python
# import re

# line = "Cats / smarter than dogs";
# line = 'post/windows/gather/forensics/duqu_check                               CVE-2011-3402'
# line = 'exploit/windows/tftp/tftpdwin_long_filename                            CVE-2006-4948'
# searchObj = re.search( r'(.*)/(.*?) .*', line, re.M|re.I)

# if searchObj:
#    print "searchObj.group() : ", searchObj.group()
#    print "searchObj.group(1) : ", searchObj.group(1)
#    print "searchObj.group(2) : ", searchObj.group(2)
# else:
#    print "Nothing found!!"