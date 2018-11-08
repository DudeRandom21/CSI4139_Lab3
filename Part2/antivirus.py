import os
import shutil
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


		pass


	'''set the first 8 bytes of the sequence to "xxxxxxxx", then
	move the file to some directory'''
	def nullify_and_quarantine(self, filename, first_byte_index):

		#print(os.listdir())
		with open(filename, 'r') as myFile:
			data = myFile.read()

		dataList = list(data)
		for i in range(first_byte_index, first_byte_index+8):
			dataList[i] = "x"

		newData = ''.join(dataList)


		with open(filename, 'a') as myFile:
			# delete file contents
			myFile.seek(0)
			myFile.truncate()

			#replace file contents with new data containing sequence of x's
			myFile.write(newData)

		shutil.move(filename, "QuarantineFolder/"+filename)
		print("File moved to Quarantine File")

		myFile.close





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





def main():
	test = Anti_virus();
	test.nullify_and_quarantine("eicar.txt",10)


if __name__ == "__main__":
	main()


