import dropbox

class uploadFiles:
    def TransferData():
        def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb') 
        dbx.files_upload(f.read(), file_to)

 