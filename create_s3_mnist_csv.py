import boto3
import requests
import numpy as np

s3 = boto3.client('s3')

# Load training dataset
resp = requests.get('https://pjreddie.com/media/files/mnist_train.csv')

with open('temp.csv', 'wb') as f:
    f.write(resp.content)

data = np.loadtxt('temp.csv', delimiter=',')

# Split into X, y, and reshape
X_train = data.T[1:].T.reshape(-1,784)
y_train = data.T[:1].T.reshape(-1)

# Upload both X and y into S3
np.savetxt('X_train.csv', X_train, delimiter=',')
s3.upload_file(
    'X_train.csv',
    'jakechenawspublic',
    'sample_data/mnist/train/images/images.csv'
)

np.savetxt('y_train.csv', y_train, delimiter=',')
s3.upload_file(
    'y_train.csv',
    'jakechenawspublic',
    'sample_data/mnist/train/labels/labels.csv'
)


# Do the same with test set
resp = requests.get('https://pjreddie.com/media/files/mnist_test.csv')

with open('temp.csv', 'wb') as f:
    f.write(resp.content)

data = np.loadtxt('temp.csv', delimiter=',')

X_test = data.T[1:].T.reshape(-1,784)
y_test = data.T[:1].T.reshape(-1)

np.savetxt('X_test.csv', X_test, delimiter=',')

s3.upload_file(
    'X_test.csv',
    'jakechenawspublic',
    'sample_data/mnist/test/images/images.csv'
)

np.savetxt('y_test.csv', y_test, delimiter=',')

s3.upload_file(
    'y_test.csv',
    'jakechenawspublic',
    'sample_data/mnist/test/labels/labels.csv'
)

# Create a smaller X_test for streaming demos
X_test_sm = X_test[:5]

np.savetxt('X_test_sm.csv', X_test_sm, delimiter=',')

s3.upload_file(
    'X_test_sm.csv',
    'jakechenawspublic',
    'sample_data/mnist/test/images/images_sm.csv'
)
