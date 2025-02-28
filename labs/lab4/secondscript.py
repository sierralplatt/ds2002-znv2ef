#!/Users/sierraplatt/anaconda3/bin/python3


import boto3
from urllib import request
import sys



def fetch_upload() :
        #takes URL and bucket_name as CL arg
        url=sys.argv[1]
        response= request.urlopen(url)
        gif=response.read()

        bucket_name=sys.argv[2]
        object_name= "new_file"

        s3= boto3.client('s3')

        resp = s3.put_object(
                 Body = gif,
                 Bucket = bucket_name,
                 Key = object_name
        )

        presigned_response=s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': bucket_name, 'Key': object_name},
                ExpiresIn=604800
                )
        print(presigned_response)

if __name__ == "__main__":
    fetch_upload()






