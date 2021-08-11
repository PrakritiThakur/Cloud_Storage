import dropbox

class TransferData :
    def __init__(self,accesstoken):
        self.accestoken = accesstoken
    
    def uploadfiles(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.accestoken)
 
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    accessToken ='ZrJOB5oW34MAAAAAAAAAAb5_lHsolebKUMUWpE5odDa35Le9abibUz_QsS7aeqtA'
    transferData = TransferData(accessToken)

    file_from = input("Enter the file path to transfer")
    file_to = input("Enter the path to upload the file to dropbox")

    transferData.files_upload(file_from,file_to)
    print("File has been moved")

main()