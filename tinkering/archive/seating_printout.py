num_rows = int(input("Num rows: "))
num_cols = int(input("Num cols: "))

# row = 1
# while row <= 3:
#     col = "A"
#     while col <= "D":
#         print(f"{row}{col}", end=" ")
#         col = chr(ord(col) + 1)
#     row += 1

row = 1
while row <= num_rows:
    col = "A"
    while col < chr(ord("A") + num_cols):
        print(f"{row}{col}", end=" ")
        col = chr(ord(col) + 1)
    row += 1
