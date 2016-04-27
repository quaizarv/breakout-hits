import numpy as np
import pylab as pl
from sklearn import svm, datasets
from sklearn.utils import shuffle
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import precision_recall_curve

lc = sklearn.ensemble.RandomForestClassifier(100)
lc.fit(trD, trC)
pas = lc.predict_proba(teD)


# Compute Precision-Recall and plot curve
precision, recall, thresholds = precision_recall_curve(teC, pas[:, 1])
area = auc(recall, precision)
print("Area Under Curve: %0.2f" % area)
pl.clf()
pl.plot(recall, precision, label='Precision-Recall curve')
pl.xlabel('Recall')
pl.ylabel('Precision')
pl.ylim([0.0, 1.05])
pl.xlim([0.0, 1.0])
pl.title('Precision-Recall example: AUC=%0.2f' % area)
pl.legend(loc="lower left")
pl.show()


# Plot ROC curve
pas = lc.predict_proba(teD)

# Compute ROC curve and area the curve
fpr, tpr, thresholds = roc_curve(teC, pas[:, 1])
roc_auc = auc(fpr, tpr)
print("Area under the ROC curve : %f" % roc_auc)

pl.clf()
pl.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
pl.plot([0, 1], [0, 1], 'k--')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.title('Receiver operating characteristic example')
pl.legend(loc="lower right")
pl.show()
