import sys
import math

filename = "total.search.set"


def getConfusionMatrix(filename, threshold, sp=-2, cp=-1):
    confusion_m = [[0.0, 0.0], [0.0, 0.0]]  # row1 neg set, row2 pos set
    with open(filename) as f:
        for line in f:
            v = line.rstrip().split()
            if int(v[cp]) == 0:
                i = 1
            if int(v[cp]) == 1:
                i = 0
            if float(v[sp]) < threshold:
                j = 1
            else:
                j = 0
            confusion_m[i][j] += 1
    print('''	   True Neg  || False positive %r
	   ======================
	   False Neg || True positive  %r ''' % (confusion_m[0], confusion_m[1]))
    return confusion_m


def printPerformance(matrix):
    TP = matrix[1][1]
    TN = matrix[0][0]
    FP = matrix[0][1]
    FN = matrix[1][0]
    acc = (TP + TN) / (sum(matrix[0]) + sum(matrix[1]))
    d = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
    mc = ((TP * TN) - (FP * FN)) / d
    precision = TP / (TP + FP)
    TPR = (TP) / (TP + FN)
    FPR = (FP) / (FP + TN)
    print('>>', 'TPR ', TPR, 'FPR ', FPR, 'Q2=', acc, 'MCC ', mc, 'PRECISION ', precision)


if __name__ == '__main__':
    th = float("1E-5")  # threshold
    score_pos = -2  # position of the score
    if len(sys.argv) > 3:
        score_pos = int(sys.argv[3]) - 1
    print('Threshold ', th)
    cm = getConfusionMatrix(filename, th, score_pos)
    printPerformance(cm)
