class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        j = 0
        for _ in range(len(students)):
            for _ in range(len(students)):
                if students[j] == sandwiches[j]:
                    del students[j]
                    del sandwiches[j]
                else:
                    students.append(students[j])
                    del students[j]
        return len(students)

a = Solution().countStudents([1,1,0,0],[0,1,0,1])
print(a)