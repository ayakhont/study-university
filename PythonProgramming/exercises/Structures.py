from operator import itemgetter


class Structures:

    # constructor with initializing all structures that we will use
    def __init__(self):
        self.emptyList = list()
        self.listOfStrings = ["a", "b", "c"]
        self.listOgMixedTypes = [1, 2.0, "abc", [1, 2]]
        self.emptyDict = dict()
        self.someDict = {1: "one", 3: "three"}
        self.listOfLists = [[4, 5, 6], [3, 2, 10], [7, 8, 9]]

    # some playing with list structures
    def playing_with_list(self):
        structures = self
        structures.emptyList.append(structures.listOfStrings)
        structures.emptyList.append(structures.listOgMixedTypes)
        print("listOfStrings and listOgMixedTypes have been appended to empty list: ", structures.emptyList)

        for element in structures.emptyList:
            print("Element in cycle: ", element)

        structures.emptyList.pop()
        print("After pop method the result is: ", structures.emptyList)

        structures.emptyList.extend(structures.listOgMixedTypes)
        print("After extend method the result is: ", structures.emptyList)

    # some playing with dictionary structures
    def playing_with_dictionaries(self):
        structures = self
        structures.emptyDict.update({2: "two"})
        print("emptyDict was updated by new element: ", structures.emptyDict)

        structures.someDict.update(structures.emptyDict)
        print("someDict was updated by emptyDict: ", structures.someDict)

        # and now absolutely madness from style of programming point of view
        structures.someDict.update({4: structures.listOfStrings})
        print("someDict was updated by listOfStrings: ", structures.someDict)

    def playing_with_sorting(self):
        structures = self
        sortedStructure = sorted(structures.listOfLists, key=itemgetter(1))
        print("Sorted list: ", sortedStructure)


newStructures = Structures()
newStructures.playing_with_list()
newStructures.playing_with_dictionaries()
newStructures.playing_with_sorting()



