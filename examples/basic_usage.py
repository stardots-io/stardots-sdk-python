from stardots_sdk import StarDots, CreateSpaceReq, UploadFileReq

client_key = "Your client key"
client_secret = "Your client secret"
sdk = StarDots(client_key, client_secret)

# 获取空间列表
try:
    space_list = sdk.get_space_list()
    print("Space list:", space_list)
except Exception as e:
    print("Error getting space list:", e)

# 创建空间
try:
    create_result = sdk.create_space(CreateSpaceReq(space="my-demo-space", public=True))
    print("Create space result:", create_result)
except Exception as e:
    print("Error creating space:", e)

# 上传文件
try:
    with open("example.txt", "rb") as f:
        upload_result = sdk.upload_file(UploadFileReq(space="my-demo-space", filename="example.txt", fileContent=f.read()))
    print("Upload result:", upload_result)
except Exception as e:
    print("Error uploading file:", e) 