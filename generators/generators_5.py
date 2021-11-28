# Compare the Memory performance of Normal functions and Generators
import memory_profiler as mem_profile

# Check the memory performance using Normal functions
brand_name = ["Apple","Sony","Samsung"]
price = ["90K","40K","30K"]
def product_list(n):
    output = []
    for i in range(n):
        product = {"id":i, "Brand_name": brand_name[0], "Price": price[0]}
        output.append(product)
    return output

print("Using Normal function")
print("Memory (Before):" + str(mem_profile.memory_usage()) + "MB")
list_of_order=product_list(10000000)
for i in list_of_order:
    continue
print("Memory (After):" + str(mem_profile.memory_usage()) + "MB")


#Check the memory performance using Generators
# print("Using generators")
# brand_name = ["Apple","Sony","Samsung"]
# price = ["90K","40K","30K"]
# def product_list(n):
#     for i in range(n):
#         product = {"id":i, "Brand_name": brand_name[0], "Price": price[0]}
#         yield product
# print("Memory (Before):" + str(mem_profile.memory_usage()) + "MB")
# list_of_order=product_list(10000000)
# for i in list_of_order:
#     continue
# print("Memory (After):" + str(mem_profile.memory_usage()) + "MB")