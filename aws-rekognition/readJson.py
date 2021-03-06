from PIL import Image, ImageDraw

response = {'Labels': [{'Name': 'Traffic Light', 'Confidence': 98.84614562988281, 'Instances': [{'BoundingBox': {'Width': 0.09542803466320038, 'Height': 0.054648105055093765, 'Left': 0.6379751563072205, 'Top': 0.025586599484086037}, 'Confidence': 98.84614562988281}, {'BoundingBox': {'Width': 0.100229412317276, 'Height': 0.057023629546165466, 'Left': 0.37981897592544556, 'Top': 0.021756276488304138}, 'Confidence': 93.4988784790039}], 'Parents': [{'Name': 'Light'}]}, {'Name': 'Light', 'Confidence': 98.84614562988281, 'Instances': [], 'Parents': []}, {'Name': 'Road', 'Confidence': 98.15386199951172, 'Instances': [], 'Parents': []}, {'Name': 'Pedestrian', 'Confidence': 83.07437133789062, 'Instances': [], 'Parents': []}, {'Name': 'Car', 'Confidence': 81.62721252441406, 'Instances': [{'BoundingBox': {'Width': 0.10168305784463882, 'Height': 0.13919740915298462, 'Left': 0.29563549160957336, 'Top': 0.6274600028991699}, 'Confidence': 81.62721252441406}, {'BoundingBox': {'Width': 0.06280136853456497, 'Height': 0.12636396288871765, 'Left': 0.38132497668266296, 'Top': 0.6371245384216309}, 'Confidence': 73.0966567993164}], 'Parents': [{'Name': 'Vehicle'}, {'Name': 'Transportation'}]}, {'Name': 'Transportation', 'Confidence': 81.62721252441406, 'Instances': [], 'Parents': []}, {'Name': 'Vehicle', 'Confidence': 81.62721252441406, 'Instances': [], 'Parents': [{'Name': 'Transportation'}]}, {'Name': 'Automobile', 'Confidence': 81.62721252441406, 'Instances': [], 'Parents': [{'Name': 'Vehicle'}, {'Name': 'Transportation'}]}, {'Name': 'Tarmac', 'Confidence': 73.10357666015625, 'Instances': [], 'Parents': []}, {'Name': 'Asphalt', 'Confidence': 73.10357666015625, 'Instances': [], 'Parents': []}], 'LabelModelVersion': '2.0', 'ResponseMetadata': {'RequestId': '3c6acc43-ed14-4d15-891f-bb601007becd', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '3c6acc43-ed14-4d15-891f-bb601007becd', 'content-type': 'application/x-amz-json-1.1', 'content-length': '1587', 'date': 'Tue, 12 Oct 2021 01:59:26 GMT'}, 'RetryAttempts': 0}}

photo = 'roadImage.png'
img = Image.open(photo)

imgWidth, imgHeight = img.size
draw = ImageDraw.Draw(img)

# print('Name : ', response['Labels'][0]['Name'])
# print('Confidence : ', response['Labels'][0]['Confidence'])


if response['Labels'][0]['Instances'] != []:
    for i in range(len(response['Labels'][0]['Instances'])):
        # print('Locate %d : '%i, response['Labels'][0]['Instances'][i])
        box = response['Labels'][0]['Instances'][i]['BoundingBox']
        left = imgWidth * box['Left']
        top = imgHeight * box['Top']
        width = imgWidth * box['Width']
        height = imgHeight * box['Height']

        points = (
            (left,top),
            (left + width, top),
            (left + width, top + height),
            (left , top + height),
            (left, top)
        )
        draw.line(points, fill='#00d400', width=2)

img.show()