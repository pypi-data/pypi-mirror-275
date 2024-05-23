import convert.json_line
import convert.json_file
import convert.string_line
import convert.audio_ar
import convert.alpaca

json_line = {'name': 'json_line', 'convert': convert.json_line.convert_data}
json_file = {'name': 'json_file', 'convert': convert.json_file.convert_data}
string_line = {'name': 'string_line', 'convert': convert.string_line.convert_data}
audio_ar = {'name': 'audio_ar', 'convert': convert.audio_ar.convert_data}
alpaca = {'name': 'alpaca', 'convert': convert.alpaca.convert_data}

data_type_list = [json_line, json_file, string_line, audio_ar, alpaca]