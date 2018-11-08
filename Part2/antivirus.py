import os
class Anti_virus(object):
	
	'''this is basically the UI, prompt the user for a virus
	definition file, a directory to scan and call the appropriate
	methods'''
	def __init__(self):
		pass
	
	'''open the file passed and read all the definitions, then
	save them to the self.offset_defs variable. '''
	def read_definitions(self, filename):
		self.offset_defs

	'''gets files in dir recursively and run check_file on each,
	then if a bad file is returned runs nullify_and_quarantine'''
	def check_dir(self, dir):
		pass

	'''read the file and run _convert_to_offset then compare
	the output with self.offset_defs.

	@returns a tuple of filename and the integer offset of 
	the start of infected sequence'''
	def check_file(self, filename):
		contence = []
		with open(filename, "rb") as file:

			byte = b'0'
			bytes = []
			while byte != b'':
				bytes.append(byte)
				byte = file.read(1);
			bytes = bytes[1:-1]

			contence = self._convert_to_offset(bytes)
			print(self.offset_defs)
			print(contence)

		for definition in self.offset_defs:
			i = 0
			for i in range(len(contence)-len(definition)):
				for j in range(len(definition)):
					if contence[i+j] != definition[j]:
						break
				else:
					print(filename, i)
					return (filename, i)


	'''set the first 8 bytes of the sequence to "xxxxxxxx", then
	move the file to some directory'''
	def nullify_and_quarantine(self, filename, first_byte_index):

		#print(os.listdir())
		with open(filename, 'r') as myFile:
			data = myFile.read()

		#print(data)
		dataList = list(data)
		for i in range(first_byte_index, first_byte_index+8):
			dataList[i] = "x"

		newData = ''.join(dataList);
		#print(newData)


		pass


	'''convert an array of bytes into an array of integer offsets.
	The offsets should be the first byte minus the next byte.
	This is probably the easiest way of handling the caesar-cipher

	@returns a list of integer offsets'''
	def _convert_to_offset(self, bytes):
		prevByte = 0;
		offsets = []

		for byte in bytes:
			byte = int.from_bytes(byte, "big")
			offsets.append(byte-prevByte)
			prevByte = byte
		offsets = offsets[1:]
		return offsets
