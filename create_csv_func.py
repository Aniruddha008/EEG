import csv 


header =  ['channel 1','channel 2','channel 3','channel 4','channel 5','channel 6','channel 7','channel 8'
  ,'channel 9','channel 10','channel 11','channel 12','channel 13','channel 14','channel 15','channel 16','channel 17'
  ,'channel 18','channel 19','output']

def create_csv(sample_list_1):
 with open('class_one_data.csv', 'w', newline= '') as file:
  id = 1
  index = 0
  
  writer = csv.DictWriter(file, fieldnames = header) 
  writer.writeheader()
  for i in range(0, len(sample_list_1)):
      writer.writerow({
          'channel 1' : sample_list_1[i][0],
          'channel 2': sample_list_1[i][1],
          'channel 3': sample_list_1[i][2],
          'channel 4': sample_list_1[i][3], 
          'channel 5': sample_list_1[i][4], 
          'channel 6': sample_list_1[i][5],
          'channel 7': sample_list_1[i][6],
          'channel 8': sample_list_1[i][7],
          'channel 9': sample_list_1[i][8],
          'channel 10': sample_list_1[i][9],
          'channel 11': sample_list_1[i][10],
          'channel 12': sample_list_1[i][11],
          'channel 13': sample_list_1[i][12],
          'channel 14': sample_list_1[i][13],
          'channel 15': sample_list_1[i][14],
          'channel 16': sample_list_1[i][15],
          'channel 17': sample_list_1[i][16],
          'channel 18': sample_list_1[i][17],
          'channel 19': sample_list_1[i][18],
          'output':'left',
          })
    id += 1
    index += 1