class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections =[]
        for i in range(len(firstList)):
            for j in range(len(secondList)):
                if firstList[i][1] < secondList[j][0]:
                    break
                elif secondList[j][1] < firstList[i][0]:
                    continue
                else:
                    intersections.append([max(firstList[i][0],secondList[j][0]),min(firstList[i][1],secondList[j][1])])
        
        return intersections

        