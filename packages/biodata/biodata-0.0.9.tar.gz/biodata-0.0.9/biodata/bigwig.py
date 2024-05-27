try:
	import pyBigWig
	_SUPPORT_BIGWIG = True
except:
	_SUPPORT_BIGWIG = False


from .baseio import BaseIReader
from genomictools import GenomicCollection, GenomicPos

class BigWigIReader(BaseIReader):
	def __init__(self, f, normalization=None, missing_data_mode="zero"):
		if not _SUPPORT_BIGWIG:
			raise Exception("bigwig is not supported without pyBigWig.")
		# missing
		self.bw = pyBigWig.open(f)
		
		if normalization is None:
			self.normalization_factor = 1
		elif isinstance(normalization, str):
			if normalization == "rpm":
				self. normalization_factor = 1000000/abs(self.bw.header()["sumData"])
			else:
				raise Exception("Unknown normalization method")
		elif isinstance(normalization, int) or isinstance(normalization, float):
			self.normalization_factor = normalization
		else:
			raise Exception()
		if missing_data_mode == "zero":
			self.missing_data_value = 0
		elif missing_data_mode == "nan":
			self.missing_data_mode = float("nan")
		
	def _intervals_generator(self):
		bw = self.bw
		for chrom in bw.chroms():
			# This condition avoids problems if a chromosome info is included but the region is not
			if bw.intervals(chrom) is not None:
				for interval in bw.intervals(chrom):
					yield (chrom, *interval)
			
	def value(self, r, method="sum"):
		'''
		Return a value processed across a selected region. It could be sum, max, abssum
		Some bigwig data also contain negative data and thus abs could be useful
		The value is always calculated exactly
		
		'''
		if r is None:
			raise Exception()
		elif isinstance(r, GenomicCollection):
			raise Exception()
		else:
			r = GenomicPos(r)
			if r.name not in self.bw.chroms():
				return 0
			zstart = r.start - 1
			ostop = r.stop
			intervals = self.bw.intervals(r.name, zstart, ostop)
			if method == "sum":
				if intervals is None:
					return 0
				return sum((min(i_ostop, ostop) - max(i_zstart, zstart)) * v for i_zstart, i_ostop, v in intervals) * self.normalization_factor
			elif method == "abssum":
				if intervals is None:
					return 0
				func = lambda vs: sum(abs(v) for v in vs)
				return func((min(i_ostop, ostop) - max(i_zstart, zstart)) * v for i_zstart, i_ostop, v in intervals) * self.normalization_factor
			elif method == "max":
				if intervals is None:
					return 0
				return func(v for i_zstart, i_ostop, v in intervals) * self.normalization_factor 
			elif method == "absmax":
				if intervals is None:
					return 0
				func = lambda vs: max(abs(v) for v in vs)
				return func(v for i_zstart, i_ostop, v in intervals) * self.normalization_factor 
			else:
				raise Exception()
	def values(self, r):
		'''
		Return a list of values of size length of r. Inefficient if the region is very large 
		'''
		r = r.genomic_pos
		d = self.values_dict(r)
		return [d[i+1] if i+1 in d else self.missing_data_value for i in range(r.zstart, r.ostop)]

	def values_dict(self, r):
		'''
		Return a dict of values. The key of dict is 1-based coordinate. Missing data is not put in the dictionary
		'''
		r = r.genomic_pos
		if r.name not in self.bw.chroms():
			return {}
		zstart = r.zstart
		ostop = r.ostop
		intervals = self.bw.intervals(r.name, zstart, ostop)
		if intervals is None:
			return {}
		return {p+1 : v * self.normalization_factor for i_zstart, i_ostop, v in intervals for p in range(max(i_zstart, zstart), min(i_ostop, ostop))}
		
	def intervals(self, r=None):
		'''
		Return all intervals that overlap with the target region
		'''
		raise Exception()
	
	def close(self):
		self.bw.close()
	
# class MultiBigWigIReader():
# 	def __init__(self, *fs, normalization=None):
# 		self.bws = [BigWigIReader(f, normalization=None) for f in fs] # Do not apply normalization to individual bws
# 		if normalization is None:
# 			self.normalization_factor = 1
# 		elif isinstance(normalization, str):
# 			if normalization == "rpm":
# 				sr = 0 
# 				for f in fs:
# 					bw = pyBigWig.open(f)
# 					sr += abs(bw.header()["sumData"])
# 					bw.close()
# 				self.normalization_factor = 1000000/sr
# 			else:
# 				raise Exception()
# 		elif isinstance(normalization, int):
# 			self.normalization_factor = normalization
# 		else:
# 			raise Exception()
# 			
# 	def value(self, r, method="sum"):
# 		vs = [bw.value(r, method) for bw in self.bws]
# 		if method == "sum" or method == "abssum":
# 			v = sum(vs)
# 		elif method == "max" or method == "absmax":
# 			v = max(vs) # absmax called in individual bw always return absolute value
# 		else:
# 			raise Exception()
# 		return v * self.normalization_factor
# 	
# 	def values_dict(self, r, method="sum"):
# 		'''
# 		method: sum, abssum, split_sign_sum, split_sign_abssum
# 		'''
# 		pass
# 	