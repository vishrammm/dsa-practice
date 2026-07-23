def previous_smaller(arr):
    stack = []
    ans = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        if stack:
            ans[i] = stack[-1]

        stack.append(i)

    return ans


def next_smaller(arr):
    n = len(arr)
    stack = []
    ans = [n] * n

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        if stack:
            ans[i] = stack[-1]

        stack.append(i)

    return ans


def largestRectangleArea(heights):
    pse = previous_smaller(heights)
    nse = next_smaller(heights)

    ans = 0

    for i in range(len(heights)):
        width = nse[i] - pse[i] - 1
        area = heights[i] * width
        ans = max(ans, area)

    return ans


heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))