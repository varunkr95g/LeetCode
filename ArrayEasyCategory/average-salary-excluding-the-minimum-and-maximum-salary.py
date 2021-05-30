class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        sal_max=float(max(salary))
        sal_min=float(min(salary))
        
        
        sal_sum=float(sum(salary))
        
        sal_avg=float((sal_sum-sal_max-sal_min)/(len(salary) - 2))
        
        return sal_avg
