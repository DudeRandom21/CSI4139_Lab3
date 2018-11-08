class Anti_virus(object):
    '''this is basically the UI, prompt the user for a virus
    definition file, a directory to scan and call the appropriate
    methods'''

    def __init__(self):
        self.read_definitions("Virus definition file.txt")

    '''open the file passed and read all the definitions, then
    save them to the self.offset_defs variable. '''

    def read_definitions(self, filename):
        file = open(filename, 'rb')
        byteList = list()
        lineList = list()
        ofsetList= list()

        for line in file:
            lineL = line.__len__()

            byteList = list()

            for x in range(0, lineL):
                byteList.append(line[x])

            lineList.append(byteList)

        for objects in lineList:
            print (objects)
            ofsetList.append(self._convert_to_offset(objects))


    '''gets files in dir recursively and run check_file on each,
    then if a bad file is returned runs nullify_and_quarantine'''

    def check_dir(self, dir):
        pass

    '''read the file and run _convert_to_offset then compare
    the output with self.offset_defs.

    @returns a tupple of filename and the integer offset of 
    the start of infected sequence'''

    def check_file(self, filename):
        pass

    '''set the first 8 bytes of the sequence to "xxxxxxxx", then
    move the file to some directory'''

    def nullify_and_quarantine(self, filename, first_byte_index):
        pass

    '''convert an array of bytes into an array of integer offsets.
    The offsets should be the first byte minus the next byte.
    This is probably the easiest way of handling the caesar-cipher

    @returns a list of integer offsets'''

    def _convert_to_offset(self, bytes):
        pass


thing = Anti_virus()
