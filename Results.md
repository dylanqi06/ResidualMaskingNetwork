***resnet34***

**JAFFE: Train on Jaffe, test on Jaffe:**

Accuracy on private test with tta: 90.909

**Chinese: Train on Chinese, test on Chinese:**

Accuracy on private test with tta: 91.667

**Asian: Train on Asian, test on Asian:**

Accuracy on private test with tta: 93.333

**Mixed: Train on FER2013, test on Asian:**

Accuracy on private test with tta: 38.936 

***resmasking_dropout1***

**JAFFE: Train on Jaffe, test on Jaffe:**

Accuracy on private test with tta: 9.091

**Chinese: Train on Chinese, test on Chinese:**

Accuracy on private test with tta: 83.333

**Asian: Train on Asian, test on Asian:**

Accuracy on private test with tta: 87.619

**Mixed: Train on FER2013, test on Asian:**

Accuracy on private test with tta: 36.467 (tta = 5)

***resmasking_dropout2***

**JAFFE: Train on Jaffe, test on Jaffe:**

Accuracy on private test with tta: 9.091

**Chinese: Train on Chinese, test on Chinese:**

Accuracy on private test with tta: 85.714

**Asian: Train on Asian, test on Asian:**

Accuracy on private test with tta: 81.905

**Mixed: Train on FER2013, test on Asian:**

Accuracy on private test with tta: 38.367

***resmasking***

**JAFFE: Train on Jaffe, test on Jaffe:**

Accuracy on private test with tta: 9.091

**Chinese: Train on Chinese, test on Chinese:**

Accuracy on private test with tta: 84.524

**Asian: Train on Asian, test on Asian:**

Accuracy on private test with tta: 85.714

***resnet18***

**Mixed: Train on FER2013, test on Asian:**

Accuracy on private test with tta: 36.407  

***resnet50***

**Mixed: Train on FER2013, test on Asian:**

Accuracy on private test with tta: 40.551 

***resatt18***

**Mixed: Train on FER2013, test on Asian:**

Accuracy on private test with tta: 42.165 


| Model/Dataset           | JAFFE   | Chinese | Asian  |  Eafe  | Mixed  |
|-------------------------|---------|---------|--------|--------|--------|
| **resnet34**            | 90.909  | 91.667  | 93.333 | 88.100 | 38.936 |
| **resmasking_dropout1** | 9.091   | 83.333  | 87.619 | 82.300 | 36.467 |
| **resmasking_dropout2** | 9.091   | 85.714  | 81.905 | 80.500 | 38.367 |
| **resmasking**          | 9.091   | 84.524  | 85.714 | 83.800 |        |
| **resnet50**            |         |         | 56.190 | 82.600 | 40.551 |
| **resnet18**            |         |         | 87.619 | 81.900 | 36.407 |
| **resatt18**            |         |         | 89.524 | 82.700 | 42.165 |

| Model/Dataset           | FER2013 | Asian  |  Eafe  | Mixed  |
|-------------------------|---------|--------|--------|--------|
| **resnet34**            | 73.140  | 93.333 | 88.100 | 38.936 |
| **resmasking_dropout1** | 67.122  | 87.619 | 82.300 | 36.467 |
| **resmasking**          | 68.292  | 85.714 | 83.800 |        |
| **resnet50**            | 66.369  | 56.190 | 82.600 | 40.551 |
| **resnet18**            | 66.704  | 87.619 | 81.900 | 36.407 |
| **resatt18**            | 68.738  | 89.524 | 82.700 | 42.165 |


ResNet18 
ResNet34 
ResNet50 
ResAtt18 
ResAtt34 
ResMask 
ResMask_Dropout
