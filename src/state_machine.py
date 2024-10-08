{
  "Comment": "Extract insights from images.",
  "StartAt": "Parallel",
  "States": {
    "Parallel": {
      "Type": "Parallel",
      "End": true,
      "Branches": [
        {
          "StartAt": "Lambda-Image metadata",
          "States": {
            "Lambda-Image metadata": {
              "Type": "Task",
              "Resource": "arn_da_função_lambda_de_extração_dos_metadados_do_arquivo",
              "End": true
            }
          }
        },
        {
          "StartAt": "Wait 10s",
          "States": {
            "Wait 10s": {
              "Type": "Wait",
              "Seconds": 10,
              "Next": "Lambda-Rekognition"
            },
            "Lambda-Rekognition": {
              "Type": "Task",
              "Resource": "arn_da_função_da_api_do_rekognition",
              "End": true
            }
          }
        }
      ]
    }
  }
}