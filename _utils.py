def make_dir(dir_name):
	try:
		if not(os.path.isdir(dir_name)):
			os.makedirs(os.path.join(dir_name))
	except OSError as e:
		if e.errno != errno.EEXIST:
			print("Failed to create directory!!!!!")
			raise