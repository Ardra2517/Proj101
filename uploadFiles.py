import dropbox

class uploadFiles:
    def TransferData():
        def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb') 
        dbx.files_upload(f.read(), file_to)

 def main():
    access_token = 'sl.BF4xs5orT9rnSzWZYPtrizamw2fjTQhvE5G5TgDsCNx81I5nWDiTglSUnAbxKhECV7EWYNqNMz-EGS20lpxHAn0q1XRxGgqsqZLnGXmg0VPryekPChhOQkXFhBVR8O8g_-tTEuY'
    transferData = TransferData(access_token)

    file_from=input('Enter the file path to transfer')
    file_to=input('Enter the destination path')

    transferData.upload_file(file_from, file_to)
    print("File has been moved.")
