__author__ = 'morteano'
__author__ = 'helmer'
import Backprop_skeleton as Bp


# Class for holding your data - one object for each line in the dataset
class dataInstance:
    def __init__(self, qid, rating, features):
        self.qid = qid  # ID of the query
        self.rating = rating  # Rating of this site for this query
        self.features = features  # The features of this query-site pair.

    def __str__(self):
        return "Datainstance - qid: " + str(self.qid) + ". rating: " + str(self.rating) + ". features: " + str(
            self.features)


# A class that holds all the data in one of our sets (the training set or the testset)
class dataHolder:
    def __init__(self, dataset):
        self.dataset = self.loadData(dataset)

    def loadData(self, file):
        # Input: A file with the data.
        # Output: A dict mapping each query ID to the relevant documents, like this: dataset[queryID] = [dataInstance1, dataInstance2, ...]
        data = open(file)
        dataset = {}
        for line in data:
            # Extracting all the useful info from the line of data
            lineData = line.split()
            rating = int(lineData[0])
            qid = int(lineData[1].split(':')[1])
            features = []
            for elem in lineData[2:]:
                if '#docid' in elem:  # We reached a comment. Line done.
                    break
                features.append(float(elem.split(':')[1]))
            # Creating a new data instance, inserting in the dict.
            di = dataInstance(qid, rating, features)
            if qid in dataset.keys():
                dataset[qid].append(di)
            else:
                dataset[qid] = [di]
        return dataset


def runRanker(trainingset, testset):
    # Dataholders for training and testset
    dhTraining = dataHolder(trainingset)
    dhTesting = dataHolder(testset)

    # Creating an ANN instance - feel free to experiment with the learning rate (the third parameter).
    nn = Bp.NN(46, 10, 0.001)
    trainingPatterns = []  # For holding all the training patterns we will feed the network
    testPatterns = []  # For holding all the test patterns we will feed the network
    for qid in dhTraining.dataset.keys():
        # This iterates through every query ID in our training set
        dataInstance = dhTraining.dataset[qid]  # All data instances (query, features, rating) for query qid
        for firstData in range(len(dataInstance)):
            for secondData in range(firstData+1, len(dataInstance)):
                if dataInstance[firstData].rating > dataInstance[secondData].rating:
                    trainingPatterns.append((dataInstance[firstData].features, dataInstance[secondData].features))
                elif dataInstance[firstData].rating < dataInstance[secondData].rating:
                    trainingPatterns.append((dataInstance[secondData].features, dataInstance[firstData].features))

    for qid in dhTesting.dataset.keys():
        # This iterates through every query ID in our test set
        dataInstance = dhTesting.dataset[qid]
        for firstData in range(len(dataInstance)):
            for secondData in range(firstData+1, len(dataInstance)):
                if dataInstance[firstData].rating > dataInstance[secondData].rating:
                    testPatterns.append((dataInstance[firstData].features, dataInstance[secondData].features))
                elif dataInstance[firstData].rating < dataInstance[secondData].rating:
                    testPatterns.append((dataInstance[secondData].features, dataInstance[firstData].features))

    # Check ANN performance before training
    it = 25
    errorrateArr = [0]*(it+1)
    errorrateArr[0] = nn.countMisorderedPairs(testPatterns)
    for i in range(it):
        # Running 25 iterations, measuring testing performance after each round of training.
        # Training
        nn.train(trainingPatterns, iterations=1)
        # Check ANN performance after training.
        errorrateArr[i+1] = nn.countMisorderedPairs(testPatterns)
        print(str(i/(it-1)*100) + "% done")

    # Print error rate as a table
    print(" ")
    print("x y")
    for i in range(it+1):
        print(str(i) + " " + str(errorrateArr[i]))

runRanker("train.txt", "test.txt")
