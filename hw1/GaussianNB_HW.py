from sklearn.datasets import make_blobs, make_classification, make_gaussian_quantiles
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8))
plt.subplots_adjust(bottom=0.05, top=0.9, left=0.05, right=0.95)

plt.subplot(321)
plt.title('Training dataset', fontsize="small")
trainX, trainY = make_classification(
    n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1
)
plt.scatter(trainX[:, 0], trainX[:, 1], marker="o", c=trainY, s=25, edgecolors="k")

plt.subplot(322)
plt.title('Test dataset', fontsize="small")
testX, testY = make_classification(
    n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1
)
plt.scatter(testX[:, 0], testX[:, 1], marker="o", c=testY, s=25, edgecolors="k")

clf = GaussianNB()
clf.fit(trainX, trainY)

predY = clf.predict(testX)

plt.subplot(323)
plt.title('GaussianNB predict', fontsize="small")
plt.scatter(testX[:, 0], testX[:, 1], marker="o", c=predY, s=25, edgecolors="k")

plt.show()