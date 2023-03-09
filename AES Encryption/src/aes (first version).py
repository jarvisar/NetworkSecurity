def hex2bin(hex_str):
    return ''.join([bin(int(c, 16))[2:].zfill(4) for c in hex_str])

def bin2hex(bin_str):
    return ''.join([hex(int(bin_str[i:i+4], 2))[2:].zfill(1) for i in range(0, len(bin_str), 4)])

def sub_bytes(state):
    # Replace the state matrix with values from s-box
	sbox = [
            0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
            0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
            0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
            0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
            0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
            0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
            0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
            0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
            0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
            0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
            0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
            0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
            0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
            0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
            0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
            0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16 ]
	for i in range(len(state)):
		state[i] = [int(x, 2) for x in state[i]]
		for j in range(len(state[i])):
			state[i][j] = format(sbox[state[i][j]], '08b')
	return state

def shift_rows(state):
    # Shift rows in the state matrix
    shifted_state = [''] * len(state)
    for i in range(len(state)):
        shifted_state[i] = state[i][i:] + state[i][:-i]
    return shifted_state

def mix_columns(state):
    # Mix columns in the state matrix
    mixed_state = [[''] * 4 for i in range(4)]
    mix_column_matrix = [['00000010', '00000011', '00000001', '00000001'],
                         ['00000001', '00000010', '00000011', '00000001'],
                         ['00000001', '00000001', '00000010', '00000011'],
                         ['00000011', '00000001', '00000001', '00000010']]
    for i in range(4):
        for j in range(4):
            mixed_state[i][j] = format(
                int(mix_column_matrix[i][0], 2) * int(state[0][j], 2) ^
                int(mix_column_matrix[i][1], 2) * int(state[1][j], 2) ^
                int(mix_column_matrix[i][2], 2) * int(state[2][j], 2) ^
                int(mix_column_matrix[i][3], 2) * int(state[3][j], 2), '08b'
            )
    return mixed_state


def add_key(state, key):
    # Add key to the state matrix
    for i in range(len(state)):
        state[i] = ''.join([format(int(str(state[i][j:j+4]), 2) ^ int(str(key[j * 4:j * 4 + 4]), 2), '04b') for j in range(0, 4, 4)])
    return state


	
# Read the plaintext from file
with open("../data/plaintext.txt", "r") as f:
    message = f.read().strip()

# Convert message to ASCII values
ascii_values = [ord(c) for c in message]

# Convert ASCII values to binary string
binary_str = ''.join([bin(c)[2:].zfill(8) for c in ascii_values])
print(binary_str)
# Initial state matrix
state = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
all = ''
for i in range(len(state)):
	all += state[i]
print(state)

# Read the subkeys from file
with open("../data/subkey_example.txt", "r") as f:
	subkeys = [hex2bin(line.strip()) for line in f]
	
print(subkeys[0])
	
# Add first subkey (subkey0)
add_key(state, subkeys[0])
print(state)

# Perform operations in Round 1
sub_bytes(state)

shift_rows(state)

mix_columns(state)
add_key(state, subkeys[1])

# Print result after the 1st round of AES encryption
result = ''
for i in range(4):
	result += ''.join(state[i])
print("result")
print(result)
print(bin2hex(result))

# Write result to file
with open("../data/result.txt", "w") as f:
    f.write(bin2hex(result))