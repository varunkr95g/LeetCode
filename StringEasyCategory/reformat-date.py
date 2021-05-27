class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        month=0
        sub_arr=date.split(" ")
        
        # print (sub_arr)
        
        if(sub_arr[1]=="Jan"):
            month="01"
        elif(sub_arr[1]=="Feb"):
            month="02"
        elif(sub_arr[1]=="Mar"):
            month="03"
        elif(sub_arr[1]=="Apr"):
            month="04"
        elif(sub_arr[1]=="May"):
            month="05"
        elif(sub_arr[1]=="Jun"):
            month="06"
        elif(sub_arr[1]=="Jul"):
            month="07"
        elif(sub_arr[1]=="Aug"):
            month="08"
        elif(sub_arr[1]=="Sep"):
            month="09"
        elif(sub_arr[1]=="Oct"):
            month="10"
        elif(sub_arr[1]=="Nov"):
            month="11"
        elif(sub_arr[1]=="Dec"):
            month="12"
        
        if(len(sub_arr[0])==3):
            sub_arr[0]="0"+sub_arr[0]
        
        # print (sub_arr[0])
        
        a= sub_arr[2]+"-"+str(month)+"-"+sub_arr[0]

        return a[0:10]
