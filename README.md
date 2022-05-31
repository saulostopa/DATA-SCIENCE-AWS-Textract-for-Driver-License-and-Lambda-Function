<div id="top"></div>

<br />
<div align="center">
  <h1 align="center">Extract text with AWS Textract for Driver License</h1>
  <img src="images/logo.png" alt="License Plate Recognition" width="500">

  <br />
  
  <p align="center">
    Amazon Textract enables you to add document text detection and analysis to your applications. You provide a document image to the Amazon Textract API, and the service detects the document text.
    <br />
    <a href="https://docs.aws.amazon.com/textract/latest/dg/what-is.html"><strong>Explore the docs of the Amazon Textract »</strong></a>
    <br />
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

This project uses a Python API to recognition of the driver license to extract information of user.

<img src="images/screenshot.jpeg" />

## Built With

This section list the major frameworks/libraries/services used to bootstrap this project.

* [AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
* [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)
* [AWS API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
* [AWS Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html)

## How to use:

1. Configure your AWS Bucket S3

2. Upload your images that you want to recognize

3. Give the right permissions

4. Set the bucket_name and region in locate "src/functions/lambda_function.py"

5. Create your lambda function with right persmissions

6. Update your lambda function with code used in this project 

7. Call API bellow in Insomnia or Postman via GET sending the key as name of image to recognize stored on AWS S3.

<div align="center">
  <img src="src/images/driver-license-alabama.png" width="400" />
</div>
  
```sh
  https://abcdefghijkl.lambda-url.us-east-1.on.aws/?key=driver-license-ex10.jpeg
  ```

8. See the result template below.

```sh
  [
    {
      "Type": {
        "Text": "FIRST_NAME"
      },
      "ValueDetection": {
        "Text": "CONNOR",
        "Confidence": 97.5824203491211
      }
    },
    {
      "Type": {
        "Text": "LAST_NAME"
      },
      "ValueDetection": {
        "Text": "SAMPLE",
        "Confidence": 99.63204193115234
      }
    },
    {
      "Type": {
        "Text": "MIDDLE_NAME"
      },
      "ValueDetection": {
        "Text": "HUGH B",
        "Confidence": 94.02507781982422
      }
    },
    {
      "Type": {
        "Text": "SUFFIX"
      },
      "ValueDetection": {
        "Text": "",
        "Confidence": 99.67054748535156
      }
    },
    {
      "Type": {
        "Text": "CITY_IN_ADDRESS"
      },
      "ValueDetection": {
        "Text": "MONTGOMERY",
        "Confidence": 97.9351806640625
      }
    },
    {
      "Type": {
        "Text": "ZIP_CODE_IN_ADDRESS"
      },
      "ValueDetection": {
        "Text": "361041234",
        "Confidence": 98.50426483154297
      }
    },
    {
      "Type": {
        "Text": "STATE_IN_ADDRESS"
      },
      "ValueDetection": {
        "Text": "AL",
        "Confidence": 99.36796569824219
      }
    },
    {
      "Type": {
        "Text": "STATE_NAME"
      },
      "ValueDetection": {
        "Text": "ALABAMA",
        "Confidence": 64.47396850585938
      }
    },
    {
      "Type": {
        "Text": "DOCUMENT_NUMBER"
      },
      "ValueDetection": {
        "Text": "1234567",
        "Confidence": 98.24909973144531
      }
    },
    {
      "Type": {
        "Text": "EXPIRATION_DATE"
      },
      "ValueDetection": {
        "Text": "01-05-2014",
        "NormalizedValue": {
          "Value": "2014-01-05T00:00:00",
          "ValueType": "Date"
        },
        "Confidence": 98.22144317626953
      }
    },
    {
      "Type": {
        "Text": "DATE_OF_BIRTH"
      },
      "ValueDetection": {
        "Text": "01-05-1948",
        "NormalizedValue": {
          "Value": "1948-01-05T00:00:00",
          "ValueType": "Date"
        },
        "Confidence": 97.7793960571289
      }
    },
    {
      "Type": {
        "Text": "DATE_OF_ISSUE"
      },
      "ValueDetection": {
        "Text": "01-05-2010",
        "NormalizedValue": {
          "Value": "2010-01-05T00:00:00",
          "ValueType": "Date"
        },
        "Confidence": 97.62773895263672
      }
    },
    {
      "Type": {
        "Text": "ID_TYPE"
      },
      "ValueDetection": {
        "Text": "DRIVER LICENSE FRONT",
        "Confidence": 98.75053405761719
      }
    },
    {
      "Type": {
        "Text": "ENDORSEMENTS"
      },
      "ValueDetection": {
        "Text": "",
        "Confidence": 99.68603515625
      }
    },
    {
      "Type": {
        "Text": "VETERAN"
      },
      "ValueDetection": {
        "Text": "",
        "Confidence": 99.60050201416016
      }
    },
    {
      "Type": {
        "Text": "RESTRICTIONS"
      },
      "ValueDetection": {
        "Text": "A",
        "Confidence": 98.69237518310547
      }
    },
    {
      "Type": {
        "Text": "CLASS"
      },
      "ValueDetection": {
        "Text": "D",
        "Confidence": 99.1164779663086
      }
    },
    {
      "Type": {
        "Text": "ADDRESS"
      },
      "ValueDetection": {
        "Text": "",
        "Confidence": 47.532798767089844
      }
    },
    {
      "Type": {
        "Text": "COUNTY"
      },
      "ValueDetection": {
        "Text": "",
        "Confidence": 99.65638732910156
      }
    },
    {
      "Type": {
        "Text": "PLACE_OF_BIRTH"
      },
      "ValueDetection": {
        "Text": "",
        "Confidence": 99.60488891601562
      }
    }
  ]
  ```
