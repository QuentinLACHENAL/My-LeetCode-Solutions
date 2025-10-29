/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i;
    int j;
    int *solution;

    i = 0;
    while(i < numsSize - 1)
    {
        j = 1;
        while (j < numsSize)
        {
            if (i == j)
            {
                j++;
                continue ;
            }
            if ((nums[i] + nums[j]) == target)
            {
                *returnSize = 2;
                solution = malloc(sizeof(int) * 2);
                solution[0] = i;
                solution[1] = j;
                return(solution);
            }
            j++;
        }
        i++;
    }
    return (NULL);
}
