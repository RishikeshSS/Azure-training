from azure.storage.blob import BlockBlobService
from flask import Flask, render_template, request

app = Flask(__name__)

# Azure Blob Storage configurations
account_name = "azuretrainingrishi"
account_key = "9em4lIXPytARTcoTEZP+AQjg5SyJkMEGIOziPeejUW6ijd9oKpJERW1+xoXLG2zb+CAG5N/6L0zb+AStr+2KPA=="
container_name = "container1"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        folder_name = request.form["folder_name"]
        block_blob_service = BlockBlobService(
            account_name=account_name, account_key=account_key
        )

        # List blobs inside the specified folder
        folder_blobs = []
        blobs = block_blob_service.list_blobs(container_name, prefix=folder_name)
        for blob in blobs:
            folder_blobs.append(blob.name)

        return render_template(
            "htmlcode.html", folder_name=folder_name, blobs=folder_blobs
        )

    # Get a list of folders to populate the dropdown
    block_blob_service = BlockBlobService(
        account_name=account_name, account_key=account_key
    )
    folders = []
    blobs = block_blob_service.list_blobs(container_name)
    for blob in blobs:
        folder = blob.name.split("/")[0]  # Extract the folder name from the blob name
        if folder and folder not in folders:
            folders.append(folder)

    return render_template("htmlcode.html", folders=folders)


if __name__ == "__main__":
    app.run(debug=True)
