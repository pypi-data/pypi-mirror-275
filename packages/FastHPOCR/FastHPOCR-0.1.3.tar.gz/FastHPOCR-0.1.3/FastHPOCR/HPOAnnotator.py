from FastHPOCR.cr.CRIndexKB import CRIndexKB
from FastHPOCR.cr.CandidateMatcher import CandidateMatcher
from FastHPOCR.cr.FormatResults import FormatResults
from FastHPOCR.cr.TextProcessor import TextProcessor
from FastHPOCR.util import AnnotationObject


class HPOAnnotator:
    crIndexKB = None

    def __init__(self, crDataFile):
        self.crIndexKB = CRIndexKB()
        self.crIndexKB.load(crDataFile)

    def annotate(self, text: str, longestMatch=False) -> [AnnotationObject]:
        textProcessor = TextProcessor(self.crIndexKB)
        textProcessor.process(text)

        candidateMatcher = CandidateMatcher(self.crIndexKB)
        candidateMatcher.matchCandidates(textProcessor.getCandidates())

        result = FormatResults(text, self.crIndexKB, candidateMatcher.getMatches(), longestMatch).getResult()
        return result

    def printResults(self, annotationList, includeCategoriesIfPresent=False):
        lines = []
        for annotationObject in annotationList:
            if includeCategoriesIfPresent:
                lines.append(annotationObject.toStringWithCategories())
            else:
                lines.append(annotationObject.toString())
        print('\n'.join(lines))

    def serialize(self, annotationList, fileOut, includeCategoriesIfPresent=False):
        lines = []
        for annotationObject in annotationList:
            if includeCategoriesIfPresent:
                lines.append(annotationObject.toStringWithCategories())
            else:
                lines.append(annotationObject.toString())
        with open(fileOut, 'w') as fh:
            fh.write('\n'.join(lines))


def main():
    hpoAnnotator = HPOAnnotator('/Users/tudor/Desktop/FFF/Test/hp.index')

    text = 'cancer'
    result = hpoAnnotator.annotate(text)
    hpoAnnotator.serialize(result, '/Users/tudor/Desktop/FFF/Test/res.txt', includeCategoriesIfPresent=True)


if __name__ == '__main__':
    main()
