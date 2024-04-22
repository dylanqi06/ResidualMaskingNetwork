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
| **resmasking_dropout1** | 9.091   | 83.333  | 87.619 |  | 36.467 |
| **resmasking_dropout2** | 9.091   | 85.714  | 81.905 |  | 38.367 |
| **resmasking**          | 9.091   | 84.524  | 85.714 |  |        |
| **resnet50**            |         |         |        |  | 40.551 |
| **resnet18**            |         |         |        |  | 36.407 |
| **resatt18**            |         |         | 89.524 | 82.700 | 42.165 |

