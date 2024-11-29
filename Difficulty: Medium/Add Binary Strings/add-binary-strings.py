#User function Template for python3
class Solution:
    def addBinary(self, s1, s2):
        # Convert input strings to lists for easier manipulation
        a = list(s1)
        b = list(s2)
        
        # Prepare the result list 'c' with extra space for possible carry
        c = ['0'] * (max(len(s1), len(s2)) + 1)
        
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        k = len(c) - 1
        
        # Loop to process both strings
        while i >= 0 and j >= 0:
            # Check bits from both strings and carry
            if a[i] == '0' and b[j] == '0':
                if carry == 0:
                    c[k] = '0'
                else:
                    c[k] = '1'
                    carry = 0
            elif a[i] == '0' and b[j] == '1' or a[i] == '1' and b[j] == '0':
                if carry == 0:
                    c[k] = '1'
                else:
                    c[k] = '0'
                    carry = 1
            elif a[i] == '1' and b[j] == '1':
                if carry == 0:
                    c[k] = '0'
                    carry = 1
                else:
                    c[k] = '1'
                    carry = 1
            
            # Move indices
            i -= 1
            j -= 1
            k -= 1
        
        # Process the remaining bits from the longer string if any
        while i >= 0:
            if carry == 0:
                c[k] = a[i]
            else:
                if a[i] == '1':
                    c[k] = '0'
                    carry = 1
                else:
                    c[k] = '1'
                    carry = 0
            i -= 1
            k -= 1
        
        while j >= 0:
            if carry == 0:
                c[k] = b[j]
            else:
                if b[j] == '1':
                    c[k] = '0'
                    carry = 1
                else:
                    c[k] = '1'
                    carry = 0
            j -= 1
            k -= 1
        
        # If there's still a carry left, add it at the highest place
        if carry == 1:
            c[k] = '1'
        
        # Join the list into a string, remove leading zeros, and return the result
        result = ''.join(c).lstrip('0')  # Remove leading zeros
        return result if result != '' else '0'  # Handle case where the result is "0"

		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends