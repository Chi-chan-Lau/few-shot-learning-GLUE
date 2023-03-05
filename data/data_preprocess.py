import json
import jsonlines

# sst-2
# write_file = open('sst2/advglue.dev','w')

# with open('dev.json', 'r') as file:
#     data = json.load(file)
#     sst2 = data['sst2']
#     for i in sst2:
#         write_file.write(str(i['label'])+' '+i['sentence']+'\n')

# write_file.close()


# rte
# write_file = jsonlines.open('rte/advglue.jsonl','w')

# with open('dev.json', 'r') as file:
#     data = json.load(file)
#     sst2 = data['rte']
#     for i in sst2:
#         json_dict = {}
#         json_dict['premise']=i['sentence1']
#         json_dict['hypothesis']=i['sentence2']
#         if i['label']==0:
#             json_dict['label']='entailment'
#         elif i['label']==1:
#             json_dict['label']='not_entailment'
#         json_dict['idx']=i['idx']
#         write_file.write(json_dict)

# write_file.close()


#qqp

# write_file = jsonlines.open('qqp/train.jsonl','w')

# with open('../../glue_data/QQP/train.tsv', 'r') as file:
#     total_text = file.readlines()
#     total_text = total_text[1:]
#     for i in range(len(total_text)):
#         split_text = total_text[i].split('\t')
#         json_dict={}
#         json_dict['idx']=int(split_text[0])
#         json_dict['question1']=split_text[3]
#         json_dict['question2']=split_text[4]
#         json_dict['label']=int(split_text[5].strip('\n'))
#         write_file.write(json_dict)

# write_file.close()

# write_file = jsonlines.open('qqp/advglue.jsonl','w')

# with open('dev.json', 'r') as file:
#     data = json.load(file)
#     sst2 = data['qqp']
#     for i in sst2:
#         write_file.write(i)

# write_file.close()


#mnli

write_file = jsonlines.open('mnli/advglue-mm.jsonl','w')

with open('dev.json', 'r') as file:
    data = json.load(file)
    sst2 = data['mnli-mm']
    for i in sst2:
        if i['label']==2:
            i['label']='contradiction'
        elif i['label']==1:
            i['label']='neutral'
        elif i['label']==0:
            i['label']='entailment'
        write_file.write(i)

write_file.close()



# write_file = jsonlines.open('mnli/train.jsonl','w')

# with open('../../glue_data/MNLI/train.tsv', 'r') as file:
#     total_text = file.readlines()
#     total_text = total_text[1:]
#     for i in range(len(total_text)):
#         split_text = total_text[i].split('\t')
#         json_dict={}
#         json_dict['idx']=int(split_text[0])
#         json_dict['premise']=split_text[8]
#         json_dict['hypothesis']=split_text[9]
#         json_dict['label']=split_text[11].strip('\n')
#         write_file.write(json_dict)

# write_file.close()


# write_file = jsonlines.open('mnli-mm/val.jsonl','w')

# with open('../../glue_data/MNLI/dev_mismatched.tsv', 'r') as file:
#     total_text = file.readlines()
#     total_text = total_text[1:]
#     for i in range(len(total_text)):
#         split_text = total_text[i].split('\t')
#         json_dict={}
#         json_dict['idx']=int(split_text[0])
#         json_dict['premise']=split_text[8]
#         json_dict['hypothesis']=split_text[9]
#         json_dict['label']=split_text[15].strip('\n')
#         write_file.write(json_dict)

# write_file.close()


#qnli

# write_file = jsonlines.open('qnli/val.jsonl','w')

# with open('../../glue_data/QNLI/dev.tsv', 'r') as file:
#     total_text = file.readlines()
#     total_text = total_text[1:]
#     for i in range(len(total_text)):
#         split_text = total_text[i].split('\t')
#         json_dict={}
#         json_dict['idx']=int(split_text[0])
#         json_dict['question']=split_text[1]
#         json_dict['sentence']=split_text[2]
#         json_dict['label']=split_text[3].strip('\n')
#         write_file.write(json_dict)

# write_file.close()



# write_file = jsonlines.open('qnli/advglue.jsonl','w')

# with open('dev.json', 'r') as file:
#     data = json.load(file)
#     sst2 = data['qnli']
#     for i in sst2:
#         if i['label']==1:
#             i['label']='not_entailment'
#         elif i['label']==0:
#             i['label']='entailment'
#         write_file.write(i)

# write_file.close()