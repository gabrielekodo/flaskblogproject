# text = "This is a sample text for cutting."
# length_to_cut = 10
#
# # Cut from the beginning
# cut_text_start = text[:length_to_cut]
# print(f"Cut from beginning: {cut_text_start}")
#
# # Cut from a specific index to the end
# start_index = 15
# cut_text_end = text[start_index:]
# print(f"Cut from index 15 to end: {cut_text_end}")
#
# # Cut a specific segment
# segment_start = 5
# segment_end = 12
# cut_segment = text[segment_start:segment_end]
# print(f"Cut segment from index 5 to 12: {cut_segment}")
#
# text = "This is a longer piece of text that needs to be truncated."
# max_length = 20
#
# if len(text) > max_length:
#     truncated_text = text[:max_length - 3] + "..."  # -3 for the ellipsis
# else:
#     truncated_text = text
#
# print(f"Truncated text with ellipsis: {truncated_text}")


# users=[
#     {
#         'name':"peter",
#         'age':20
#     },
#     {
#         'name': "john",
#         'age': 19
#     }
# ]
#
# new_list=[{**user, "id":index} for index, user in users]
# print(new_list)

data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}, {'id': 3, 'name': 'Charlie'}, {'id': 4, 'name': 'Bob'}]
search_name = 'Bob'

# Find all dictionaries where 'name' is 'Bob'
results = [d for d in data if d['name'] == search_name]
print(results)