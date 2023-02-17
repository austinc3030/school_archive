class SBox(object):

    X_AXIS = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "0a", "0b", "0c", "0d", "0e", "0f"]
    Y_AXIS = ["00", "10", "20", "30", "40", "50", "60", "70", "80", "90", "a0", "b0", "c0", "d0", "e0", "f0"]    
    
    ROW_00 = ["63", "7c", "77", "7b", "f2", "6b", "6f", "c5", "30", "01", "67", "2b", "fe", "d7", "ab", "76"]
    ROW_10 = ["ca", "82", "c9", "7d", "fa", "59", "47", "f0", "ad", "d4", "a2", "af", "9c", "a4", "72", "c0"]
    ROW_20 = ["b7", "fd", "93", "26", "36", "3f", "f7", "cc", "34", "a5", "e5", "f1", "71", "d8", "31", "15"]
    ROW_30 = ["04", "c7", "23", "c3", "18", "96", "05", "9a", "07", "12", "80", "e2", "eb", "27", "b2", "75"]
    ROW_40 = ["09", "83", "2c", "1a", "1b", "6e", "5a", "a0", "52", "3b", "d6", "b3", "29", "e3", "2f", "84"]
    ROW_50 = ["53", "d1", "00", "ed", "20", "fc", "b1", "5b", "6a", "cb", "be", "39", "4a", "4c", "58", "cf"]
    ROW_60 = ["d0", "ef", "aa", "fb", "43", "4d", "33", "85", "45", "f9", "02", "7f", "50", "3c", "9f", "a8"]
    ROW_70 = ["51", "a3", "40", "8f", "92", "9d", "38", "f5", "bc", "b6", "da", "21", "10", "ff", "f3", "d2"]
    ROW_80 = ["cd", "0c", "13", "ec", "5f", "97", "44", "17", "c4", "a7", "7e", "3d", "64", "5d", "19", "73"]
    ROW_90 = ["60", "81", "4f", "dc", "22", "2a", "90", "88", "46", "ee", "b8", "14", "de", "5e", "0b", "db"]
    ROW_a0 = ["e0", "32", "3a", "0a", "49", "06", "24", "5c", "c2", "d3", "ac", "62", "91", "95", "e4", "79"]
    ROW_b0 = ["e7", "c8", "37", "6d", "8d", "d5", "4e", "a9", "6c", "56", "f4", "ea", "65", "7a", "ae", "08"]
    ROW_c0 = ["ba", "78", "25", "2e", "1c", "a6", "b4", "c6", "e8", "dd", "74", "1f", "4b", "bd", "8b", "8a"]
    ROW_d0 = ["70", "3e", "b5", "66", "48", "03", "f6", "0e", "61", "35", "57", "b9", "86", "c1", "1d", "9e"]
    ROW_e0 = ["e1", "f8", "98", "11", "69", "d9", "8e", "94", "9b", "1e", "87", "e9", "ce", "55", "28", "df"]
    ROW_f0 = ["8c", "a1", "89", "0d", "bf", "e6", "42", "68", "41", "99", "2d", "0f", "b0", "54", "bb", "16"] 

    ROW_ARRAY = [ROW_00, ROW_10, ROW_20, ROW_30, ROW_40, ROW_50, ROW_60, ROW_70,
                 ROW_80, ROW_90, ROW_a0, ROW_b0, ROW_c0, ROW_d0, ROW_e0, ROW_f0]
                      
                      
    def __init__(self):
        """
        Build the sbox dictionary so elements can be referenced by their hexadecimal indexes
        """
        self.sbox = {}
        # Build SBox
        for y_int_index, y_hex_index in enumerate(self.Y_AXIS):
            row_array = self.ROW_ARRAY[y_int_index]
            hex_row = {}
            for x_int_index, x_hex_index in enumerate(self.X_AXIS):
                hex_row[x_hex_index] = row_array[x_int_index]
            
            self.sbox[y_hex_index] = hex_row


    def get_sbox(self):
        """
        Generates the initial state for the encryption operation

        :return: The class variable self.sbox
        """
        return self.sbox